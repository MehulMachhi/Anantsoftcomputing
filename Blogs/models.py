# blog/models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50 , blank=True)  # For storing icons if needed
    meta_title = models.CharField(max_length=200 , blank=True)
    meta_description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    display_order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['display_order' , 'name']

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self , *args , **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args , **kwargs)


class Author(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='blog/authors/')
    bio = models.TextField()
    role = models.CharField(max_length=100)
    linkedin_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    website_url = models.URLField(blank=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username


class Post(models.Model):
    STATUS_CHOICES = [
        ('draft' , 'Draft') ,
        ('review' , 'In Review') ,
        ('published' , 'Published') ,
        ('archived' , 'Archived') ,
    ]

    # Basic Fields
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    excerpt = models.TextField(help_text="A short summary of the post")
    content = RichTextUploadingField()

    # Relations
    author = models.ForeignKey(Author , on_delete=models.PROTECT)
    category = models.ForeignKey(Category , on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag)

    # Media
    featured_image = models.ImageField(upload_to='blog/posts/')
    featured_image_alt = models.CharField(max_length=200)

    # Meta fields
    status = models.CharField(max_length=20 , choices=STATUS_CHOICES , default='draft')
    is_featured = models.BooleanField(default=False)
    read_time = models.PositiveIntegerField(help_text="Estimated reading time in minutes")

    # SEO fields
    meta_title = models.CharField(max_length=200 , blank=True)
    meta_description = models.TextField(blank=True)
    keywords = models.CharField(max_length=200 , blank=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True , blank=True)

    class Meta:
        ordering = ['-published_at' , '-created_at']

    def __str__(self):
        return self.title

    def save(self , *args , **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args , **kwargs)


class PostEngagement(models.Model):
    post = models.OneToOneField(Post , on_delete=models.CASCADE , related_name='engagement')
    views = models.PositiveIntegerField(default=0)
    unique_views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    shares = models.PositiveIntegerField(default=0)
    bookmarks = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Engagement for {self.post.title}"


class Comment(models.Model):
    post = models.ForeignKey(Post , on_delete=models.CASCADE , related_name='comments')
    parent = models.ForeignKey('self' , null=True , blank=True , on_delete=models.CASCADE)
    author_name = models.CharField(max_length=100)
    author_email = models.EmailField()
    content = models.TextField()
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Comment by {self.author_name} on {self.post.title}"


class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100 , blank=True)
    is_active = models.BooleanField(default=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email