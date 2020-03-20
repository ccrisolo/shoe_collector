from django.contrib import admin
from .models import Shoe, LastWorn, Store, Photo

# Register your models here.
admin.site.register(Shoe)
admin.site.register(LastWorn)
admin.site.register(Store)
admin.site.register(Photo)