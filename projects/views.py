from django.shortcuts import render
from django.http import HttpResponse

from .models import Project


def projects(request):
    projects = Project.objects.all()
    context = {'projectsList': projects}
    return render(request, 'projects/projects.html', context)
    

def project(request, pk):
    project = Project.objects.get(pk=pk)
    tags = project.tags.all()
    return render(request, 'projects/single-project.html', { 'project': project, 'tags': tags })