from django.shortcuts import render
from .models import Personal, Skills, Projects, Logo, CV, Url

# Create your views here.

def index(request):
    personal = Personal.objects.last()
    logo = Logo.objects.last()
    cv = CV.objects.last()
    url = Url.objects.all()
    skills = Skills.objects.all()
    projects = Projects.objects.all()

    return render(
        request,
        'index.html',
        {
            'personal' : personal,
            'logo': logo,
            'cv': cv,
            'urls': url,
            'skills': skills,
            'projects': projects
        }
    )