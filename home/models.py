from django.db import models

# Create your models here.
class Newsletter(models.Model):
    email = models.EmailField()
    def __str__(self):
        return self.email+" added in the list."

class Contact(models.Model):
    name = models.CharField(max_length= 30)
    email= models.EmailField()
    subject = models.CharField(max_length = 100)
    message = models.TextField()

    def __str__(self):
        return "Query made by "+ self.name


class Project(models.Model):
    category = models.CharField(max_length= 50)
    client = models.CharField(max_length= 50)
    images = models.ImageField(upload_to='home/images', default='')
    date = models.DateTimeField(auto_now_add=True)
    link = models.URLField()
    title = models.CharField(max_length= 150)
    desc = models.TextField()
    tag = models.CharField(max_length= 30)
    def __str__(self):
        return self.title


class Image(models.Model):
    project = models.ForeignKey(Project, on_delete= models.CASCADE)
    image = models.ImageField(upload_to='home/images', default='')
    def __str__(self):
        return 'Some image added'
    
    