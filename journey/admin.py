from django.contrib import admin
from .models import Journey


@admin.register(Journey)
class JouneyPanel(admin.ModelAdmin) : 
    list_display = ['driver','from_place','to_place','start_at']