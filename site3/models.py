from datetime import datetime
from django.db import models
from django.conf import settings


class YoutubeVideo(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField(max_length=10000)

    def __str__(self):
        return '%s - %s' % (
            self.title,
            self.link,
        )


class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')

    def __str__(self):
        return '%s' % self.docfile


class FavouriteArticle(models.Model):
    article_name = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.article_name + ' ' + self.user.username

    class Meta:
        ordering = ('date',)