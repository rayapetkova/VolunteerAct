from django.urls import path

from VolunteerAct.comments.views import CommentListApiView

urlpatterns = [
    path('', CommentListApiView.as_view(), name='list-create-comments-api')
]
