from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore

from.models import departments,contacts


def index(request):
   person={
       'name':'John',
       'age':30,
       'place':'Calicut'
   }
   numbers={
       'num1':10,
   }
   return render(request,'index.html',numbers)
# Create your views here.

def about(request):
    return render(request,'about.html')

def booking(request):
    return render(request,'booking.html')

def doctors(request):
    return render(request,'doctors.html')

def contact(request):
    dict_dept1={
        'contact':contacts.objects.all()
    } 
    return render(request,'contact.html',dict_dept1)

def department(request):
    dict_dept={
        'dept':departments.objects.all()
    }
    return render(request,'department.html',dict_dept)