from django.contrib import admin

from .models import Contract, MatchSchedule, NewsArticle, PlayerProfile, Product


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
