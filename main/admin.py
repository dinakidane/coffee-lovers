from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'approved')
    list_filter = ('approved',)
    actions = ['approve_comments', 'disapprove_comments']
    search_fields = ['user', 'body']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

    def disapprove_comments(self, request, queryset):
        queryset.update(approved=False)

admin.site.register(Comment, CommentAdmin)
