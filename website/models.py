# website/models.py
from django.db import models
from website_Master.models import ProjectTechstack, ProjectKeyFeature, PortfolioCategory, ProjectImpact

class Testimonials(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100, null=True, blank=True)
    Company_Name = models.CharField(max_length=100, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='testimonials', null=True, blank=True)

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    Portfolio_category = models.ForeignKey(PortfolioCategory, on_delete=models.CASCADE)
    Project_title = models.CharField(max_length=100)
    Project_Techstack = models.ManyToManyField(ProjectTechstack)
    Project_KeyFeatures = models.ManyToManyField(ProjectKeyFeature)
    Project_Impact = models.ForeignKey(ProjectImpact, on_delete=models.CASCADE)
    Project_live_link = models.CharField(max_length=100)
    Project_Repos_link = models.CharField(max_length=100)
    Project_case_study_link = models.CharField(max_length=100)
    Project_description = models.TextField()
    Project_image = models.ImageField(upload_to='portfolio')

    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolios'

    def __str__(self):
        return self.Project_title

class Aboutus(models.Model):
    Mission = models.TextField()
    Vision = models.TextField()
    aboutus_title = models.CharField(max_length=100)
    Core_values = models.TextField()

    class Meta:
        verbose_name = 'About Us'
        verbose_name_plural = 'About Us'

    def __str__(self):
        return self.aboutus_title