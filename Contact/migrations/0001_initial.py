# Generated by Django 5.1.3 on 2024-11-13 11:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(default='Anant Soft Computing', max_length=200)),
                ('address_line1', models.CharField(max_length=200)),
                ('address_line2', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=20)),
                ('phone_primary', models.CharField(max_length=20)),
                ('phone_secondary', models.CharField(blank=True, max_length=20)),
                ('email_primary', models.EmailField(max_length=254)),
                ('email_secondary', models.EmailField(blank=True, max_length=254)),
                ('working_hours_weekday', models.CharField(default='Monday - Friday: 9:00 AM - 6:00 PM', max_length=100)),
                ('working_hours_weekend', models.CharField(default='Saturday: 9:00 AM - 2:00 PM', max_length=100)),
                ('linkedin_url', models.URLField(blank=True)),
                ('twitter_url', models.URLField(blank=True)),
                ('github_url', models.URLField(blank=True)),
                ('instagram_url', models.URLField(blank=True)),
                ('map_embed_url', models.URLField(help_text='Google Maps Embed URL')),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
            ],
            options={
                'verbose_name': 'Contact Information',
                'verbose_name_plural': 'Contact Information',
            },
        ),
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ContactEnquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('company', models.CharField(blank=True, max_length=200)),
                ('message', models.TextField()),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
                ('user_agent', models.TextField(blank=True)),
                ('referrer', models.URLField(blank=True)),
                ('status', models.CharField(choices=[('new', 'New'), ('in_progress', 'In Progress'), ('contacted', 'Contacted'), ('closed', 'Closed')], default='new', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('admin_notes', models.TextField(blank=True)),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Contact.servicetype')),
            ],
            options={
                'verbose_name': 'Contact Enquiry',
                'verbose_name_plural': 'Contact Enquiries',
                'ordering': ['-created_at'],
            },
        ),
    ]
