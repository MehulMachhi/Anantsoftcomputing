from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    Category, Tag, Author, Post, PostEngagement,
    Comment, NewsletterSubscriber
)

class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'full_name', 'email']

    def get_full_name(self, obj):
        return obj.get_full_name() or obj.username

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id', 'name', 'slug', 'description', 'icon',
            'meta_title', 'meta_description', 'is_active',
            'display_order', 'created_at'
        ]

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug', 'description', 'created_at']

class AuthorSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Author
        fields = [
            'id', 'user', 'avatar', 'bio', 'role',
            'linkedin_url', 'twitter_url', 'github_url',
            'website_url', 'is_featured', 'created_at'
        ]

class PostEngagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostEngagement
        fields = [
            'views', 'unique_views', 'likes',
            'shares', 'bookmarks'
        ]

class CommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            'id', 'post', 'parent', 'author_name',
            'author_email', 'content', 'is_approved',
            'created_at', 'replies'
        ]
        read_only_fields = ['is_approved']

    def get_replies(self, obj):
        if obj.parent is None:  # Only get replies for parent comments
            replies = Comment.objects.filter(parent=obj)
            return CommentSerializer(replies, many=True).data
        return []

class PostListSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    engagement = PostEngagementSerializer(read_only=True)

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'excerpt', 'author',
            'category', 'tags', 'featured_image',
            'featured_image_alt', 'status', 'is_featured',
            'read_time', 'engagement', 'published_at', "content"
        ]

class PostDetailSerializer(PostListSerializer):
    comments = serializers.SerializerMethodField()

    class Meta(PostListSerializer.Meta):
        fields = PostListSerializer.Meta.fields + [
            'content', 'meta_title', 'meta_description',
            'keywords', 'comments', 'created_at', 'updated_at'
        ]

    def get_comments(self, obj):
        # Only get parent comments
        comments = obj.comments.filter(parent=None, is_approved=True)
        return CommentSerializer(comments, many=True).data

class NewsletterSubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterSubscriber
        fields = ['id', 'email', 'name', 'is_active', 'subscribed_at']
        read_only_fields = ['is_active', 'subscribed_at']