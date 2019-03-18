from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime as dt

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    bio = models.TextField(max_length=100, blank=True)
    contact = models.TextField(max_length=100, blank=True)


    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self,**kwargs):
        super().save()

    @classmethod
    def filter_by_id(cls, id):
        details = Profile.objects.filter(user = id).first()
        return details

class Project(models.Model):
    image = models.ImageField(upload_to = 'images/')
    title = models.CharField(max_length =20)
    url = models.CharField(max_length =50)
    detail_desciption=models.TextField(max_length=500)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(User, related_name='posted_by', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-pk']
 
    def save_project(self):
        self.save()

class Rate(models.Model):
    design = models.CharField(max_length=30)
    usability = models.CharField(max_length=8)
    creativity = models.CharField(max_length=8,blank=True,null=True)


    def __str__(self):
        return self.design

    class Meta:
        ordering = ['-id']

    def save_rate(self):
        self.save()

    @classmethod
    def get_rate(cls, profile):
        rate = Rate.objects.filter(Profile__pk = profile)
        return rate
    
    @classmethod
    def get_all_rating(cls):
        rating = Rate.objects.all()
        return rating