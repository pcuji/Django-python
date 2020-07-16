
from django.shortcuts import render,redirect
from .models import Article
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required



# Create your views here.
def article_list(request):
    article = Article.objects.all().order_by('date')
    paginator = Paginator(article , 3)
    page = request.GET.get('page')
    article = paginator.get_page(page)
    return render(request,'articles/article_list.html', {'articles': article})



def article_detail(request,slug):
    #the brakets in the below lines is for a dictionary
    article = Article.objects.get(slug=slug)
    return render(request,'articles/article_detail.html', {'article':article})
# by the 'article': article we have access to the article and what will be displya in the webaplication
    return HttpResponse(slug)
