from django.contrib import admin

from VolunteerAct.comments.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ('body', 'event__title')

    readonly_fields = ('created_at', 'updated_at')

    ordering = ('created_at', )
