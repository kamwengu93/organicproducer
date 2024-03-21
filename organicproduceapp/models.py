from django.db import models

#
class Contacts(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name

class Member(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.username

class ImageModel(models.Model):
        image = models.ImageField(upload_to='images/')
        title = models.CharField(max_length=50)
        price = models.CharField(max_length=50)