from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.


class QuotePost(models.Model):

    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now,blank=True, null=True)
    likes = models.PositiveIntegerField(default=0)
    comments = models.PositiveIntegerField(default=0)
    shares = models.PositiveIntegerField(default=0)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('quote_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f"{ self.text }, by: {self.author}"


class QuoteComment(models.Model):

    text = models.TextField()
    quote = models.ForeignKey(QuotePost, on_delete=models.CASCADE, related_name='quotecomments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    likes = models.PositiveIntegerField(default=0)
    comments = models.PositiveIntegerField(default=0)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('quote_detail', kwargs={'pk': self.quote.pk})

    def __str__(self):
        return f"{ self.text }, by: {self.author}"
