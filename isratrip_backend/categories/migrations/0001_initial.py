# Generated by Django 4.2.6 on 2023-12-13 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=100)),
            ],
        ),
    ]
