import re
from unicodedata import name
from wsgiref.util import request_uri
from django.shortcuts import render, redirect, get_object_or_404
from fundraiser.settings import DEFAULT_FROM_EMAIL
from django.core.mail import EmailMultiAlternatives
from django.contrib import messages
from userapp.models import *
import requests
import random

# Create your views here.






def adminhome(request):
    adminhome=FundRaiserModel.objects.all()  
    count=FundRaiserModel.objects.filter(cause='Health').count()
    Livelihood=FundRaiserModel.objects.filter(cause='Livelihood').count()
    Education=FundRaiserModel.objects.filter(cause='Education').count()
    Total=count+Livelihood+Education
    return render(request,'admin/admin-index.html',{'adminhome':adminhome,'count':count,'Livelihood':Livelihood,'Education':Education,'Total':Total})

def raiser(request):
    raiser=FundRaiserModel.objects.all()
    return render(request,'admin/admin-view-raiser.html',{'raiser':raiser})

def funds(request):
    funds=FundRaiserModel.objects.all()
    return render(request,'admin/admin-view-funds.html',{'funds':funds})
    


def feedbacks(request):
    feedback=FeedbackModel.objects.all()
    return render(request,'admin/admin-view-feedbacks.html',{'feedback': feedback})

def fundraiserprofile(request,id):
    data = get_object_or_404(FundRaiserModel,fund_id=id)
    data2 = FundRaiserModel.objects.filter(fund_id=id).values('phone_number')
    print(data2.query)

    otp = random.randint(1111,9999)
    
    # mention url
    url = "https://www.fast2sms.com/dev/bulk"
    # create a dictionary
    my_data = {
        # Your default Sender ID
        'sender_id': 'FSTSMS',            
        # Put your message here!
        'message': 'your are done',            
        'language': 'english',
        'route': 'p',            
        # You can send sms to multiple numbers
        # separated by comma.
        # 'numbers':data
   
    }
    
    headers = {
        'authorization': 'O06m5nBxshDJWPpZvidLHoeNMC9IK41agj7XkR3UVFGc2fESur0jdqNoVkSH2At1aWg5lO9ywGPBrLnv',
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache"
    }
    # make a post request
    response = requests.request("POST",
                                url,
                                data = my_data,
                                headers = headers)
    # print the send message
    print(response.text)      
    
    
    
      
    return render(request,'admin/raiserprofile.html',{'data':data})



#STATUS UPDATE

def fundraiserprofileaccept(request,id):
    data = get_object_or_404(FundRaiserModel,fund_id=id)
    data.status = 'Accepted'
    data.save(update_fields=['status'])
    data.save()
    print("this is accept")
    
    #email message
    html_content = "<br/> <p> fundraiser application has been successfully accepted</p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [data.gmail]
    
    # if send_mail (subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("fundraiser Application Status",html_content,from_mail,to_mail)
    msg.attach_alternative(html_content,"text/html")
    if msg.send():
        print("sent")
        
       
    
    
    
    return redirect('view_fundraisers')
    
def fundraiserprofilereject(request,id):
    accept = get_object_or_404(FundRaiserModel,fund_id=id)
    accept.status = 'Rejected'
    accept.save(update_fields=['status'])
    accept.save()
    
     #email message
    html_content = "<br/> <p> fundraiser application has been Rejected so please Reapply it.</p>"
    from_mail = DEFAULT_FROM_EMAIL
    to_mail = [accept.gmail]
    
    # if send_mail (subject,message,from_mail,to_mail):
    msg = EmailMultiAlternatives("fundraiser Application Status",html_content,from_mail,to_mail)
    msg.attach_alternative(html_content,"text/html")
    if msg.send():
        print("sent")
    
    return redirect('view_fundraisers')




def adminlogin(request):
    if request.method=='POST':
        name=request.POST.get('username') 
        password=request.POST.get('password') 
        if name=='cloud' and password=='cloud':
            return redirect('admin_home')
    return render(request,'admin/login2.html')
