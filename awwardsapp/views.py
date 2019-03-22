from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import ProjectForm, ProfileUpdateForm
from django.views.generic import ListView, CreateView, DetailView,UpdateView 

from .models import Project
# from decouple import config
from django.core.mail import send_mail
from django.conf import settings

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  Profile, Project
from .serializer import ProfileSerializer, ProjectSerializer



def search_project(request):

    if 'search-project' in request.GET and request.GET["search-project"]:
        find = request.GET.get("search-project")
        searched_projects = Project.search_by_projectname(find)
        message = f"{find}"

        return render(request,'search.html',{'message':message,'projects':searched_projects})

    else:
        message ="You have not searched for any project"
        return render(request,'search.html',{'message':message,})


def home(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'home.html', context)

class ProjectListView(DetailView):
    model = Project
    template_name = 'home.html'
    context_object_name = "projects"
    ordering = ['-created_date']

class ProjectDetailView(DetailView):
    model = Project

class ProjectCreateView(LoginRequiredMixin,CreateView):
    model = Project
    fields = ['image','title','url','detail_desciption']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProjectUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Project
    fields = ['image','title','url','detail_desciption']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        project = self.get_object()
        if self.request.user == project.user:
            return True
        return False


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
    projects = Project.objects.filter(user = current_user)

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
         'projects': projects
    }

    return render(request, 'profile.html', context)

class new_project(LoginRequiredMixin,CreateView):
    model = Project
    fields = ['image','title','url','detail_desciption',]
    # current_user = request.user
    
    def form_valid(self, form):
        # form.instance.user = Image.objects.get(user=self.request.user)
        form.instance.user = self.request.user
        form.instance.name = self.request.user
        return super().form_valid(form)

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


def vote(request,project_id):
    pass


