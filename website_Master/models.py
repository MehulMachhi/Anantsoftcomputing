# master/models.py
from django.db import models


class ProjectTechstack(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    icon = models.ImageField(upload_to='techstack_icons/' , blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Project Tech Stack"
        verbose_name_plural = "Project Tech Stacks"
        ordering = ['name']

    def __str__(self):
        return self.name


class ProjectKeyFeature(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Project Key Feature"
        verbose_name_plural = "Project Key Features"
        ordering = ['name']

    def __str__(self):
        return self.name


class PortfolioCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Portfolio Category"
        verbose_name_plural = "Portfolio Categories"
        ordering = ['name']

    def __str__(self):
        return self.name


class ProjectImpact(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    metrics = models.TextField(blank=True , help_text="Enter quantifiable metrics or KPIs")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Project Impact"
        verbose_name_plural = "Project Impacts"
        ordering = ['title']

    def __str__(self):
        return self.title