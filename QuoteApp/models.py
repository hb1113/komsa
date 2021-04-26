from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager


class QuotePost(models.Model):

    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    tag = TaggableManager()
    likes = models.ManyToManyField(User, related_name='quote_post_likes')
    shares = models.PositiveIntegerField(default=0)

    def sum_likes(self):
        return self.likes.count()

    def sum_comments(self):
        return self.quotecomments.count()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('quote_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f"{ self.text }, by: {self.author}"

    # def count_posts_of(author):
    #     return QuotePost.objects.filter(author=author).count()


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
