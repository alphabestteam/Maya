from django.db import models
from reviews.models import Review
from django.db.models import Avg
# Create your models here.
WEATHER_OPTIONS = (
    ('summer', 'summer'),
    ('winter', 'winter'),
    ('spring', 'spring'),
    ('autumn', 'autumn'),
)
class Trip(models.Model):
    trip_id = models.AutoField(primary_key=True, editable=False)
    location = models.ForeignKey(to='locations.Location', on_delete=models.CASCADE)
    categories =  models.ManyToManyField(to='categories.Category', related_name='categories', blank=True)
    trip_title = models.CharField(max_length=100)
    trip_description = models.TextField()
    user_id = models.ForeignKey(to="users.User", on_delete=models.CASCADE)
    age_limit = models.IntegerField()
    best_weather = models.TextField(choices=WEATHER_OPTIONS)
    is_open = models.BooleanField(default=False)

    @property
    def trip_rating(self):
        avg_rating = Review.objects.filter(is_approved_review=True, trip_id=self.trip_id).annotate(Avg('user_rating'))
        return avg_rating['user_rating__avg'] if avg_rating['user_rating__avg'] else 0.0

class RequestedTrip(Trip):
    admin_approved = models.BooleanField(default=False)
