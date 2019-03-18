from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime as dt

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    bio = models.TextField(max_length=500, blank=True)
    rate = models.ManyToManyField('Project', related_name='image',max_length=30)
    contact = models.TextField(max_length=500, blank=True)


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
    title = models.CharField(max_length =10)
    url = models.CharField(max_length =50)
    detail_desciption=models.TextField(max_length=500)
    profile = models.ForeignKey(Profile, null = True,related_name='project')
    pub_date = models.DateTimeField(auto_now_add=True, null=True)
    user= models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-pk']
 
    def save_project(self):
        self.save()

class Rate(models.Model):
    pass