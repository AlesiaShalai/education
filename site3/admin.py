from django.contrib import admin

from . import models


admin.site.register(models.YoutubeVideo)

admin.site.register(models.Document)

admin.site.register(models.FavouriteArticle)