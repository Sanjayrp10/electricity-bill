from django.shortcuts import render
import mysql.connector
from django.core.files.storage import FileSystemStorage

# Create your views here.

mydb=mysql.connector.connect(

host="localhost",
user="root",
password="root",
database="electricitybill",
charset="utf8"

)

mycur = mydb.cursor()

def login(request):
    return render(request,'login.html')
    
def registeration(request):
    return render(request,'registeration.html') 
    
def r1(request):
    if request.method=="POST":
        RailwayReceiptNumber = request.POST.get("rrno")
        Name = request.POST.get("name")
        Address = request.POST.get("address")
        Contact = request.POST.get("contact")
        UserID = request.POST.get("userid")
        Password = request.POST.get("password")
        sql = "insert into customer_details(RailwayReceiptNumber,Name,Address,Contact,UserID,Password)values(%s,%s,%s,%s,%s,%s)"
        val =(RailwayReceiptNumber,Name,Address,Contact,UserID,Password)
        mycur.execute(sql,val)
        mydb.commit()
        return render(request,'login.html')
        
def v1(request):
    if request.method=="POST":
        UserID = request.POST.get("userid")
        Password = request.POST.get("password")
        if UserID=="admin" and Password=="123":
            return render(request,"admin.html")
        else:
            sql = "select * from customer_details where UserID='"+UserID+"' and Password='"+Password+"'"
            mycur.execute(sql);
            if len(mycur.fetchall())>0:
                return render(request,"customer.html")
            else:
                return render(request,"login.html")
            
def customer(request):
    return render(request,'customer.html')
    
def admin(request):
    return render(request,'admin.html')

def checkrr(request):
    return render(request,'checkrr.html') 

def checkbill(request):
    return render(request,'checkbill.html')      
    
def v2(request):
    if request.method=="POST":
        RailwayReceiptNumber = request.POST.get("rrno")
        sql = "select * from generate where RailwayReceiptNumber='"+RailwayReceiptNumber+"'"
        mycur.execute(sql);
        result = mycur.fetchall();
        if len(result)>0:
            name=result[0][0];
            rrno=result[0][1];
            tax=result[0][5];
            grand=result[0][6];
            return render(request,"checkbill.html",{"res":result,"name":name,"rrno":rrno,"tax":tax,"grand":grand})
        else:
            return render(request,"customer.html")
            
def v3(request):
    if request.method=="POST":
        RailwayReceiptNumber = request.POST.get("rrno")
        sql = "select * from generate where RailwayReceiptNumber='"+RailwayReceiptNumber+"'"
        mycur.execute(sql);
        result = mycur.fetchall();
        if len(result)>0:
            return render(request,"payment.html",{"res":result})
        else:
            return render(request,"customer.html")            

def v4(request):
    if request.method=="POST":
        RailwayReceiptNumber = request.POST.get("rrno")
        sql = "select * from generate where RailwayReceiptNumber='"+RailwayReceiptNumber+"'"
        mycur.execute(sql);
        result = mycur.fetchall();
        if len(result)>0:
            return render(request,"history.html",{"res":result})
        else:
            return render(request,"customer.html")
            
def generatebill(request):
    return render(request,'generatebill.html')
    
def payment(request):
    return render(request,'payment.html')    

def checkhistory(request):
    return render(request,'checkhistory.html')
    
def paymentcheck(request):
    return render(request,'paymentcheck.html')
    
def success(request):
    return render(request,'success.html')
    
    
def r2(request):
    if request.method=="POST":
        Name = request.POST.get("name")
        RailwayReceiptNumber = request.POST.get("rrno")
        Date = request.POST.get("date")
        Hourprice = request.POST.get("hourprice")
        Total = request.POST.get("total")
        Tax = request.POST.get("tax")
        Grandtotal = request.POST.get("grandtotal")
        sql = "insert into generate(RailwayReceiptNumber,Name,Date,Hourprice,Total,Tax,Grandtotal)values(%s,%s,%s,%s,%s,%s,%s)"
        val =(RailwayReceiptNumber,Name,Date,Hourprice,Total,Tax,Grandtotal)
        mycur.execute(sql,val)
        mydb.commit()
        return render(request,'admin.html')
        
def adminpayment(request):
    sql="select customer_details.RailwayReceiptNumber,customer_details.Name,customer_details.Address,customer_details.Contact,customer_details.UserID,customer_details.Password,generate.Grandtotal from customer_details inner join generate on customer_details.RailwayReceiptNumber=generate.RailwayReceiptNumber;"
    mycur.execute(sql);
    result = mycur.fetchall()
    return render(request,'adminpayment.html',{"res":result})
    
def paymentdetails(request):
    sql="select generate.RailwayReceiptNumber,generate.Name,generate.Date,generate.Hourprice,generate.Total,generate.Tax,generate.Grandtotal,payment.Paid from generate inner join payment on generate.RailwayReceiptNumber=payment.RailwayReceiptNumber;"
    mycur.execute(sql);
    result = mycur.fetchall()
    return render(request,'paymentdetails.html',{"res":result})    

def v5(request):
    sql="select payment.Paid,generate.RailwayReceiptNumber,generate.Name,generate.Date,generate.Grandtotal from payment inner join generate on payment.RailwayReceiptNumber=generate.RailwayReceiptNumber;"
    mycur.execute(sql);
    result = mycur.fetchall()
    return render(request,'history.html',{"res":result})
    
def history(request):
    return render(request,'history.html')
    
def c1(request):
    if request.method=="POST":
        RailwayReceiptNumber = request.POST.get("rrno")
        Cardname = request.POST.get("cardname")
        Cardno = request.POST.get("cardno")
        Cardcvc = request.POST.get("cardcvc")
        Cardmonth = request.POST.get("cardmonth")
        Cardyear = request.POST.get("cardyear")
        Paid = request.POST.get("paid")
        sql = "insert into payment(RailwayReceiptNumber,Cardname,Cardno,Cardcvc,Cardmonth,Cardyear,Paid)values(%s,%s,%s,%s,%s,%s,%s)"
        val =(RailwayReceiptNumber,Cardname,Cardno,Cardcvc,Cardmonth,Cardyear,Paid)
        mycur.execute(sql,val)
        mydb.commit()
        return render(request,'customer.html')
        
        
