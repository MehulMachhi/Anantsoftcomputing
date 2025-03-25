# blog/admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Category , Tag , Author , Post , PostEngagement ,
    Comment , NewsletterSubscriber
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name' , 'slug' , 'is_active' , 'display_order')
    list_filter = ('is_active' ,)
    search_fields = ('name' , 'description')
    prepopulated_fields = {'slug': ('name' ,)}
    ordering = ('display_order' , 'name')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name' , 'slug' , 'created_at')
    search_fields = ('name' , 'description')
    prepopulated_fields = {'slug': ('name' ,)}
    ordering = ('name' ,)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('get_full_name' , 'role' , 'is_featured' , 'avatar_preview')
    list_filter = ('is_featured' ,)
    search_fields = ('user__username' , 'user__first_name' , 'user__last_name' , 'bio')

    def get_full_name(self , obj):
        return obj.user.get_full_name() or obj.user.username

    get_full_name.short_description = 'Name'

    def avatar_preview(self , obj):
        if obj.avatar:
            return format_html(
                '<img src="{}" style="max-height: 50px;"/>' ,
                obj.avatar.url
            )
        return "No Avatar"

    avatar_preview.short_description = 'Avatar'


class PostEngagementInline(admin.StackedInline):
    model = PostEngagement
    can_delete = False


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostEngagementInline]
    list_display = (
        'title' , 'author' , 'category' , 'status' ,
        'is_featured' , 'published_at' , 'get_engagement'
    )
    list_filter = ('status' , 'category' , 'is_featured' , 'author')
    search_fields = ('title' , 'excerpt' , 'content')
    prepopulated_fields = {'slug': ('title' ,)}
    filter_horizontal = ('tags' ,)
    date_hierarchy = 'published_at'

    fieldsets = (
        ('Basic Information' , {
            'fields': ('title' , 'slug' , 'author' , 'excerpt' , 'content')
        }) ,
        ('Categorization' , {
            'fields': ('category' , 'tags')
        }) ,
        ('Media' , {
            'fields': ('featured_image' , 'featured_image_alt')
        }) ,
        ('Publishing' , {
            'fields': ('status' , 'is_featured' , 'read_time' , 'published_at')
        }) ,
        ('SEO' , {
            'fields': ('meta_title' , 'meta_description' , 'keywords') ,
            'classes': ('collapse' ,)
        })
    )

    def get_engagement(self , obj):
        try:
            engagement = obj.engagement
            return f"👁️ {engagement.views} | ❤️ {engagement.likes} | 🔖 {engagement.bookmarks}"
        except PostEngagement.DoesNotExist:
            return "No engagement data"

    get_engagement.short_description = 'Engagement'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author_name' , 'post' , 'created_at' , 'is_approved')
    list_filter = ('is_approved' , 'created_at')
    search_fields = ('author_name' , 'author_email' , 'content' , 'post__title')
    actions = ['approve_comments']

    def approve_comments(self , request , queryset):
        queryset.update(is_approved=True)

    approve_comments.short_description = "Approve selected comments"


@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email' , 'name' , 'is_active' , 'subscribed_at')
    list_filter = ('is_active' , 'subscribed_at')
    search_fields = ('email' , 'name')
    actions = ['activate_subscribers' , 'deactivate_subscribers']

    def activate_subscribers(self , request , queryset):
        queryset.update(is_active=True)

    activate_subscribers.short_description = "Activate selected subscribers"

    def deactivate_subscribers(self , request , queryset):
        queryset.update(is_active=False)

    deactivate_subscribers.short_description = "Deactivate selected subscribers"