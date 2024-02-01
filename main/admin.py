from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'published')
    list_filter = ('published',)
    search_fields = ('title', 'author__username')
    actions = ['publish_posts', 'unpublish_posts']

    def publish_posts(self, request, queryset):
        queryset.update(published=True)
    publish_posts.short_description = "Publish selected posts"

    def unpublish_posts(self, request, queryset):
        queryset.update(published=False)
    unpublish_posts.short_description = "Unpublish selected posts"

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_at', 'approved')
    list_filter = ('approved',)
    search_fields = ('user__username', 'post__title', 'coffee_experience')
    actions = ['approve_comments', 'disapprove_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
    approve_comments.short_description = "Approve selected comments"

