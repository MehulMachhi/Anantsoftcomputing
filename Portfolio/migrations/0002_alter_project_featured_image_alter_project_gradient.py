# Generated by Django 4.2.16 on 2024-11-18 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, null=True, upload_to='portfolio/projects/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='gradient',
            field=models.CharField(blank=True, choices=[('primary', 'From Primary 400 to Primary 600'), ('secondary', 'From Secondary 400 to Secondary 600'), ('accent', 'From Accent 400 to Accent 600')], default='primary', max_length=50, null=True),
        ),
    ]
