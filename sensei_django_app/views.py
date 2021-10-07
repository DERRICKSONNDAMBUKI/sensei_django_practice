from django.shortcuts import render
from django.http import HttpResponse
from .models import Person

# Create your views here.
def index(request):
    people = Person.objects.all()
    return render(request,'index.html',{'people':people})

def counter(request):
    words = request.POST['words']
    amount_of_words = len(words.split())
    return render(request,'counter.html',{'amount':amount_of_words})

def postInput(request,i):
    return render(request,'postInput.html',{'i':i}) 