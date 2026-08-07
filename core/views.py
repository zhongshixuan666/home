import json
import re
import secrets
from datetime import datetime
from datetime import timedelta

from django.conf import settings
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.utils import timezone
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import (
    Contract,
    MatchSchedule,
    MemberProfile,
    NewsArticle,
    PlayerProfile,
    Product,
    VerificationCode,
    CommunityPost,
)


PHONE_RE = re.compile(r'^1[3-9]\d{9}$')
EMAIL_RE = re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$')
CODE_MINUTES = 5


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


def user_payload(user):
    profile = getattr(user, 'profile', None)
    return {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'phone': profile.phone if profile else '',
        'phone_verified': profile.phone_verified if profile else False,
        'email_verified': profile.email_verified if profile else False,
    }


def verify_code(channel, account, code):
    now = timezone.now()
    item = (
        VerificationCode.objects.filter(
            channel=channel,
            account__iexact=account,
            code=code,
            purpose='register',
            verified=False,
            expires_at__gt=now,
        )
        .order_by('-created_at')
        .first()
    )
    if not item:
        return False
    item.verified = True
    item.save(update_fields=['verified'])
    return True


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
            'community': '/api/community/',
            'community_hot': '/api/community/hot/',
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


@csrf_exempt
def send_verification_code_api(request):
    if request.method != 'POST':
        return JsonResponse({'error': '仅支持 POST 请求'}, status=405)

    data = parse_body(request)
    channel = clean_text(data.get('channel'))
    account = clean_text(data.get('account'))
    purpose = clean_text(data.get('purpose') or 'register')

    if channel == 'phone' and not PHONE_RE.match(account):
        return JsonResponse({'error': '请输入正确的 11 位手机号'}, status=400)
    if channel == 'email' and not EMAIL_RE.match(account):
        return JsonResponse({'error': '请输入正确的邮箱地址'}, status=400)
    if channel not in ('phone', 'email'):
        return JsonResponse({'error': '验证渠道仅支持 phone 或 email'}, status=400)

    code = f'{secrets.randbelow(1000000):06d}'
    VerificationCode.objects.create(
        channel=channel,
        account=account,
        code=code,
        purpose=purpose,
        expires_at=timezone.now() + timedelta(minutes=CODE_MINUTES),
    )

    payload = {'ok': True, 'message': '验证码已生成，5 分钟内有效'}
    if settings.DEBUG:
        payload['dev_code'] = code
    return JsonResponse(payload)


@csrf_exempt
def register_api(request):
    if request.method != 'POST':
        return JsonResponse({'error': '仅支持 POST 请求'}, status=405)

    data = parse_body(request)
    username = clean_text(data.get('username'))
    password = clean_text(data.get('password'))
    phone = clean_text(data.get('phone'))
    email = clean_text(data.get('email'))
    channel = clean_text(data.get('channel'))
    code = clean_text(data.get('code'))

    if not all([username, password, phone, email, channel, code]):
        return JsonResponse({'error': '请填写完整注册信息'}, status=400)
    if len(username) < 2:
        return JsonResponse({'error': '用户名至少 2 个字符'}, status=400)
    if len(password) < 6:
        return JsonResponse({'error': '密码至少 6 位'}, status=400)
    if not PHONE_RE.match(phone):
        return JsonResponse({'error': '请输入正确的 11 位手机号'}, status=400)
    if not EMAIL_RE.match(email):
        return JsonResponse({'error': '请输入正确的邮箱地址'}, status=400)
    if channel not in ('phone', 'email'):
        return JsonResponse({'error': '验证渠道仅支持 phone 或 email'}, status=400)

    account = phone if channel == 'phone' else email
    if not verify_code(channel, account, code):
        return JsonResponse({'error': '验证码错误或已过期'}, status=400)
    if User.objects.filter(username__iexact=username).exists():
        return JsonResponse({'error': '用户名已被注册'}, status=400)
    if User.objects.filter(email__iexact=email).exists():
        return JsonResponse({'error': '邮箱已被注册'}, status=400)
    if MemberProfile.objects.filter(phone=phone).exists():
        return JsonResponse({'error': '手机号已被注册'}, status=400)

    user = User.objects.create_user(username=username, email=email, password=password)
    MemberProfile.objects.create(
        user=user,
        phone=phone,
        phone_verified=channel == 'phone',
        email_verified=channel == 'email',
    )
    login(request, user)
    return JsonResponse({'ok': True, 'user': user_payload(user), 'message': '注册成功'}, status=201)


@csrf_exempt
def login_api(request):
    if request.method != 'POST':
        return JsonResponse({'error': '仅支持 POST 请求'}, status=405)

    data = parse_body(request)
    account = clean_text(data.get('account'))
    password = clean_text(data.get('password'))
    if not account or not password:
        return JsonResponse({'error': '请输入账号和密码'}, status=400)

    user = None
    try:
        user = User.objects.get(username__iexact=account)
    except User.DoesNotExist:
        profile = MemberProfile.objects.filter(phone=account).first()
        if profile:
            user = profile.user
        else:
            user = User.objects.filter(email__iexact=account).first()

    if not user:
        return JsonResponse({'error': '账号不存在，请检查用户名、手机号或邮箱'}, status=400)

    auth_user = authenticate(request, username=user.username, password=password)
    if not auth_user:
        return JsonResponse({'error': '密码不正确'}, status=400)

    login(request, auth_user)
    return JsonResponse({'ok': True, 'user': user_payload(auth_user), 'message': '登录成功'})


def auth_me_api(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': '未登录'}, status=401)
    return JsonResponse({'ok': True, 'user': user_payload(request.user)})


@csrf_exempt
def logout_api(request):
    if request.method != 'POST':
        return JsonResponse({'error': '仅支持 POST 请求'}, status=405)
    auth_logout(request)
    return JsonResponse({'ok': True, 'message': '已退出登录'})


class CommunityApiView(ContentApiView):
    model = CommunityPost
    label = '社区投稿'
    fields = (
        'title',
        'content',
        'author',
        'category',
        'views',
        'likes',
        'hot_score',
        'is_published',
        'created_at',
    )
    required = ('title', 'content', 'author')
    editable = (
        'title',
        'content',
        'author',
        'category',
        'views',
        'likes',
        'hot_score',
        'is_published',
    )
    boolean_fields = ('is_published',)

    def get_queryset(self):
        return self.model.objects.filter(is_published=True)


def community_hot_api(request):
    posts = (
        CommunityPost.objects.filter(is_published=True)
        .order_by('-hot_score', '-views', '-likes', '-created_at')[:10]
    )
    results = [
        serialize(post, ('title', 'category', 'views', 'likes', 'hot_score', 'created_at'))
        for post in posts
    ]
    return JsonResponse({'ok': True, 'count': len(results), 'results': results})