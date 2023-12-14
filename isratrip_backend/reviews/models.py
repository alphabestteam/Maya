from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
# Create your models here.
class Review(models.Model):
    review_id = models.AutoField(primary_key=True, editable=False)
    trip_id = models.ForeignKey(to="trips.Trip", on_delete=models.CASCADE)
    user_id = models.ForeignKey(to="users.User", on_delete=models.CASCADE)
    user_rating = models.DecimalField(max_digits=3, decimal_places=2, validators=[MaxValueValidator(5), MinValueValidator(0)])
    date_published = models.DateField(default=timezone.now)
    review = models.TextField()
    is_review_approved = models.BooleanField(default=False)