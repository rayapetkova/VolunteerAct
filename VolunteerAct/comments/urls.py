from django.urls import path

from VolunteerAct.comments.views import CommentListApiView, CommentDetailsApiView, CommentEditAndDeleteApiView

urlpatterns = [
    path('events/<int:eventId>/', CommentListApiView.as_view(), name='list-create-comments-api'),
    path('<int:pk>/', CommentDetailsApiView.as_view(), name='details-comment-api'),
    path('<int:pk>/edit_delete', CommentEditAndDeleteApiView.as_view(), name='edit-delete-comment-api')
]
