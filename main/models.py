from django.db import models

# Create your models here.

class Media(models.Model):
    logo = models.ImageField()
    cv = models.FileField(null=True)
    urls = models.URLField()


class Skills(models.Model):
    my_skills = models.CharField(max_length=50)


class Projects(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    url = models.URLField()
    image_for_project = models.ImageField()