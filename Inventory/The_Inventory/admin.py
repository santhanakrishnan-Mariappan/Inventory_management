from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Laptop, DeskTop, Mobile)
class ViewAdmin(admin.ModelAdmin):
    pass