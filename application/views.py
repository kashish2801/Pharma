from django.shortcuts import render
from django.http import HttpResponse
from application.models import enquiry_table
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'index.html')
    
def aboutus(request):
    return render(request,"index.html")



def contactus(request):
    if request.method == "POST":
        a = request.POST.get('name')
        b = request.POST.get('email')
        c = request.POST.get('phone')
        d = request.POST.get('message')
        enquiry = enquiry_table(name = a, email = b, phone = c, message = d)
        enquiry.save()

        messages.success(request, 'Enquiry Form Submitted Successfully...')
        
    return render(request, 'contact.html')

def login_user(request):
    return render(request,'login.html')

def generic(request):
    return render(request,'generic.html')
    