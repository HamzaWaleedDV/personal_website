from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Personal)
class PersonalAdmin(admin.ModelAdmin):
    list_per_page = 20


@admin.register(models.CV)
class CVAdmin(admin.ModelAdmin):
    list_per_page = 20


@admin.register(models.Logo)
class LogoAdmin(admin.ModelAdmin):
    list_per_page = 20


@admin.register(models.Url)
class UrlAdmin(admin.ModelAdmin):
    list_per_page = 20        