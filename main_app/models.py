from django.db import models
from django.urls import reverse


ACTIVITIES = (
    ('C', 'Casual'),
    ('G', 'Gym'),
    ('S', 'Sport'),
)
# Create your models here.
class Shoe(models.Model):
    model = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return self.model

    def get_absolute_url(self):
        return reverse('detail', kwargs={'shoe_id': self.id})


class LastWorn(models.Model):
    date = models.DateField('date last worn')
    activity = models.CharField(
        max_length=1,
        choices=ACTIVITIES,
        default=ACTIVITIES[0][0]
      )
    #create shoe_id FK
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_activity_display()} on {self.date}"