from django.shortcuts import render
from bloogapp.models import blog,POSTBLOG
from bloogapp.forms import signup,postblog
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.
def home(request):
    return render(request,'bloogapp/home.html');

def Signup(request):
    Sign=signup()
    mydict={'Sign':Sign}
    if request.method=='POST':
        Sign=signup(request.POST)
        user=Sign.save()
        user.set_password(user.password)
        user.save()
        subject="BLOOGINGSITE WELCOME MAIL"
        message="Welcome" +user.email+ ",your registration is done!!"
        recipient_list=[user.email]
        email_form=settings.EMAIL_HOST_USER
        send_mail(subject,message,email_form,recipient_list)
        mydict.update({'msg':'Registered Successfully'})
    return render(request,'bloogapp/signup.html',context=mydict);

@login_required
def viewblogs(request):
    images=POSTBLOG.objects.all().order_by('-id')
    mydict={'images':images}
    return render(request,'bloogapp/viewblogs.html',context=mydict)

@login_required
def postblogs(request):
    Postblog=postblog()
    mydict={'Postblog':Postblog}
    if request.method=='POST':
        Postblog=postblog(request.POST,request.FILES)
        if Postblog.is_valid():
            data=Postblog.save(commit=False)
            data.author=request.user
            data.save()
            mydict.update({'msg':'New Blog Register'})
    return render(request,'bloogapp/postblogs.html',context=mydict);

def detail(request,did):
    images=POSTBLOG.objects.get(id=did)
    mydict={'images':images}
    return render(request,'bloogapp/detail.html',context=mydict )

def viewdelete(request,did):
    images=POSTBLOG.objects.get(id=did)
    images.delete()
    images=POSTBLOG.objects.all().order_by('-id')
    return render(request,'bloogapp/viewblogs.html',{'images':images ,'msg':'DELETE RECORD'})
