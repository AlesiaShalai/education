from django.shortcuts import render, redirect

from . import models
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from site3.models import Document, FavouriteArticle
from site3.forms import DocumentForm

def tasks(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()
            return HttpResponseRedirect(reverse('tasks'))
    else:
        form = DocumentForm()

    documents = Document.objects.all()

    return render_to_response(
        'tasks.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )


def mainpage(request):
    return render(request, 'mainpage.html')

def material1(request):
    favourite_articles = FavouriteArticle.objects.filter(user=request.user, article_name='material1')
    return render(request, 'materials/material1.html', {'is_favourite': bool(favourite_articles)})

def material2(request):
    favourite_articles = FavouriteArticle.objects.filter(user=request.user, article_name='material2')
    return render(request, 'materials/material2.html', {'is_favourite': bool(favourite_articles)})

def material3(request):
    favourite_articles = FavouriteArticle.objects.filter(user=request.user, article_name='material3')
    return render(request, 'materials/material3.html', {'is_favourite': bool(favourite_articles)})

def material4(request):
    favourite_articles = FavouriteArticle.objects.filter(user=request.user, article_name='material4')
    return render(request, 'materials/material4.html', {'is_favourite': bool(favourite_articles)})

def material5(request):
    favourite_articles = FavouriteArticle.objects.filter(user=request.user, article_name='material5')
    return render(request, 'materials/material5.html', {'is_favourite': bool(favourite_articles)})

def materials(request):
    videos = models.YoutubeVideo.objects.all()
    return render(request, 'materials.html', {"videos": videos})

def tests(request):
    return render(request, 'tests.html')

def links(request):
    return render(request, 'links.html')

def favourites(request):
    favourite_pages = FavouriteArticle.objects.filter(user=request.user)
    return render(request, 'favourites.html', {"favourite_pages": favourite_pages})

def create_favourite(request, pagename):
    favourite_page = FavouriteArticle(article_name=pagename, user=request.user)
    favourite_page.save()
    return redirect('/materials/' + pagename + '.html')

def delete_favourite(request, pagename):
    FavouriteArticle.objects.filter(user=request.user, article_name=pagename).delete()
    return redirect('/materials/' + pagename + '.html')