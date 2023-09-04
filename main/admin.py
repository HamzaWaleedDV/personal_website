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


@admin.register(models.Facts)
class FactsAdmin(admin.ModelAdmin):
    list_per_page = 20           


@admin.register(models.Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_per_page = 20      


@admin.register(models.Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_per_page = 20


@admin.register(models.Opinion)
class OpinionAdmin(admin.ModelAdmin):
    list_per_page = 20