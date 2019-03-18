from django.urls import path
# from .views import ImageListView, ImageDetailView, ImageCreateView,ImageUpdateView
from . import views

urlpatterns = [
    path('upload/', views.upload_project, name='upload_project'),
]
