from django.shortcuts import render
from .models import Personal, Skills, Projects, Logo, CV, Url, Facts, Opinion
from django.core.mail import send_mail

# Create your views here.

def index(request):
    personal = Personal.objects.last()
    logo = Logo.objects.last()
    cv = CV.objects.last()
    url = Url.objects.all()
    skills = Skills.objects.all()
    projects = Projects.objects.all()
    facts = Facts.objects.all()
    opinions = Opinion.objects.all()

    return render(
        request,
        'index.html',
        {
            'personal' : personal,
            'logo': logo,
            'cv': cv,
            'urls': url,
            'skills': skills,
            'projects': projects,
            'facts': facts,
            'opinions': opinions,
        }
    )