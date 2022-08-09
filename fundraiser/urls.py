"""fundraiser URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from userapp import views as user_views
from adminapp import views as admin_views

urlpatterns = [
    
    path('admins', admin.site.urls), 
    
    path('sms',user_views.smsapi,name='sms2'),
    path('',user_views.home2,name='home2'),
    path('about',user_views.about,name='about'),
    path('login',user_views.login,name='login'),
    path('contact',user_views.contact,name='contact'),
    path('livehood',user_views.livehood,name='livehood'),
    path('userprofile',user_views.userprofile,name='userprofile'),
    path('userdashboard',user_views.userdashboard,name='userdashboard'),
    path('userfeedback',user_views.userfeedback,name='userfeedback'),
    path('userfund',user_views.userfund,name='userfund'),
    path('health',user_views.health,name='health'),
    path('education',user_views.education,name='education'),
    # path('creditcard',user_views.payment,name='creditcard'),
    path('donate',user_views.donate,name='donate'),
    path('donateaction2',user_views.donateaction,name='donateaction2'),
    path('donateaction/<int:id>',user_views.donateaction,name='donateaction'),
    path('signup',user_views.signup,name='signup'),
    # path('netbanking',user_views.netbanking,name='netbanking'),
    path('fundrasing',user_views.fundrasing,name='fundrasing'),
    
    # <admin pages starts here:>
    
    path('admindashboard',admin_views.adminhome,name='admin_home'),
    path('view-fundraisers',admin_views.raiser,name='view_fundraisers'),
    path('view-funds',admin_views.funds,name='view_funds'),
    #path('view_fundraiser_profile',admin_views.fundraiserprofile,name='view_fundraiser_profile'),
    path('view_fundraiser_profile/<int:id>/',admin_views.fundraiserprofile,name='view_fundraiser_profile'),
    # accept_fundraiser_profile status
    
    
    path('fundraiserprofile_accept/<int:id>/', admin_views.fundraiserprofileaccept, name='fundraiserprofile_accept'),
    path('fundraiserprofile_reject/<int:id>/',admin_views.fundraiserprofilereject,name='fundraiserprofile_reject'),
    
    
    path('view-feedbacks',admin_views.feedbacks,name='view_feedbacks'),
    path('view-adminlogin',admin_views.adminlogin,name='admin_login'),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)