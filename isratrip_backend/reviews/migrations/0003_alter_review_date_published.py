# Generated by Django 4.2.6 on 2023-12-13 12:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_alter_review_date_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date_published',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
