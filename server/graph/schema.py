import graphene

from graphene_django.types import DjangoObjectType

from blogcms.models import BlogPost

class BlogPostType(DjangoObjectType):
        class Meta:
                model = BlogPost

class Query(object):
        all_posts = graphene.List(BlogPostType)
        
        def resolve_all_posts(self, info, **kwargs):
                return BlogPost.objects.all()

