from django.urls import path

from . import views

urlpatterns = [
    path('api/home/', views.home_api, name='home_api'),
    path('api/contact/', views.contact_api, name='contact_api'),
]
