
from ast import Pass
from random import random
from typing_extensions import dataclass_transform
from django.shortcuts import render,redirect,get_object_or_404 
from userapp.models import *
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db.models import Sum
from django.http import HttpResponseRedirect
import requests
import random


# Create your views here.



def smsapi(request):
    if request.method=="POST":
        
        
        otp = random.randint(1111,9999)
        mobile = request.POST.get("mobile")  
        # mention url
        url = "https://www.fast2sms.com/dev/bulk"
        # create a dictionary
        my_data = {
            # Your default Sender ID
            'sender_id': 'FSTSMS',            
            # Put your message here!
            'message': 'your y4y6',            
            'language': 'english',
            'route': 'p',            
            # You can send sms to multiple numbers
            # separated by comma.
            'numbers': mobile   
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


    
    return render(request,'user/test.html')

def home2(request):
    livelihood = FundRaiserModel.objects.filter(cause = "Livelihood", status="Accepted").order_by('-submitted_date').values("cause","title","upload_image","fund_price","fund_id","describtion","raisefundfor","gmail","phone_number","price").exclude(price="0").first()
    health = FundRaiserModel.objects.filter(cause = "Health", status="Accepted").order_by('-submitted_date').values("cause","title","upload_image","fund_price","fund_id","describtion","raisefundfor","gmail","phone_number","price").exclude(price="0").first()
    education = FundRaiserModel.objects.filter(cause = "Education", status="Accepted").order_by('-submitted_date').values("cause","title","upload_image","fund_price","fund_id","describtion","raisefundfor","gmail","phone_number","price").exclude(price="0").first()
    
    return render(request,'user/index2.html',{'livelihood':livelihood,'health':health,'education':education})


def about(request):
    livelihood = FundRaiserModel.objects.filter(cause = "Livelihood", status="Accepted").order_by('-submitted_date').values("cause","title","upload_image","fund_price","fund_id","describtion","raisefundfor","gmail","phone_number","price").exclude(price="0").first()
    health = FundRaiserModel.objects.filter(cause = "Health", status="Accepted").order_by('-submitted_date').values("cause","title","upload_image","fund_price","fund_id","describtion","raisefundfor","gmail","phone_number","price").exclude(price="0").first()
    education = FundRaiserModel.objects.filter(cause = "Education", status="Accepted").order_by('-submitted_date').values("cause","title","upload_image","fund_price","fund_id","describtion","raisefundfor","gmail","phone_number","price").exclude(price="0").first()
    return render(request,'user/about.html',{'livelihood':livelihood,'health':health,'education':education})


def login(request):  
    if request.method=='POST':
    
      gmail = request.POST.get('email')
      password = request.POST.get('password') 
      
      try:
            check = UserModel.objects.get(gmail=gmail,password=password)
          
            request.session['signup_id'] = check.signup_id
            messages.success(request,"Your Are Successfully Logged")   
            return redirect ('userdashboard')
        
      except:
            messages.error(request,"Your Email or Password Given Worng")
            return redirect ('login')
            
          
         
       
    return render(request,'user/login.html')

def contact(request):
    if request.method=='POST':
     feedback_name= request.POST.get('feedback_name')  
     feedback_cause=request.POST.get('feedback_cause') 
     feedback_email=request.POST.get('feedback_email')
     feedbacks=request.POST.get('feedbacks')
     
     FeedbackModel.objects.create(feedback_name=feedback_name,feedback_email=feedback_email,feedback_cause=feedback_cause,feedbacks=feedbacks)
     
    return render(request,'user/contact.html')

def livehood(request):
    
    livelihood = FundRaiserModel.objects.filter(cause = "Livelihood", status="Accepted").order_by('-submitted_date').values("cause","title","upload_image","fund_price","fund_id","describtion","raisefundfor","gmail","phone_number","price").exclude(price="0").first()
    data = FundRaiserModel.objects.filter(cause = "Livelihood",status="Accepted").exclude(price="0").order_by('-submitted_date')
    
  
    return render(request,'user/livehood.html',{'data' : data,'cause': livelihood })

def health(request ):
    health = FundRaiserModel.objects.filter(cause = "Health", status="Accepted").order_by('-submitted_date').values("cause","title","upload_image","fund_price","fund_id","describtion","raisefundfor","gmail","phone_number","price").exclude(price="0").first()
    data = FundRaiserModel.objects.filter(cause = "Health",status="Accepted").exclude(price='0').order_by('-submitted_date')
   
    return render(request,'user/health.html',{'data' : data,'cause': health})   

def education(request):
    education = FundRaiserModel.objects.filter(cause = "Education", status="Accepted").order_by('-submitted_date').values("cause","title","upload_image","fund_price","fund_id","describtion","raisefundfor","gmail","phone_number","price").exclude(price="0").first()
    data = FundRaiserModel.objects.filter(cause = "Education",status="Accepted").order_by('-submitted_date').exclude(price='0')
    
    return render(request,'user/education.html', {'data' : data, 'cause': education})

def userdashboard(request):
     livelihood = FundRaiserModel.objects.filter(cause = "Livelihood", status="Accepted").order_by('-submitted_date').values("cause","title","upload_image","fund_price","fund_id","describtion","raisefundfor","gmail","phone_number","price").exclude(price="0").first()
     health = FundRaiserModel.objects.filter(cause = "Health", status="Accepted").order_by('-submitted_date').values("cause","title","upload_image","fund_price","fund_id","describtion","raisefundfor","gmail","phone_number","price").exclude(price="0").first()
     education = FundRaiserModel.objects.filter(cause = "Education", status="Accepted").order_by('-submitted_date').values("cause","title","upload_image","fund_price","fund_id","describtion","raisefundfor","gmail","phone_number","price").exclude(price="0").first()
    
    
     return render(request,'user/user-dashboard.html',{'livelihood':livelihood,'health':health,'education':education})

def userfeedback(request):
     user=request.session["signup_id"]
     data = FundRaiserModel.objects.filter(fund_id=user)
     print('data')
     
     
      
     
     if request.method=='POST':
        user_cause=request.POST.get('user_cause') 
        user_name= request.POST.get('user_name')  
        user_email=request.POST.get('user_email')
        user_feedbacks=request.POST.get('user_feedbacks')
         
         
        FeedbackModel.objects.create(user_feedbacks=user_feedbacks, user_name = user_name, user_email=user_email, user_cause=user_cause)
     
    
     return render(request,'user/user-feedback.html',{'data':data})

def userfund(request):
    user=request.session["signup_id"]
    # data = FundRaiserModel.objects.filter(fund_id=user)
    # print(data)
    
    # values('fund_price','price')
    data2 = FundRaiserModel.objects.filter(fund_id=user).values('price')
    
    data = PaymentModel.objects.select_related('fund_id').filter(fund_id=user)
    print(data.query)
    
    data3 = PaymentModel.objects.all().filter(fund_id=user).aggregate(payment=Sum('amount'))
    print(data3)
    
    
    for f in data :
        a = f.fund_id
        b = a.price
        print(b)
    
    
    # for i in data:
    #     c = i.aggregatie
        
    #     print(c)   
    
    
    for j in data :
        
        k = j.fund_id
        l = k.fund_price
        print(l)
             
    
    return render(request,'user/user-funds.html',{'data':data,'data2':data2,'left':b,'fund':l,'payment':data3})

def userprofile(request):
    user=request.session["signup_id"]
    
    data = FundRaiserModel.objects.filter(fund_id=user)
    print(data)
    obj=get_object_or_404(FundRaiserModel,fund_id=user)
    if request.method =='POST'and request.FILES['upload_image']:
        
        name=request.POST['Name']
        relation=request.POST['relation']
        phone_number=request.POST['phone_number']
        gmail=request.POST['email']
        describtion=request.POST['describtion']
 
        title=request.POST['title']
        
        upload_image=request.FILES['upload_image']
        
        cause=request.POST['cause']
        raisefundfor=request.POST['raisefundfor']
        
        
        
        obj.name=name
        obj.relation=relation
        
        obj.phone_number=phone_number
        obj.gmail=gmail
        obj.upload_image=upload_image
        obj.describtion=describtion
       
        obj.title=title
        
       
        obj.cause=cause
        obj.raisefundfor=raisefundfor
        obj.save(update_fields=['name','relation','phone_number','gmail','describtion','title','cause','raisefundfor','upload_image'])
    
    return render(request,'user/user-profile.html',{'data':data})


def donate(request):
    if request.method=='POST':
        name = request.POST.get('fname')
        gmail = request.POST.get('email')
        country = request.POST.get('country')
        phonenumber = request.POST.get('tel')
        # debitcard
        cardholder_name= request.POST.get('cardholder_name')
        cardnumber= request.POST.get('cardnumber')
        startmonth= request.POST.get('start')
        expiarydate= request.POST.get('expiary')
        cvv= request.POST.get('cvv')
        amount=request.POST.get('amount')
        # creditcard
        
        # netbanking
        selectbank=request.POST.get('selectbank')
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        
        PaymentModel.objects.create(username=username,amount=amount,password=password,selectbank=selectbank,cardholder_name=cardholder_name,cardnumber=cardnumber,startmonth=startmonth,expiarydate=expiarydate,cvv=cvv,name=name,gmail=gmail,country=country,phno=phonenumber)
    
    return render(request,'user/donate.html')

def donateaction(request,id):
    # user = request.session["signup_id"]
    print(id)
    data1 = FundRaiserModel.objects.get(fund_id = id)
    
   
    
    price_1 = int(data1.price)
    print(price_1)

    
    # data = FundRaiserModel.objects.all().filter(fund_id=id)
    # print('hello')
    # print('hello')
    
    data= id
    print(data)
    if request.method=='POST':
        name = request.POST.get('fname')
        gmail = request.POST.get('email')
        country = request.POST.get('country')
        phonenumber = request.POST.get('tel')
        # debitcard
        cardholder_name= request.POST.get('cardholder_name')
        cardnumber= request.POST.get('cardnumber')
        # startmonth= request.POST.get('start')
        # expiarydate= request.POST.get('expiary')
        # cvv= request.POST.get('cvv')
        amount=request.POST.get('amount')
        # creditcard
        
        # # netbanking
        # selectbank=request.POST.get('selectbank')
        # username=request.POST.get('username')
        # password=request.POST.get('password')
        
        
        
       
         
     
        price_2 = int(amount)
        
       
        print(price_2)
        print(price_1)
        if price_2 < price_1 or price_2 == price_1:
             data1.price = price_1 - price_2
             data1.save(update_fields=['price'])
             data1.save()
             messages.success(request,"Your Are Payment is successfull") 
             
        else:
            messages.error(request,"please enter valid amount")
            return HttpResponseRedirect(request.path_info)
            
         
        
    
        
        
        # data2.price = data2.price - int(amount)
        # data2.save(update_fields = ['price'])
        # data2.save()
        
        PaymentModel.objects.create(cardholder_name=cardholder_name,cardnumber=cardnumber,amount=amount,fund_id=data1,name=name,gmail=gmail,country=country,phno=phonenumber)
       
            
    
    return render(request,'user/donate.html',{'donate':data1,'left':price_1})




def signup(request):
    if request.method =='POST':
        name=request.POST.get('name')
        gmail=request.POST.get('gmail')
        password=request.POST.get('password')
        if UserModel.objects.filter(gmail=gmail).exists():
            messages.error(request,"Email Already Existed")
            return redirect("signup")
        else:
            user=UserModel.objects.create(name=name,gmail=gmail,password=password)
            user.save()
            messages.success(request,"Your Account Is Successfully Registered")          
    return render(request,'user/signup-form-user.html')
    

def fundrasing(request):
    if request.method =='POST' and request.FILES['upload_proof'] and request.FILES['upload_doc'] and request.FILES['upload_image']:
        name=request.POST['Name']
        relation=request.POST['relation']
        phone_number=request.POST['phone_number']
        gmail=request.POST['email']
        upload_image=request.FILES['upload_image']
        upload_doc=request.FILES['upload_doc']
        upload_proof=request.FILES['upload_proof']
        describtion=request.POST['describtion']
        document_verification=request.POST['document_verification']
        title=request.POST['title']
        proof=request.POST['proof']
        gender=request.POST['currency']
        price=request.POST['fund_price']
        fund_price=request.POST['fund_price']
        cause=request.POST['cause']
        raisefundfor=request.POST['raisefundfor']
        
        raiser = FundRaiserModel.objects.create(name=name,relation=relation,phone_number=phone_number,gmail=gmail,upload_image=upload_image,upload_proof=upload_proof,upload_doc=upload_doc,describtion=describtion,document_verification=document_verification,gender=gender,title=title,proof=proof,fund_price=fund_price,cause=cause,raisefundfor=raisefundfor,price=price)
          
        raiser.save()
        if raiser:
             messages.success(request,"Your Registration Form Is Successfully Uploaded")       
        else:
            
            Pass
           
            
            
             
        
    return render(request,'user/user-fundraiser-register.html')
    