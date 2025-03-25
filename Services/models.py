# services/models.py
from django.db import models


class ServiceCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Service Category"
        verbose_name_plural = "Service Categories"
        ordering = ['name']

    def __str__(self):
        return self.name


class Service(models.Model):
    GRADIENT_CHOICES = [
        ('primary' , 'From Primary 400 to Primary 600') ,
        ('secondary' , 'From Secondary 400 to Secondary 600') ,
        ('accent' , 'From Accent 400 to Accent 600') ,
    ]

    ICON_CHOICES = [
        ('FaSearch' , 'Search Icon') ,
        ('FaDesktop' , 'Desktop Icon') ,
        ('FaMobile' , 'Mobile Icon') ,
        ('FaDatabase' , 'Database Icon') ,
        ('FaCode' , 'Code Icon') ,
        ('FaChartLine' , 'Chart Line Icon') ,
    ]

    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    icon = models.CharField(max_length=50 , choices=ICON_CHOICES, null=True, blank=True)
    gradient = models.CharField(max_length=50 , choices=GRADIENT_CHOICES, null=True, blank=True)
    category = models.ForeignKey(ServiceCategory , on_delete=models.SET_NULL , null=True)

    # Detailed service information
    detailed_description = models.TextField(blank=True)
    features = models.TextField(blank=True , help_text="List the key features of this service")
    benefits = models.TextField(blank=True , help_text="List the benefits of this service")

    # Meta information
    is_active = models.BooleanField(default=True)
    display_order = models.IntegerField(default=0, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ['display_order' , 'title']

    def __str__(self):
        return self.title


class ServiceFeature(models.Model):
    service = models.ForeignKey(Service , related_name='feature_list' , on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=50 , blank=True)
    display_order = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Service Feature"
        verbose_name_plural = "Service Features"
        ordering = ['display_order']

    def __str__(self):
        return f"{self.service.title} - {self.title}"


class ServiceImage(models.Model):
    service = models.ForeignKey(Service , related_name='images' , on_delete=models.CASCADE)
    image = models.ImageField(upload_to='services/')
    alt_text = models.CharField(max_length=200)
    display_order = models.IntegerField(default=0)
    is_primary = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Service Image"
        verbose_name_plural = "Service Images"
        ordering = ['display_order']

    def __str__(self):
        return f"{self.service.title} - {self.alt_text}"