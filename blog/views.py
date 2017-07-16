from django.shortcuts import render
from django.http import HttpResponse

from . import models


def index(request):
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', locals())
