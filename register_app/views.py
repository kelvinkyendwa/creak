from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    a_dict = {"insert_2":"how is this happening"}
    return render(request,'register_app/index.html',context=a_dict)
