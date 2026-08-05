from pathlib import Path

from django.http import FileResponse, HttpResponse

BASE_DIR = Path(__file__).resolve().parent.parent


def spa_index(request):
    """生产环境由 Django 托管 Vue 构建产物（单页应用）。"""
    index = BASE_DIR / 'frontend' / 'dist' / 'index.html'
    if not index.exists():
        return HttpResponse('前端尚未构建：请在 frontend 目录执行 npm run build', status=503)
    return FileResponse(index.open('rb'))
