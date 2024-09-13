from django.db import models

# Create your models here.

class AboutUs(models.Model):
    description = models.TextField()

    def __str__(self):
        return "About Us"

class ResourceLink(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to="icons/", blank=True, null=True)
    url = models.URLField()

    def __str__(self):
        return self.name

class Store(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    map_url = models.URLField()
    
    def __str__(self):
        return self.name
