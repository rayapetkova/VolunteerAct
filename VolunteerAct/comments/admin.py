from django.contrib import admin

from VolunteerAct.comments.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
