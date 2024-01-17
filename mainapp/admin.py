from django.contrib import admin
from .models import User, Coordinates, Image, Level, Pereval

admin.site.register(User)
admin.site.register(Coordinates)
admin.site.register(Image)
admin.site.register(Level)
admin.site.register(Pereval)

