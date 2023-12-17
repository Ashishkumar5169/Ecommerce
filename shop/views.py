from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from datetime import datetime
from django.db import connection

# Create your views here.
def base(request):
    return render(request,'base.html')

def index(request):
    user=request.session.get('userid')
    ct=""
    if user:
        ct=mcart.objects.all().filter(userid=user).count()
    x=category.objects.all().order_by('-id')
    y=myproduct.objects.all()

    mydict={"data":x,"prodata":y,"cart":ct}
    return render(request,'app/index.html',context=mydict)

def aboutus(request):
    user=request.session.get('userid')
    ct=""
    if user:
        ct=mcart.objects.all().filter(userid=user).count()
    return render(request,'app/aboutus.html',{"cart":ct})

def enquiry(request):
    status=False
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        mob=request.POST.get('mob')
        message=request.POST.get('msg')
        contact(Name=name,Email=email,Mobile=mob,Message=message).save()
        status=True
    msg={'m':status}
    return render(request,'app/enquiry.html',context=msg)

def myorder(request):
    user=request.session.get('userid')
    oid=request.GET.get('oid')
    mydict={}
    if user:
        if oid is not None:
            morder.objects.all().filter(id=oid).delete()
            return HttpResponse("<script>alert('Your Order has been Cancelled...');location.href='/myorder/'</script>")
        cursor=connection.cursor()
        cursor.execute("select p.*,o.* from shop_myproduct p,shop_morder o where p.id=o.pid and o.userid='"+str(user)+"' and o.remarks='Pending'")
        pdata=cursor.fetchall()
        cursor.execute("select p.*,o.* from shop_myproduct p,shop_morder o where p.id=o.pid and o.userid='"+str(user)+"' and o.remarks='Delivered'")
        ddata=cursor.fetchall()
        mydict={"pdata":pdata,"ddata":ddata}
    return render(request,'app/myorder.html',mydict)

def myprofile(request):
    user=request.session.get('userid')
    x=""
    if user:
        if request.method=="POST":
            Name=request.POST.get('name')
            Mobile=request.POST.get('mob')
            Passwd=request.POST.get('passwd')
            Address=request.POST.get('address')
            Picture=request.FILES.get('pic')
            register(email=user,name=Name,mobile=Mobile,ppic=Picture,passwd=Passwd,address=Address).save()
            return HttpResponse("<script>alert('Your Profile Updated Successfully...');location.href='/myprofile/'</script>")
        x=register.objects.all().filter(email=user)
    mydata={"mdata":x}
    return render(request,'app/myprofile.html',mydata)

def product(request):
    return render(request,'app/product.html')


def signin(request):
    if request.method=="POST":
        Email=request.POST.get('email')
        Password=request.POST.get('passwd')
        x=register.objects.all().filter(email=Email,passwd=Password).count()
        y=register.objects.all().filter(email=Email,passwd=Password)
        if x==1:
            request.session['userid']=Email
            request.session['userpic']=str(y[0].ppic)
            return HttpResponse("<script>alert('You are Login...');location.href='/signin/'</script>")
        else:
            return HttpResponse("<script>alert('Your userid or password is incorrect..');location.href='/signin/'</script>")
    return render(request,'app/signin.html')


def signup(request):
    if request.method=="POST":
        Name=request.POST.get('name')
        Email=request.POST.get('email')
        Mobile=request.POST.get('mob')
        Passwd=request.POST.get('passwd')
        Address=request.POST.get('address')
        Picture=request.FILES.get('pic')
        x=register.objects.all().filter(email=Email).count()
        if x==0:
            register(name=Name,email=Email,mobile=Mobile,ppic=Picture,passwd=Passwd,address=Address).save()
            return HttpResponse("<script>alert('You are Registered successfully');location.href='/signup/'</script>")
        else:
            return HttpResponse("<script>alert('Your email id is already registered..');location.href='/signup/'</script>")
    return render(request,'app/signup.html')


def mens(request):
    cid=request.GET.get('msg')
    cat=category.objects.all().order_by('-id')
    d=myproduct.objects.all().filter(mcategory=1)
    if cid is not None:
        d=myproduct.objects.all().filter(mcategory=1,pcategory=cid)
    mydict={"cats":cat,"data":d,"a":cid}
    return render(request,'app/mens.html',mydict)


def womens(request):
    cid=request.GET.get('msg')
    cat=category.objects.all().order_by('-id')
    d=myproduct.objects.all().filter(mcategory=2)
    if cid is not None:
        d=myproduct.objects.all().filter(mcategory=2,pcategory=cid)
    mydict={"cats":cat,"data":d,"a":cid}
    return render(request,'app/womens.html',mydict)


def kids(request):
    cid=request.GET.get('msg')
    cat=category.objects.all().order_by('-id')
    d=myproduct.objects.all().filter(mcategory=3)
    if cid is not None:
        d=myproduct.objects.all().filter(mcategory=3,pcategory=cid)
    mydict={"cats":cat,"data":d,"a":cid}
    return render(request,'app/kids.html',mydict)


def viewproduct(request):
    a=request.GET.get('msg')
    x=myproduct.objects.all().filter(id=a)
    return render(request,'app/viewproduct.html',{"pdata":x,"msg":a})


def signout(request):
    if request.session.get('userid'):
        del request.session['userid']
    return HttpResponse("<script>alert('You are signed out...');location.href='/index/'</script>")

def myordr(request):
    user=request.session.get('userid')
    pid=request.GET.get('msg')

    if user:
        if pid is not None:
            morder(userid=user,pid=pid,remarks="Pending",odate=datetime.now().date(),status=True).save()
            return HttpResponse("<script>alert('Your Order confirmed...');location.href='/index/'</script>")
    else:
        return HttpResponse("<script>alert('You have to login first...');location.href='/signin/'</script>")
    return render(request,'app/myordr.html')

def mycart(request):
    p=request.GET.get('pid')
    user=request.session.get('userid')
    if user:
        if p is not None:
            mcart(userid=user,pid=p,cdate=datetime.now().date(),status=True).save()
            return HttpResponse("<script>alert('Your Item is added cart..');location.href='/index/'</script>")
    else:
        return HttpResponse("<script>alert('You have to login first...');location.href='/signin/'</script>")
    return render(request,'app/mycart.html')


def showcart(request):
    user=request.session.get('userid')
    md={}
    a=request.GET.get('msg')
    cid=request.GET.get('cid')
    pid=request.GET.get('pid')
    if user:
        if a is not None:
            mcart.objects.all().filter(id=a).delete()
            return HttpResponse("<script>alert('Your item is deleted from card...');location.href='/showcart/'</script>")
        elif pid is not None:
            mcart.objects.all().filter(id=cid).delete()
            morder(userid=user,pid=pid,remarks="Pending",status=True,odate=datetime.now().date()).save()
            return HttpResponse("<script>alert('Your Order has been placed successfully..');location.href='/myorder/'</script>")
        cursor=connection.cursor()
        cursor.execute("select p.*,c.* from shop_myproduct p,shop_mcart c where p.id=c.pid and c.userid='"+str(user)+"'")
        cdata=cursor.fetchall()
        md={"cdata":cdata}
    return render(request,'app/showcart.html',md)


def cpdetail(request):
    c=request.GET.get('cid')
    p=myproduct.objects.all().filter(pcategory=c)
    return render(request,'app/cpdetail.html',{"pdata":p})