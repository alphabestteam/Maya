from django.db import models

# Create your models here.
class Category(models.Model):
    category_id = models.AutoField(primary_key=True, editable=False)
    category_name = models.CharField(max_length=100)