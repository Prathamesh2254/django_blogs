from django.db import models

# Create your models here.

class about_us(models.Model):
    About_us = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.About_us
    

class social(models.Model):
    social_name = models.CharField(max_length=200)
    social_link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.social_name