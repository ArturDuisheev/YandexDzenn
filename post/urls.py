
from django.urls import path

from . import views


urlpatterns = [
    path('create-post/', views.PostListCreateView.as_view()),
    path('<int:pk>/', views.PostRetrieveUpdateDeleteView.as_view()),
    path('comment/<int:post_id>/', views.CommentListCreateAPIView.as_view()),
    path('comment/<int:post_id>/comment/<int:pk>/', views.CommentRetrieveDestroyUpdateAPIView.as_view()),

    ]