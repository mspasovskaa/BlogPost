from django.contrib.auth.models import User
from django.db import models

# Create your models here.





class Author(models.Model):
    first_name = models.CharField(max_length=30,null=True, blank=True)
    last_name = models.CharField(max_length=30,null=True, blank=True)
    country = models.CharField(max_length=30,null=True, blank=True)
    image = models.ImageField(upload_to='cover_images/',null=True, blank=True)
    interests=models.TextField(null=True,blank=True)
    skills=models.TextField(null=True,blank=True)
    profession=models.TextField(null=True,blank=True)

    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.first_name+" "+self.last_name

class Block(models.Model):
    bloking_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE,related_name='blocking_user')
    bloked_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE,related_name='bloked_user')
    def __str__(self):
        return self.bloking_user.first_name + self.bloked_user.first_name



class Post(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(Author, null=True, blank=True, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    file = models.FileField(null=True, blank=True)
    dateCreated = models.DateField(null=True, blank=False)
    dateLastChange = models.DateField(null=True, blank=False)
    def __str__(self):
        return self.title+" "+self.author.first_name + " "+ self.author.last_name



class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.content