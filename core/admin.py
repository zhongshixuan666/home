from django.contrib import admin

from .models import CommunityPost, Contract, MatchSchedule, MemberProfile, NewsArticle, PlayerProfile, Product, VerificationCode


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'project_type', 'created_at')
    list_filter = ('project_type',)
    search_fields = ('name', 'phone', 'message')


@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date', 'is_published', 'created_at')
    list_filter = ('category', 'is_published')
    search_fields = ('title', 'excerpt')


@admin.register(PlayerProfile)
class PlayerProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'status', 'is_published', 'created_at')
    list_filter = ('country', 'is_published')
    search_fields = ('name', 'en_name', 'bio')


@admin.register(MatchSchedule)
class MatchScheduleAdmin(admin.ModelAdmin):
    list_display = ('event', 'date', 'match_type', 'is_published', 'created_at')
    list_filter = ('match_type', 'is_published')
    search_fields = ('event', 'venue', 'player_a', 'player_b')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'tag', 'rank', 'score', 'is_published', 'created_at')
    list_filter = ('tag', 'is_published')
    search_fields = ('name', 'desc')


@admin.register(MemberProfile)
class MemberProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'phone_verified', 'email_verified', 'created_at')
    list_filter = ('phone_verified', 'email_verified')
    search_fields = ('user__username', 'user__email', 'phone')


@admin.register(VerificationCode)
class VerificationCodeAdmin(admin.ModelAdmin):
    list_display = ('channel', 'account', 'code', 'purpose', 'expires_at', 'verified')
    list_filter = ('channel', 'purpose', 'verified')
    search_fields = ('account', 'code')


@admin.register(CommunityPost)
class CommunityPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'views', 'likes', 'hot_score', 'is_published', 'created_at')
    list_filter = ('category', 'is_published')
    search_fields = ('title', 'content', 'author')