from django.contrib import admin

# Register your models here.
from .models import collection, artPiece

admin.site.register(collection)
admin.site.register(artPiece)