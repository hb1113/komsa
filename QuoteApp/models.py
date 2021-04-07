from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class QuotePost(models.Model):

    text = models.CharField(max_length=256)
    author = moels.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return f"{ self.text }, by: {self.author}"
