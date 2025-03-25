# portfolio/models.py
from django.db import models


class ProjectCategory(models.Model):
    name = models.CharField(max_length=100)  # e.g., 'CRM Systems', 'Healthcare'
    identifier = models.SlugField(unique=True)  # e.g., 'crm', 'healthcare'
    description = models.TextField(blank=True)
    display_order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Project Category"
        verbose_name_plural = "Project Categories"
        ordering = ['display_order' , 'name']

    def __str__(self):
        return self.name


class Technology(models.Model):
    name = models.CharField(max_length=100)  # e.g., 'Python', 'Django', 'React'
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Technology"
        verbose_name_plural = "Technologies"
        ordering = ['name']
    
    def __str__(self):
        return self.name
        
    
class Project(models.Model):
    GRADIENT_CHOICES = [
        ('primary' , 'From Primary 400 to Primary 600') ,
        ('secondary' , 'From Secondary 400 to Secondary 600') ,
        ('accent' , 'From Accent 400 to Accent 600') ,
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(ProjectCategory , on_delete=models.SET_NULL , null=True)
    technologies = models.ManyToManyField(Technology , related_name='projects')
    description = models.TextField()
    detailed_description = models.TextField(blank=True)
     
    
    # Visual elements
    featured_image = models.ImageField(upload_to='portfolio/projects/', null=True, blank=True)
    gradient = models.CharField(max_length=50 , choices=GRADIENT_CHOICES , default='primary', null=True, blank=True)
    
    # Project links
    live_url = models.URLField(blank=True)
    repository_url = models.URLField(blank=True)
    case_study_url = models.URLField(blank=True)

    # Project details
    client = models.CharField(max_length=200 , blank=True)
    duration = models.CharField(max_length=100 , blank=True)
    completion_date = models.DateField(null=True , blank=True)

    # Meta fields
    is_featured = models.BooleanField(default=False)
    display_order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ['-is_featured' , 'display_order' , '-created_at']

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(Project , related_name='images' , on_delete=models.CASCADE)
    image = models.ImageField(upload_to='portfolio/projects/gallery/')
    alt_text = models.CharField(max_length=200)
    display_order = models.IntegerField(default=0)
    is_primary = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Project Image"
        verbose_name_plural = "Project Images"
        ordering = ['display_order']

    def __str__(self):
        return f"{self.project.title} - {self.alt_text}"
        
class Keyfeature(models.Model):
    title = models.CharField(max_length=220, null=True, blank=True)
    service = models.ForeignKey(Project , related_name='Key_feature' , on_delete=models.CASCADE)
        
