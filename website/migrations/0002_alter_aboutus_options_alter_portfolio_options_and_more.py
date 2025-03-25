# Generated by Django 5.1.3 on 2024-11-13 10:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
        ('website_Master', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutus',
            options={'verbose_name': 'About Us', 'verbose_name_plural': 'About Us'},
        ),
        migrations.AlterModelOptions(
            name='portfolio',
            options={'verbose_name': 'Portfolio', 'verbose_name_plural': 'Portfolios'},
        ),
        migrations.AlterModelOptions(
            name='testimonials',
            options={'verbose_name': 'Testimonial', 'verbose_name_plural': 'Testimonials'},
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='Portfolio_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website_Master.portfoliocategory'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='Project_Impact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website_Master.projectimpact'),
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='Project_KeyFeatures',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='Project_Techstack',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='Project_KeyFeatures',
            field=models.ManyToManyField(to='website_Master.projectkeyfeature'),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='Project_Techstack',
            field=models.ManyToManyField(to='website_Master.projecttechstack'),
        ),
    ]
