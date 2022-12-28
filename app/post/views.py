from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import BasePermission, CommentPermission


class PostListCreateView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication, ]
    permission_classes = [BasePermission, ]

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication, ]
    permission_classes = [BasePermission]


class CommentListCreateAPIView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        return self.queryset.filter(post_id=self.kwargs['post_id'])

    def perform_create(self, serializer):
        try:
            serializer.save(
                author=self.request.user,
                post=get_object_or_404(Post, id=self.kwargs['post_id'])
            )
        except ValueError:
            serializer.save(
                post=get_object_or_404(Post, id=self.kwargs['post_id'])
            )


class CommentRetrieveDestroyUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication, ]
    permission_classes = [CommentPermission, ]
