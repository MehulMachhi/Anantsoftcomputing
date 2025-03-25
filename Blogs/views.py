from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.utils import timezone
from django.contrib.syndication.views import Feed
from django.urls import reverse
from django.utils.feedgenerator import Atom1Feed

from .models import (
    Category, Tag, Author, Post, PostEngagement,
    Comment, NewsletterSubscriber
)
from .serializers import (
    CategorySerializer, TagSerializer, AuthorSerializer,
    PostListSerializer, PostDetailSerializer, CommentSerializer,
    NewsletterSubscriberSerializer
)


class PostFeed(Feed):
    title = "Blog Posts"
    link = "/blog/"
    description = "Latest blog posts"
    feed_type = Atom1Feed

    def items(self):
        return Post.objects.filter(
            status='published',
            published_at__lte=timezone.now()
        ).order_by('-published_at')[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.excerpt

    def item_link(self, item):
        return reverse('blog:post-detail', args=[item.slug])

    def item_author_name(self, item):
        return str(item.author)

    def item_pubdate(self, item):
        return item.published_at
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['is_active']
    search_fields = ['name', 'description']
    ordering_fields = ['display_order', 'name']
    ordering = ['display_order', 'name']

    @action(detail=True)
    def posts(self , request , pk=None):
        """Get all posts in a category"""
        category = self.get_object()
        posts = Post.objects.filter(
            category=category ,
            status='published'
        ).order_by('-published_at')
        serializer = PostListSerializer(posts , many=True)
        return Response(serializer.data)

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']

    @action(detail=True)
    def posts(self , request , pk=None):
        """Get all posts with this tag"""
        tag = self.get_object()
        posts = Post.objects.filter(
            tags=tag ,
            status='published'
        ).order_by('-published_at')
        serializer = PostListSerializer(posts , many=True)
        return Response(serializer.data)

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['is_featured']
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'bio', 'role']

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'category', 'tags', 'author', 'is_featured']
    search_fields = ['title', 'excerpt', 'content']
    ordering_fields = ['published_at', 'created_at', 'read_time']
    ordering = ['-published_at']

    def get_queryset(self):
        if self.request.user.is_staff:
            return Post.objects.all()
        return Post.objects.filter(status='published')

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        return PostDetailSerializer

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        post = self.get_object()
        engagement, _ = PostEngagement.objects.get_or_create(post=post)
        engagement.likes += 1
        engagement.save()
        return Response({'status': 'liked', 'likes': engagement.likes})

    @action(detail=True, methods=['post'])
    def bookmark(self, request, pk=None):
        post = self.get_object()
        engagement, _ = PostEngagement.objects.get_or_create(post=post)
        engagement.bookmarks += 1
        engagement.save()
        return Response({'status': 'bookmarked', 'bookmarks': engagement.bookmarks})

    @action(detail=True , methods=['post'])
    def share(self , request , pk=None):
        """Track post shares"""
        post = self.get_object()
        engagement , _ = PostEngagement.objects.get_or_create(post=post)
        engagement.shares += 1
        engagement.save()
        return Response({'status': 'shared' , 'shares': engagement.shares})

    @action(detail=True)
    def related(self , request , pk=None):
        """Get related posts based on tags and category"""
        post = self.get_object()
        related_posts = Post.objects.filter(
            status='published' ,
            tags__in=post.tags.all()
        ).exclude(id=post.id).distinct()[:3]
        serializer = PostListSerializer(related_posts , many=True)
        return Response(serializer.data)

    @action(detail=True)
    def engagement_stats(self , request , pk=None):
        """Get detailed engagement statistics"""
        post = self.get_object()
        engagement , _ = PostEngagement.objects.get_or_create(post=post)
        return Response({
            'views': engagement.views ,
            'unique_views': engagement.unique_views ,
            'likes': engagement.likes ,
            'shares': engagement.shares ,
            'bookmarks': engagement.bookmarks ,
            'comments_count': post.comments.filter(is_approved=True).count()
        })

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['post', 'is_approved']
    ordering = ['-created_at']

    def get_queryset(self):
        if self.request.user.is_staff:
            return Comment.objects.all()
        return Comment.objects.filter(is_approved=True)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def approve(self, request, pk=None):
        comment = self.get_object()
        comment.is_approved = True
        comment.save()
        return Response({'status': 'approved'})

    @action(detail=True , methods=['post'] , permission_classes=[IsAuthenticated])
    def reject(self , request , pk=None):
        """Reject a comment"""
        comment = self.get_object()
        comment.is_approved = False
        comment.save()
        return Response({'status': 'rejected'})

    @action(detail=False , methods=['get'] , permission_classes=[IsAuthenticated])
    def pending(self , request):
        """Get all pending comments"""
        pending_comments = Comment.objects.filter(is_approved=False)
        serializer = self.get_serializer(pending_comments , many=True)
        return Response(serializer.data)

    @action(detail=True , methods=['post'] , permission_classes=[IsAuthenticated])
    def report_spam(self , request , pk=None):
        """Mark comment as spam and reject it"""
        comment = self.get_object()
        comment.is_approved = False
        comment.admin_notes = "Marked as spam"
        comment.save()
        # You could add additional spam handling here
        return Response({'status': 'marked as spam'})

class NewsletterSubscriberViewSet(viewsets.ModelViewSet):
    queryset = NewsletterSubscriber.objects.all()
    serializer_class = NewsletterSubscriberSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['email', 'name']

    def get_permissions(self):
        if self.action == 'create':
            return []
        return [IsAuthenticated()]