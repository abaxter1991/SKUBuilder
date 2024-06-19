from django.contrib import admin

from .models import FaireAPI, FaireAPIEndpoints

admin.site.register(FaireAPI)
admin.site.register(FaireAPIEndpoints)
