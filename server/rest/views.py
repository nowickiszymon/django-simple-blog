from django.shortcuts import render

# REST LIBS
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from blogcms.models import BlogPost
from .serialziers import BlogPostSerializer

class PostLists(APIView):
    """
    List all snippets
    """
    def get(self, request, format=None):
        blog_posts = BlogPost.objects.all()
        serializer = BlogPostSerializer(blog_posts, many=True)
        return Response(serializer.data)
