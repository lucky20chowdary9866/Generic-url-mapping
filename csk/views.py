from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def msd(request):
    return HttpResponse('<h1> Msd is best player </h1>')
def raina(request):
    return render(request,'basic.html')
