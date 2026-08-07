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
    path('api/auth/send-code/', views.send_verification_code_api, name='auth_send_code'),
    path('api/auth/register/', views.register_api, name='auth_register'),
    path('api/auth/login/', views.login_api, name='auth_login'),
    path('api/auth/me/', views.auth_me_api, name='auth_me'),
    path('api/auth/logout/', views.logout_api, name='auth_logout'),
    path('api/community/', views.CommunityApiView.as_view(), name='community_api'),
    path('api/community/hot/', views.community_hot_api, name='community_hot_api'),
    path('api/community/<int:item_id>/', views.CommunityApiView.as_view(), name='community_api_detail'),
    path('api/community/<int:item_id>', views.CommunityApiView.as_view(), name='community_api_detail_no_slash'),
]
