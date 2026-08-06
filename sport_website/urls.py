"""
URL configuration for sport_website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, path, re_path
from django.views.static import serve as media_serve

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]

# Django 直接托管 media 目录，打包后的本地版也无需依赖 Vite
urlpatterns.append(
    re_path(r'^media/(?P<path>.*)$', media_serve, {'document_root': settings.MEDIA_ROOT})
)

# Vue 单页应用兜底路由（排除 admin/api/media/static）
urlpatterns.append(
    re_path(r'^(?!admin/|api/|media/|static/).*', views.spa_index, name='spa_index')
)
