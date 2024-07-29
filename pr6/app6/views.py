from django.shortcuts import redirect, render
from django.http import HttpResponse

# Create your views here.
def fun(r):
    return HttpResponse("create your own website")

def page6(r):
    return render(r,"temp.html",{'a':range(5),'b':1})

import requests 
def page7(r):
    base_url="https://dummyjson.com/products"
    response=requests.get(base_url)
    data=response.json()
    return render(r,"temp1.html",{'info':data['products']})

def page8(r):
    a=['mercury','venus','earth','mars','jupyter','saturn','uranus','neptune']
    return render(r,"temp2.html",{'planets':a})

import requests 
def page9(r):
    base_url="https://rappid.in/apis/train.php?train_no={}".format("16102")
    response=requests.get(base_url)
    data=response.json()
    return render(r,"temp3.html",{'data':data,'info':data['data']})

def page10(r):
    return render(r,"temp4.html",{'b':3})

from .forms import *
def student_form(request):
    if request.method=='POST':
        form=Itemforms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=Itemforms()
    return render(request,'form.html',{'form':form})