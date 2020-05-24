from django.shortcuts import render
from django.http import HttpResponse
import feedparser
import ssl

def index(request):
    if hasattr(ssl, '_create_unverified_context'):
        ssl._create_default_https_context = ssl._create_unverified_context
    if request.GET.get("url"):
        print("url:", request.GET.get("url"))
        url = request.GET["url"] #Getting URL
        result = feedparser.parse(url) #Parsing XML data
        #print(feed)
        
    else:
        result = None
        print('else')

    return render(request, "reader.html", {
        "result" : result,
    })