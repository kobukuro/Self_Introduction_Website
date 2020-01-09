from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_page(request):
    return render(request,'home_page.html',{})
    #return HttpResponse('<h1>1</h1>')