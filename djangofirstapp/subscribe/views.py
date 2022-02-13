from django.shortcuts import render
from name.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail
# Create your views here.

def subscribe(request):
    sub=forms.Subscribe()
    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)
        subject = 'Welcome to schoolMis'
        message = 'Hope you are enjoying your Django Tutorials Now Jeanluc developer here in Django'
        recipient=str(sub['Email'].value())
        send_mail(subject,
                   message,EMAIL_HOST_USER,[recipient],fail_silently=False)   #In this case, it will be smtplib.SMTPException. These are the required fields and can not be empty.
        return render(request,'success.html',{'recepient':recipient})
    return render(request,"index.html",{'form':sub})
