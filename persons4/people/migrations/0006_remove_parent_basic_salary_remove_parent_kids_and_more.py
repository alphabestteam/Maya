# Generated by Django 4.2.6 on 2023-10-16 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0005_parent_basic_salary_parent_kids_parent_work_place'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parent',
            name='basic_salary',
        ),
        migrations.RemoveField(
            model_name='parent',
            name='kids',
        ),
        migrations.RemoveField(
            model_name='parent',
            name='work_place',
        ),
    ]
