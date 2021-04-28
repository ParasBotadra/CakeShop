from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog_posts.models import Post
from blog_posts.serializers import PostSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class UserRegistration(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostCollection(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        serializer = PostSerializer(data=data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class PostElement(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        post_element = Post.objects.get(id=pk)
        serializer = PostSerializer(post_element)
        return Response(serializer.data)



