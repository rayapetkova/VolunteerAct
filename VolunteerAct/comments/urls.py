from django.urls import path

from VolunteerAct.comments.views import CommentListApiView, CommentDetailsApiView

urlpatterns = [
    path('', CommentListApiView.as_view(), name='list-create-comments-api'),
    path('<int:pk>/', CommentDetailsApiView.as_view(), name='details-comment-api')
]
