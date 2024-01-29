from django.shortcuts import render
from django.http import HttpResponse
from .models import Projects

# projects_list = [
#     {
#         'id': '1',
#         'title': 'Ecommerce Website',
#         'description': 'Fully functional ecomm website',
#     },
#     {
#         'id':'2',
#         'title': 'Portfolio website',
#         'description': 'Built a portfolio website',
#     },
#     {
#         'id': '3',
#         'title': 'Social Network',
#         'description': 'Built a social network',
#     }
# ]

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