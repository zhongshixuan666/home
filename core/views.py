import json
import re
from datetime import datetime

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import Contract, MatchSchedule, NewsArticle, PlayerProfile, Product


PHONE_RE = re.compile(r'^1[3-9]\d{9}$')


def parse_body(request):
    try:
        data = json.loads(request.body)
    except (json.JSONDecodeError, UnicodeDecodeError):
        return {}
    return data if isinstance(data, dict) else {}


def clean_text(value, default=''):
    if value is None:
        return default
    return str(value).strip()


def clean_bool(value, default=False):
    if isinstance(value, bool):
        return value
    if isinstance(value, str) and value.lower() in ('true', '1', 'yes', 'on'):
        return True
    if isinstance(value, str) and value.lower() in ('false', '0', 'no', 'off'):
        return False
    if value in (0, 1):
        return bool(value)
    return default


def serialize(obj, fields):
    data = {'id': obj.id}
    for field in fields:
        value = getattr(obj, field)
        if isinstance(value, datetime):
            value = value.isoformat()
        data[field] = value
    return data


@method_decorator(csrf_exempt, name='dispatch')
class ContentApiView(View):
    model = None
    label = '内容'
    fields = ()
    required = ()
    editable = ()
    boolean_fields = ()

    def get_queryset(self):
        return self.model.objects.all()

    def get(self, request, item_id=None):
        if item_id is not None:
            try:
                obj = self.get_queryset().get(id=item_id)
            except self.model.DoesNotExist:
                return JsonResponse({'error': '记录不存在'}, status=404)
            return JsonResponse({'ok': True, 'result': serialize(obj, self.fields)})

        results = [serialize(obj, self.fields) for obj in self.get_queryset()]
        return JsonResponse({'ok': True, 'count': len(results), 'results': results})

    def post(self, request, item_id=None):
        data = parse_body(request)
        missing = [field for field in self.required if not clean_text(data.get(field))]
        if missing:
            return JsonResponse({'error': f'请填写：{"、".join(missing)}'}, status=400)

        values = {}
        for field in self.editable:
            if field not in data:
                continue
            if field in self.boolean_fields:
                values[field] = clean_bool(data.get(field))
            else:
                values[field] = clean_text(data.get(field))

        obj = self.model.objects.create(**values)
        return JsonResponse({'ok': True, 'id': obj.id, 'message': f'{self.label}新增成功'}, status=201)

    def patch(self, request, item_id=None):
        if item_id is None:
            return JsonResponse({'error': '缺少记录 ID'}, status=400)
        try:
            obj = self.get_queryset().get(id=item_id)
        except self.model.DoesNotExist:
            return JsonResponse({'error': '记录不存在'}, status=404)

        data = parse_body(request)
        for field in self.editable:
            if field not in data:
                continue
            if field in self.boolean_fields:
                setattr(obj, field, clean_bool(data.get(field)))
            else:
                setattr(obj, field, clean_text(data.get(field)))
        obj.save()
        return JsonResponse({'ok': True, 'id': obj.id, 'message': f'{self.label}更新成功'})

    def delete(self, request, item_id=None):
        if item_id is None:
            return JsonResponse({'error': '缺少记录 ID'}, status=400)
        try:
            obj = self.get_queryset().get(id=item_id)
        except self.model.DoesNotExist:
            return JsonResponse({'error': '记录不存在'}, status=404)
        obj.delete()
        return JsonResponse({'ok': True, 'message': f'{self.label}删除成功'})

    def http_method_not_allowed(self, request, *args, **kwargs):
        return JsonResponse({'error': '仅支持 GET、POST、PATCH、DELETE 请求'}, status=405)


class NewsApiView(ContentApiView):
    model = NewsArticle
    label = '新闻'
    fields = ('title', 'category', 'date', 'excerpt', 'image', 'is_published', 'created_at')
    required = ('title',)
    editable = ('title', 'category', 'date', 'excerpt', 'image', 'is_published')
    boolean_fields = ('is_published',)


class PlayerApiView(ContentApiView):
    model = PlayerProfile
    label = '球员'
    fields = (
        'name',
        'en_name',
        'country',
        'birth',
        'height',
        'status',
        'style',
        'bio',
        'image',
        'video',
        'is_published',
        'created_at',
    )
    required = ('name',)
    editable = (
        'name',
        'en_name',
        'country',
        'birth',
        'height',
        'status',
        'style',
        'bio',
        'image',
        'video',
        'is_published',
    )
    boolean_fields = ('is_published',)


class MatchApiView(ContentApiView):
    model = MatchSchedule
    label = '比赛'
    fields = (
        'match_type',
        'date',
        'time',
        'event',
        'stage',
        'venue',
        'watch',
        'player_a',
        'player_b',
        'score',
        'result',
        'champion',
        'is_published',
        'created_at',
    )
    required = ('event',)
    editable = (
        'match_type',
        'date',
        'time',
        'event',
        'stage',
        'venue',
        'watch',
        'player_a',
        'player_b',
        'score',
        'result',
        'champion',
        'is_published',
    )
    boolean_fields = ('is_published',)


class ProductApiView(ContentApiView):
    model = Product
    label = '装备'
    fields = ('name', 'desc', 'image', 'tag', 'rank', 'score', 'is_published', 'created_at')
    required = ('name',)
    editable = ('name', 'desc', 'image', 'tag', 'rank', 'score', 'is_published')
    boolean_fields = ('is_published',)


def home_api(request):
    return JsonResponse({
        'name': '羽界',
        'message': 'Django 后端连接成功，欢迎来到羽界！',
        'api': {
            'news': '/api/news/',
            'players': '/api/players/',
            'matches': '/api/matches/',
            'products': '/api/products/',
        },
    })


@csrf_exempt
def contact_api(request):
    if request.method != 'POST':
        return JsonResponse({'error': '仅支持 POST 请求'}, status=405)
    data = parse_body(request)

    name = clean_text(data.get('name'))
    phone = clean_text(data.get('phone'))
    project_type = clean_text(data.get('project_type'))
    message = clean_text(data.get('message'))

    if not all([name, phone, project_type, message]):
        return JsonResponse({'error': '请填写完整表单'}, status=400)
    if not PHONE_RE.match(phone):
        return JsonResponse({'error': '联系电话格式不正确，请填写 11 位大陆手机号'}, status=400)

    Contract.objects.create(
        name=name,
        phone=phone,
        project_type=project_type,
        message=message,
    )
    return JsonResponse({'ok': True, 'message': '提交成功'})
