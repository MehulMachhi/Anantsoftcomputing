# careers/models.py
from django.db import models
from django.core.validators import MinValueValidator , MaxValueValidator


class Department(models.Model):
    name = models.CharField(max_length=100)  # e.g., Engineering, Design
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50 , blank=True)  # For storing FontAwesome icon names
    display_order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['display_order' , 'name']

    def __str__(self):
        return self.name


class JobLocation(models.Model):
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    is_remote = models.BooleanField(default=False)

    class Meta:
        unique_together = ['city' , 'state' , 'country']
        ordering = ['country' , 'state' , 'city']

    def __str__(self):
        location = f"{self.city}, {self.state}"
        return f"{location} (Remote)" if self.is_remote else location


class Skill(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class JobPosting(models.Model):
    JOB_TYPE_CHOICES = [
        ('full_time' , 'Full-time') ,
        ('part_time' , 'Part-time') ,
        ('contract' , 'Contract') ,
        ('internship' , 'Internship') ,
    ]

    EXPERIENCE_LEVEL_CHOICES = [
        ('entry' , 'Entry Level') ,
        ('junior' , 'Junior') ,
        ('mid' , 'Mid Level') ,
        ('senior' , 'Senior') ,
        ('lead' , 'Lead') ,
    ]

    STATUS_CHOICES = [
        ('draft' , 'Draft') ,
        ('published' , 'Published') ,
        ('filled' , 'Position Filled') ,
        ('closed' , 'Closed') ,
    ]

    # Basic Information
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    department = models.ForeignKey(Department , on_delete=models.CASCADE)
    job_type = models.CharField(max_length=20 , choices=JOB_TYPE_CHOICES)
    experience_level = models.CharField(max_length=20 , choices=EXPERIENCE_LEVEL_CHOICES)
    experience_years_min = models.PositiveIntegerField()
    experience_years_max = models.PositiveIntegerField()

    # Location and Salary
    location = models.ForeignKey(JobLocation , on_delete=models.CASCADE)
    salary_min = models.DecimalField(max_digits=12 , decimal_places=2)
    salary_max = models.DecimalField(max_digits=12 , decimal_places=2)
    salary_is_visible = models.BooleanField(default=True)

    # Job Details
    summary = models.TextField(help_text="A brief summary of the role")
    description = models.TextField(help_text="Detailed job description")
    responsibilities = models.TextField(help_text="Key responsibilities of the role")
    requirements = models.TextField(help_text="Required qualifications and skills")
    benefits = models.TextField(help_text="Job benefits and perks")

    # Skills and Requirements
    required_skills = models.ManyToManyField(Skill , related_name='required_jobs')
    preferred_skills = models.ManyToManyField(Skill , related_name='preferred_jobs' , blank=True)

    # Meta Information
    is_featured = models.BooleanField(default=False)
    is_urgent = models.BooleanField(default=False)
    status = models.CharField(max_length=20 , choices=STATUS_CHOICES , default='draft')
    applications_email = models.EmailField(help_text="Email where applications will be sent")

    # Dates and Tracking
    posting_date = models.DateField()
    closing_date = models.DateField(null=True , blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-is_featured' , '-posting_date']
        indexes = [
            models.Index(fields=['status' , 'posting_date']) ,
            models.Index(fields=['department' , 'job_type']) ,
        ]

    def __str__(self):
        return self.title

    def get_experience_range(self):
        if self.experience_years_min == self.experience_years_max:
            return f"{self.experience_years_min}+ years"
        return f"{self.experience_years_min}-{self.experience_years_max} years"

    def get_salary_range(self):
        if not self.salary_is_visible:
            return "Not Disclosed"
        return f"{self.salary_min:,.0f}-{self.salary_max:,.0f} LPA"


class EmployeeTestimonial(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    department = models.ForeignKey(Department , on_delete=models.SET_NULL , null=True)
    quote = models.TextField()
    image = models.ImageField(upload_to='careers/testimonials/')
    is_featured = models.BooleanField(default=False)
    display_order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-is_featured' , 'display_order']

    def __str__(self):
        return f"{self.name} - {self.role}"


class BenefitCategory(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50)  # For FontAwesome icons
    description = models.TextField()
    display_order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Benefit Categories"
        ordering = ['display_order']

    def __str__(self):
        return self.name
        
class JobApplication(models.Model):
    job_posting = models.ForeignKey(  
        JobPosting, 
        on_delete=models.CASCADE, 
        related_name="applications"  
    )
    name = models.CharField(max_length=200)
    phone = models.IntegerField()
    email = models.EmailField()
    address = models.TextField(null=True, blank=True)
    years_of_experience = models.CharField(max_length=200)
    resume = models.FileField()
    
    