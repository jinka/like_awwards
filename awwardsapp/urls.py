from django.urls import path
# from .views import ImageListView, ImageDetailView, ImageCreateView,ImageUpdateView
from . import views

urlpatterns = [
    path('upload/', views.new_project, name='new_project'),
]
