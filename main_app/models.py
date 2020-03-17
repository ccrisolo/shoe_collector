from django.db import models

# Create your models here.
class Shoe(models.Model):
    model = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return self.model