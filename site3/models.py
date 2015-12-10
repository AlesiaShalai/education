from django.db import models


class YoutubeVideo(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField(max_length=10000)

    def __str__(self):
        return '%s - %s' % (
            self.title,
            self.link,
        )
