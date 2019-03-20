# my_project/urls.py
from django.contrib import admin
from django.contrib.auth import views as auth_views
# from .views import new_project
# from . import views
from django.urls import path, include
from awwardsapp import views
from awwardsapp import views as user_views
from django.views.generic.base import TemplateView 
import urllib.request

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    # path('newproject/', new_project.as_view(), name='newproject'),
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('', include('awwardsapp.urls')),

]
# if settings.DEBUG:
#     urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
