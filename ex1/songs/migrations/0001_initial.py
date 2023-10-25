# Generated by Django 4.2.6 on 2023-10-23 11:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('song_name', models.TextField(max_length=100)),
                ('song_id', models.IntegerField(primary_key=True, serialize=False, verbose_name=django.core.validators.MinValueValidator(0))),
                ('released_date', models.DateField()),
                ('singer_name', models.TextField(max_length=100)),
            ],
        ),
    ]
