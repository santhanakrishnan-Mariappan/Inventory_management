from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('Index', Index, name="Index_page"),
    path('display_Laptops', display_Laptops, name="display_Laptops"),
    path('display_Desktops', display_Desktops, name="display_Desktops"),
    path('display_Mobiles', display_Mobiles, name="display_Mobiles"),
    path('add_laptop', add_laptop, name="add_laptop"),
    path('add_Desktop', add_Desktop, name="add_Desktop"),
    path('add_Mobile', add_Mobile, name="add_Mobile"),
    path('edit_Laptop/<pk>', edit_Laptop, name="edit_Laptop"),
    path('edit_Desktop/<pk>', edit_Desktop, name="edit_Desktop"),
    path('edit_Mobile/<pk>', edit_Mobile, name="edit_Mobile"),
    path('delete_Laptop/<pk>', delete_Laptop, name="delete_Laptop"),
    path('delete_Desktop/<pk>', delete_Desktop, name="delete_Desktop"),
    path('delete_Mobile/<pk>', delete_Mobile, name="delete_Mobile"),

]
