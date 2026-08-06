from pathlib import Path

from django.http import FileResponse, HttpResponse

BASE_DIR = Path(__file__).resolve().parent.parent
DIST_ROOT = BASE_DIR / 'frontend' / 'dist'


def dist_file(request, rel_path):
    """从 frontend/dist 提供多页面构建产物，未知路径回退到首页。"""
    candidate = (DIST_ROOT / rel_path).resolve()
    if candidate.is_file() and str(candidate).startswith(str(DIST_ROOT)):
        return FileResponse(candidate.open('rb'))

    index = DIST_ROOT / 'index.html'
    if not index.exists():
        return HttpResponse('前端尚未构建：请在 frontend 目录执行 npm run build', status=503)
    return FileResponse(index.open('rb'))


def spa_index(request):
    """Django 托管 Vue 多页面构建产物。"""
    rel_path = request.path.lstrip('/')
    if rel_path:
        return dist_file(request, rel_path)
    return dist_file(request, 'index.html')
