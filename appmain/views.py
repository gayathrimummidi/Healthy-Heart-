from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
#main-home(index)
def home(request):
    return render(request,'maintemplate/main-index.html')

#main-admin
def admin(request):
    x = 'admin'
    y = 'admin'
    if request.method == "POST":
        aemail=request.POST.get("aemail")
        apassword=request.POST.get("apassword")
        if (aemail == x and apassword == y):
            messages.success(request,"Login successful")
            return redirect('admindashboard')
        else:
            messages.error(request,"Invalid Details")
            return redirect('admin')
    return render(request,'maintemplate/main-admin.html')

#main-about
def about(request):
    return render(request,'maintemplate/main-about.html')

#main-contact
def contact(request):

    return render(request,'maintemplate/main-contact.html')