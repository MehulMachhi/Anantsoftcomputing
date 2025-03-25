from django.urls import path, include
from django.utils.feedgenerator import Atom1Feed
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet, TagViewSet, AuthorViewSet, PostViewSet,
    CommentViewSet, NewsletterSubscriberViewSet, PostFeed
)

router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='blog-categories')
router.register('tags', TagViewSet, basename='blog-tags')
router.register('authors', AuthorViewSet, basename='blog-authors')
router.register('posts', PostViewSet, basename='blog-posts')
router.register('comments', CommentViewSet, basename='blog-comments')
router.register('newsletter', NewsletterSubscriberViewSet, basename='blog-newsletter')

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', PostFeed(), name='post-feed'),
    path('feed/atom/', PostFeed(), {'feed_type': Atom1Feed}, name='post-atom-feed'),
]