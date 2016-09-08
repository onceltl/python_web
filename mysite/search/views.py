#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
def index(request):
	return render(request,'home.html')
def search(request):
	info = request.GET['input']
	return render(request,'display.html',{'string':info})
# Create your views here.
