from django.shortcuts import render
from .models import Template

def template_list(request):
    templates = Template.objects.all()
    return render(request, 'template_list.html', {'templates': templates})