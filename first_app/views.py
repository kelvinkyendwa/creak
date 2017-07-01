from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    my_dict = {'insert_me':"Hello nigga  I am from views.py"}
    return render(request,'first_app/index.html',context=my_dict)
def movies(request):
    my_movie = {'insert_mes':"Here is where the movies Reviews will be"}
    return render(request,'first_app/movies.html',context=my_movie)
def series(request):
    my_series = {'series_list':"Here is where the series Reviews will be"}
    return render(request,'first_app/series.html',context=my_series)
