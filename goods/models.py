from django.db import models
from time import strftime
from django.contrib.auth.models import User


class Media(models.Model):
    name = models.CharField(max_length=100, unique=False, null=False)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=False, null=False)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=100, unique=False, null=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, unique=False, null=False)
    weight = models.DecimalField(decimal_places=2, max_digits=10, null=False, default=0.0)
    height = models.DecimalField(decimal_places=2, max_digits=10, null=False, default=0.0)
    photo = models.FileField(null=False, upload_to='upload/')
    buy_url = models.URLField(max_length=300, unique=False, null=False)
    description = models.TextField(max_length=1024, unique=False, null=False)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)

    published = models.DateTimeField(null=False,  default=strftime('%Y-%m-%d %H:%M:%S'))

    def __str__(self):
        return f'{self.name} / {self.genre} / {self.status}'
