from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .forms import ProjectForm, ProfileUpdateForm

from .models import Project
# from decouple import config
from django.core.mail import send_mail
from django.conf import settings

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  Profile, Project
from .serializer import ProfileSerializer, ProjectSerializer


def email(request):
    pass
    return redirect('redirect to a new page')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')

            subject = 'Thank you for registering to our site'
            message = ' it  means a world to us '
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['daudishuuti@gmail.com',settings.EMAIL_HOST_USER]

            send_mail( subject, message, email_from, recipient_list )

            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


@login_required
def profile(request):

    current_user = request.user
    # images = Image.objects.filter(user = current_user)

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        # 'images': images
    }

    return render(request, 'profile.html', context)


def new_project(request):
    current_user = request.user
    project = Project.objects.filter(user = current_user)

    if request.method == 'POST':
        uploadform = ProjectForm(request.POST, request.FILES,instance=request.user)
        if uploadform.is_valid():
            upload = uploadform.save(commit=False)
            upload.profile = request.user.profile
            upload.save()
            return redirect('home')
    else:
        uploadform = ProjectForm()
    return render(request,'update-project.html',locals())

class ProfileList(APIView):
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)
class ProjectList(APIView):
    def get(self, request, format=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)