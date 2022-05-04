from django.db import models
from django.urls import reverse

# Create your models here.

class User(models.Model):
    user = models.CharField(max_length=30)
    password = models.CharField(max_length=20)

    class Meta:
        verbose_name_plural = 'Uzivatel'

    def __str__(self):
        return f'{self.user}'

class Posts(models.Model):
    userId = models.IntegerField()
    title = models.CharField(max_length=50)
    body = models.TextField()
    
    class Meta:
        verbose_name_plural = 'Posts'

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse("home")