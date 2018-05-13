from django.shortcuts import render
from .models import Article,Author
from django.http import HttpResponse
# Create your views here.
def welcome(request):
    return HttpResponse("You've start the server successfully!")

def index(request):
    autlist=Author.objects.all()
    return render(request,'index.html',{"autlist":autlist})
    # return render(request,'index.html')

def arc(request,num):
    au=Author(pk=num)
    arclist=au.article_set.all()
    return render(request,'arcticle.html',{"arclist":arclist})

def content(request,num):
    arc=Article.objects.get(pk=num)
    arclist=[arc]
    aut=Author.objects.get(pk=arc.writer_id)
    # print(aut)
    return render(request,'content.html',{"arclist":arclist,"aut":aut})