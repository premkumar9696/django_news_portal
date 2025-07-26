from django.shortcuts import render
import requests
# Create your views here.
def home(request):
    category=[
        'technology',
        'sports', 
        'entertainment',
        'health',
        'business',          
        'general',
    ]
    dict={'category': category}
    return render(request, 'home.html',context=dict)

def news_category(request, category):
    url=f"https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey=77fc3776f2674fc685688843e336269e"
    response= requests.get(url)
    data=response.json()
    articles=data.get('articles',[]) if data.get('status')=='ok' else []
    dict={'articles': articles, 'category': category}
    return render(request, 'news_category.html', context=dict)