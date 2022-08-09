from email.policy import default
from django.db import models
from django.core.validators import validate_comma_separated_integer_list


# Create your models here.
class FundRaiserModel(models.Model):
    fund_id=models.AutoField(primary_key=True)
    name=models.TextField(help_text='Enter Your Name',)
    relation=models.TextField(help_text='enter Your Relation')
    phone_number=models.BigIntegerField(help_text='enter phone number',null=True,blank=True)
    gmail=models.EmailField(help_text='Enter gmail')
    upload_image=models.ImageField(upload_to='images/')
    upload_doc=models.ImageField(upload_to='document/images/' )
    upload_proof=models.ImageField(upload_to='proof/images/')
    describtion=models.TextField(help_text='Enter describtion ', max_length=500)
    title=models.CharField(help_text='Enter tittle' , max_length=50)
    proof=models.CharField(help_text='Types of proof ' , max_length=50)
    document_verification=models.CharField(help_text='Enter document_verification', max_length=50)
    gender=models.CharField(help_text='currency' ,max_length=100,null=True,blank=True)
    fund_price=models.BigIntegerField(null=True)
    # fund_price=models.CommaSeparatedIntegerField(help_text='fund_price' ,null=True)
    cause=models.TextField(help_text='cause',null=True)
    raisefundfor=models.TextField(help_text='raisefundfor',null=True)
    status=models.TextField(default='pendding',null=True)
    price=models.BigIntegerField(null=True)
    submitted_date=models.DateField(auto_now_add=True,null=True)
    
    class Meta:
        db_table='fund_raiser_details'
        
              
class UserModel(models.Model):
    signup_id=models.AutoField(primary_key=True)
    name=models.TextField(help_text='Enter Your Name' , max_length=50)
    gmail=models.EmailField(help_text='Enter gmail', max_length=50)
    password=models.CharField(help_text='enter Password',max_length=200)
    reg_date=models.DateField(auto_now_add=True,null=True)
    
    class Meta:
        db_table='user_details'
        
        
class PaymentModel(models.Model):
    fund_id = models.ForeignKey(FundRaiserModel, on_delete=models.CASCADE,null=True)
    payment_id=models.AutoField(primary_key=True)
    name=models.CharField(help_text='Enter Your Name',null=True,max_length=100)
    gmail=models.EmailField(help_text='Enter Gmail Here',null=True)
    country=models.CharField(help_text='Enter country here',max_length=200)
    phno=models.BigIntegerField()
    payment_date=models.DateField(auto_now_add=True,null=True)
    cardnumber=models.CharField(help_text='cardnumber',max_length=15,null=True)
    cardholder_name=models.TextField(help_text='Enter Your Name',null=True)
    
   
    
    amount=models.BigIntegerField(null=True)
    
    
    class Meta:
        db_table='payment_details'
        
class FeedbackModel(models.Model):
    feedback_id=models.AutoField(primary_key=True)  
    user_name=models.TextField( help_text='feeback_name')
    user_cause=models.CharField( help_text='feeback_cause',max_length=25)     
    user_email=models.CharField( help_text='feeback_email',max_length=25)
    fund_id=models.CharField(help_text='fund_id', max_length=50,null=True)
    user_feedbacks=models.TextField( help_text='feebacks',null=True) 
    feedback_date=models.DateField(auto_now_add=True,null=True)
    
    class Meta:
        db_table='feedback_details'     
 
        




    
    