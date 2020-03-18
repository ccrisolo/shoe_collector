from django.contrib import admin
from .models import Shoe, LastWorn

# Register your models here.
admin.site.register(Shoe)
admin.site.register(LastWorn)