from django.urls import path

from VolunteerAct.comments.views import CommentListApiView, CommentEditAndDeleteApiView, comment_details_async_api_view

urlpatterns = [
    path('events/<int:eventId>/', CommentListApiView.as_view(), name='list-create-comments-api'),
    path('<int:pk>/', comment_details_async_api_view, name='details-comment-api'),
    path('<int:pk>/edit_delete', CommentEditAndDeleteApiView.as_view(), name='edit-delete-comment-api')
]
