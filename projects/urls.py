from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.projects, name='project'),
    path('project/<str:pk>/', views.project, name='projects')
]