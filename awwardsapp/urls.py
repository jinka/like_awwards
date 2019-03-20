from django.urls import path
# from .views import ImageListView, ImageDetailView, ImageCreateView,ImageUpdateView
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('api/profiles/', views.ProfileList.as_view()),
    path('api/projects/', views.ProjectList.as_view()),
]
