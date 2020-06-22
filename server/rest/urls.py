from django.urls import path

from .views import PostLists

urlpatterns = [
        path('posts/', PostLists.as_view(), name="all_posts"),
        
]
