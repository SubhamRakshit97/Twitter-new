from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Tweet
from .forms import TweetForm

# Create your views here.

def index(request):
    if request.method =='POST':
        form = TweetForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('form.erros.as_json()')




    tweets = Tweet.objects.all()[:20]


    return render(request, "tweet.html",
                {'tweets':tweets})


def delete(request, tweet_id):
    tweet =  Tweet.objects.get( id = tweet_id)
    tweet.delete()
    return HttpResponseRedirect("/")


def edit(request, tweet_id):
    tweet =  Tweet.objects.get( id = tweet_id)
    if request.method =='POST':
        form = TweetForm(request.POST,request.FILES, instance = tweet)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('form.erros.as_json()')

    #tweet.edit()
    return render(request, "edit.html" , {"tweet":tweet})


def like(request, tweet_id):
    tweet= Tweet.objects.get( id=tweet_id)
    tweet.like += 1
    tweet.save()
    return HttpResponseRedirect("/")
def unlike(request, tweet_id):
    tweet= Tweet.objects.get( id=tweet_id)
    tweet.like -= 1
    tweet.save()
    return HttpResponseRedirect("/")

