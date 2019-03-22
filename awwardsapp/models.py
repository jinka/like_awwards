from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime as dt
from django.utils import timezone
from django.urls import reverse
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    bio = models.TextField(max_length=100, blank=True)
    contact = models.TextField(max_length=100, blank=True)
    # votes = models.IntegerField(default = 0)


    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, **kwargs):
        super().save()

    @classmethod
    def filter_by_id(cls, id):
        details = Profile.objects.filter(user = id).first()
        return details

class Project(models.Model):
    image = models.ImageField(upload_to = 'images/')
    title = models.CharField(max_length =100)
    url = models.CharField(max_length =80)
    detail_desciption=models.TextField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project-detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-pk']
 
    def save_project(self):
        self.save()

    @classmethod
    def search_by_projectname(cls,idea):
        projects = cls.objects.filter(title__icontains=idea)
        return projects
        
class Rate(models.Model):
    pass
    # design = models.IntegerField()
    # usability = models.IntegerField()
    # creativity = models.IntegerField()

    # def __str__(self):
    #     return self.design

    # class Meta:
    #     ordering = ['-id']

    # def save_rate(self):
    #     self.save()

    # @classmethod
    # def get_rate(cls, profile):
    #     rate = Rate.objects.filter(Profile__pk = profile)
    #     return rate
    
    # @classmethod
    # def get_all_rating(cls):
    #     rating = Rate.objects.all()
    #     return rating