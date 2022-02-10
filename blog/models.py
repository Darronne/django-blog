from django.conf import settings
from django.db import models
from django.utils import timezone

class Region(models.Model):
    title = models.CharField(max_length=40)
    url = models.CharField(max_length=200, default='')

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class Partition(models.Model):
    title = models.CharField(max_length=40)
    url = models.CharField(max_length=200, default='')

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    partition = models.ForeignKey(Partition, default=0, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, default=0, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    description = models.CharField(max_length=200, default='')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    url = models.CharField(max_length=200, default='')
    img = models.ImageField(upload_to='img/')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

