from django.urls import path
from .views import ProjectDetailView, ProjectListView, ProjectCreateView, ProjectUpdateView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('project/new/', ProjectCreateView.as_view(), name='project-create'),
    path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name='project-update'),
    path('api/profiles/', views.ProfileList.as_view()),
    path('api/projects/', views.ProjectList.as_view()),
]
