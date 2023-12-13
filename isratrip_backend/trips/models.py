from django.db import models

# Create your models here.
WEATHER_OPTIONS = (
    ('summer', 'summer'),
    ('winter', 'winter'),
    ('spring', 'spring'),
    ('autumn', 'autumn'),
)
class Trip(models.Model):
    trip_id = models.AutoField(primary_key=True, editable=False)
    location_id = models.ForeignKey(to='locations.Location', on_delete=models.CASCADE)
    categories =  models.ManyToManyField(to='categories.Category', related_name='categories', blank=True)
    trip_title = models.CharField(max_length=100)
    user_id = models.ForeignKey(to="users.User", on_delete=models.CASCADE)
    trip_rating = models.DecimalField(max_digits=3, decimal_places=2)
    # review_id = models.ForeignKey(to="reviews.Review", on_delete=models.CASCADE)
    age_limit = models.IntegerField()
    best_weather = models.TextField(choices=WEATHER_OPTIONS)
    is_open = models.BooleanField(default=False)

