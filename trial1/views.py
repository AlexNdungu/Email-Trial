from django.shortcuts import render
from django.core.mail import EmailMessage,send_mail
from .forms import sendEmail
from django.conf import settings
from django.shortcuts import redirect
import idna
from django.shortcuts import get_object_or_404


# Create your views here.

def index(request):
    return render(request, 'index.html')

def email(request): 
   
    form = sendEmail()
    if request.method == 'POST':
        form = sendEmail(request.POST)
        if form.is_valid():
            subject = 'Remedy Pavers Daily Review'
            info = 'Welcome Here'
            sender = form.cleaned_data.get('person_email')
            send_mail(subject,info,settings.EMAIL_HOST_USER,[sender])
    return render(request, 'email.html',{'form':form}) 
