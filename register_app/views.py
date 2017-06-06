from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    a_dict = {"insert_2":"how is this happening"}
    return render(request,'register_app/index.html',context=a_dict)
# def help(request):
#     dict_2 = {"help_text":"Help is on the way"}
#     return render(request,"register_app/help",context=dict_2)


def help(request):
    helpdict = {'help_insert':'HELP PAGE'}
    return render(request,'register_app/help.html',context=helpdict)

def register(request):
    a_dict = {"insert_2":"how is this happening"}
    return render(request,'register_app/register.html',context=a_dict)
