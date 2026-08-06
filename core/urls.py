from django.urls import path

from . import views

urlpatterns = [
    path('api/home/', views.home_api, name='home_api'),
    path('api/contact/', views.contact_api, name='contact_api'),
    path('api/news/', views.NewsApiView.as_view(), name='news_api'),
    path('api/news/<int:item_id>/', views.NewsApiView.as_view(), name='news_api_detail'),
    path('api/news/<int:item_id>', views.NewsApiView.as_view(), name='news_api_detail_no_slash'),
    path('api/players/', views.PlayerApiView.as_view(), name='players_api'),
    path('api/players/<int:item_id>/', views.PlayerApiView.as_view(), name='players_api_detail'),
    path('api/players/<int:item_id>', views.PlayerApiView.as_view(), name='players_api_detail_no_slash'),
    path('api/matches/', views.MatchApiView.as_view(), name='matches_api'),
    path('api/matches/<int:item_id>/', views.MatchApiView.as_view(), name='matches_api_detail'),
    path('api/matches/<int:item_id>', views.MatchApiView.as_view(), name='matches_api_detail_no_slash'),
    path('api/products/', views.ProductApiView.as_view(), name='products_api'),
    path('api/products/<int:item_id>/', views.ProductApiView.as_view(), name='products_api_detail'),
    path('api/products/<int:item_id>', views.ProductApiView.as_view(), name='products_api_detail_no_slash'),
]
