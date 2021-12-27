from django.contrib import admin

# Register your models here.
from .models import localisation, police_centrale, user, alerte
admin.site.register(localisation)
admin.site.register(police_centrale)
admin.site.register(user)
admin.site.register(alerte)