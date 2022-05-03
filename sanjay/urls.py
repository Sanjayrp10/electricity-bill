from django.urls import path
from . import views

urlpatterns=[
    path('',views.login,name='login'),
    path('login',views.login,name='login'),
    path('registeration',views.registeration,name='registeration'),
    path('v1',views.v1,name='v1'),
    path('r1',views.r1,name='r1'),
    path('r2',views.r2,name='r2'),
    path('customer',views.customer,name='customer'),  
    path('admin',views.admin,name='admin'),
    path('checkbill',views.checkbill,name='checkbill'),
    path('checkrr',views.checkrr,name='checkrr'),
    path('v2',views.v2,name='v2'),
    path('v3',views.v3,name='v3'),
    path('v4',views.v4,name='v4'),
    path('v5',views.v5,name='v5'),
    path('c1',views.c1,name='c1'),
    path('generatebill',views.generatebill,name='generatebill'),
    path('payment',views.payment,name='payment'),
    path('paymentcheck',views.paymentcheck,name='paymentcheck'),
    path('adminpayment',views.adminpayment,name='adminpayment'),
    path('success',views.success,name='success'),
    path('paymentdetails',views.paymentdetails,name='paymentdetails'),
    path('history',views.history,name='history'),
    path('checkhistory',views.checkhistory,name='checkhistory'),
    
    
    ]
