from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Topic(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name
class Rooms(models.Model):
    host=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # image_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    topic=models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name=models.CharField(max_length=150)
    descriptions=models.TextField(max_length=5000 ,null=True, blank=True)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering=['-updated', 'created']

class Messeag(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    room=models.ForeignKey(Rooms,related_name='message' ,on_delete=models.CASCADE)
    body=models.TextField()
    update=models.DateTimeField(auto_now_add=True)
    created=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body[0:50]
    class Meta:
        ordering=['-update', 'created']
# class Comment(models.Model):
#     name=models.ForeignKey(User, on_delete=models.CASCADE)
#     room.
