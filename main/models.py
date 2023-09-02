from django.db import models

# Create your models here.


class Personal(models.Model):
    name = models.CharField(max_length=30)
    career = models.CharField(max_length=80)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Logo(models.Model):
    title = models.CharField(max_length=30, default="My Logo")
    logo = models.ImageField()

    def __str__(self):
        return self.title

class CV(models.Model):  
    title = models.CharField(max_length=30, default="My CV")
    cv = models.FileField()

    def __str__(self):
        return self.title

class Url(models.Model):
    title = models.CharField(max_length=30, default="My Urls")
    url = models.URLField()

    def __str__(self):
        return self.title


class Skills(models.Model):
    my_skills = models.CharField(max_length=50)


class Projects(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    url = models.URLField()
    image_for_project = models.ImageField()

    def __str__(self):
        return self.title