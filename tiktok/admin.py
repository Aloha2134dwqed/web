from django.contrib import admin
from .models import Category, ContentType, TikTokContent

admin.site.register(Category)
admin.site.register(ContentType)

@admin.register(TikTokContent)
class TikTokContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'content_type', 'views', 'likes', 'is_trending')
    list_filter = ('category', 'content_type', 'is_trending')
    search_fields = ('title', 'author')