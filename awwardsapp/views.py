# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profile.bio = 'New user profile bio'
    user.save()