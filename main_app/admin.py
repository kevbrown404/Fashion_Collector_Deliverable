from django.contrib import admin
from .models import Brand, Collection, Favorites # import the Brand and Collection model from models.py
# Register your models here.

admin.site.register(Brand) # this line will add the model to the admin panel
admin.site.register(Collection)
admin.site.register(Favorites)