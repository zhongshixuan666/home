import json
import re

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Contract


PHONE_RE = re.compile(r'^1[3-9]\d{9}$')


def home_api(request):
    return JsonResponse({
        'name': '羽界',
        'message': 'Django 后端连接成功，欢迎来到羽界！',
    })


@csrf_exempt
def contact_api(request):
    if request.method != 'POST':
        return JsonResponse({'error': '仅支持 POST 请求'}, status=405)
    try:
        data = json.loads(request.body)
    except (json.JSONDecodeError, UnicodeDecodeError):
        data = {}

    name = (data.get('name') or '').strip()
    phone = (data.get('phone') or '').strip()
    project_type = (data.get('project_type') or '').strip()
    message = (data.get('message') or '').strip()

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
