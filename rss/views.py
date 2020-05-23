from django.shortcuts import render
from django.http import HttpResponse
import feedparser
import ssl

def index(request):
    if hasattr(ssl, '_create_unverified_context'):
        ssl._create_default_https_context = ssl._create_unverified_context
    if request.GET.get("url"):
        url = request.GET["url"] #Getting URL
        feed = feedparser.parse(url) #Parsing XML data
        print(len(feed))
    else:
        feed = None
        print('else')

    return render(request, "rss/reader.html", {
        "feed" : feed,

    })