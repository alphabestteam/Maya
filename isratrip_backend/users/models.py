from django.db import models
# Create your models here.
ROLE_OPTIONS = (
    ('user', 'user'),
    ('admin', 'admin'),
)
class User(models.Model):
    user_id = models.AutoField(primary_key=True, editable=False)
    first_name = models.TextField(max_length=100)
    last_name = models.TextField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    city = models.TextField()
    date_of_birth = models.DateField()
    role = models.TextField(choices=ROLE_OPTIONS, default=ROLE_OPTIONS[0][0])

