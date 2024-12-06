from django.http import HttpResponse
from django.shortcuts import render

def sayHello(request):
 return render(request, 'index.html', {})