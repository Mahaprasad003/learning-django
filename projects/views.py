from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Projects
from .forms import ProjectsForm



# Create your views here.
def projects(request):
    projects = Projects.objects.all()
    context = {
        'projects' : projects
    }
    return render(request, 'projects/projects.html', context)

def project(request,pk):
    projectObj = Projects.objects.get(id=pk)
    tag = projectObj.tags.all()
    
    context = {
        'project' : projectObj,
        'tags' : tag
    }
    return render(request, 'projects/single-project.html',context)

def createProject(request):
    form = ProjectsForm()
    context = {'forms': form}

    if request.method == 'POST':
        form = ProjectsForm(request.POST)
        if form.is_valid():
            form.save()
            return(redirect('projects'))
    return render(request, 'projects/project_form.html', context)

def updateProject(request,pk):
    project = Projects.objects.get(id=pk)
    form = ProjectsForm(instance=project)
    context = {'forms': form}

    if request.method == 'POST':
        form = ProjectsForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return(redirect('projects'))
    return render(request, 'projects/project_form.html', context)

def deleteProject(request,pk):
    project = Projects.objects.get(id=pk)
    # form = ProjectsForm(instance=project)
    # context = {'forms': form}

    if request.method == 'POST':
    #     form = ProjectsForm(request.POST, instance=project)
        project.delete()
        return(redirect('projects'))
    context={'object' : project}
    return render(request, 'projects/delete_template.html', context)