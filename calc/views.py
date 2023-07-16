from django.shortcuts import render
from django.http import HttpResponse

# Create your  here.
def home(request):
    
    return render(request,'name.html')
def home1(request):
    name = (request.POST['n1'])
    return render(request,'base.html',{'name':name})
def add(request):

    val1 = int(request.POST['gp1'])
   

    va1 = float(request.POST['cr1'])
    
    resul = (val1+va1)

    return render(request,'result.html',{'result':resul})