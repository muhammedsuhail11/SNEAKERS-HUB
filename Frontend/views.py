from django.contrib import messages
from django.shortcuts import render,redirect
from Backend.models import productdb,categorydb,cartdb
from Frontend.models import deatilescustomer,contact,savecheckoutdb


# Create your views here.
def homepage(req):
    data = categorydb.objects.all()
    return render(req,"homepage.html",{"data":data})

def categorypage(req):
    data=categorydb.objects.all()
    return render(req,"category_page.html",{"data":data})

def contactpage(req):
    return render(req,"contact.html")
def aboutpage(req):
    return render(req,"about.html")


def displayproductpage(request,itemcatg):
    print("===itemcatg===", itemcatg)
    catg = itemcatg.upper()

    products = productdb.objects.filter(CATEGORY=itemcatg)
    context = {
        'products': products,
        'catg': catg
    }

    return render(request,"productpage.html",context)

def productsinglee(req,dataid):
    data = productdb.objects.filter(id=dataid)
    return render(req, "productsingle.html", {'data': data})
def cartpage(req):
    data=cartdb.objects.all()
    return render(req,"cartview.html",{'data':data})
def savecartdb(req):
    if req.method== "POST":
        Name=req.POST.get('name')
        qty=req.POST.get('quantity')
        to = req.POST.get('totalprice')
        obj = cartdb(Name=Name, Quantity=qty,Total=to)
        obj.save()
        messages.success(req, "your item is added to cart")
        return redirect(homepage)
def deletecart(req,dataid):
    data=cartdb.objects.filter(id=dataid)
    data.delete()
    return redirect(cartpage)

def checkoutt(req):
    return render(req,"checkout.html")

def webloginpage(req):
    return render(req,"Weblogin.html")

def custemerlogin(request):
    if request.method=='POST':
        Username_r=request.POST.get("username")
        Password_r=request.POST.get("password")

        if deatilescustomer.objects.filter(Username=Username_r,Password=Password_r).exists():
            request.session['username']=Username_r
            request.session['password']=Password_r
            messages.success(request,"login successfully")
            return redirect(homepage)
        else:
            messages.error(request,"invalid user")
    return render(request,'weblogin.html')

def logout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "Logout successfully")
    return redirect(webloginpage)

def savecustomer(request):
    if request.method == "POST":
        Us  = request.POST.get('username')
        pas = request.POST.get('password')
        Em  = request.POST.get('email')
        Cp  = request.POST.get("confirmpassword")
        if pas==Cp:
            obj = deatilescustomer(Username=Us,Password=pas,confirmpassword=Cp,Email=Em,)
        obj.save()
        messages.success(request,"registered successfully")
        return redirect(webloginpage)
def savecontact(req):
    if req.method== "POST":
        NAME=req.POST.get('name')
        EMAIL=req.POST.get('email')
        SUBJECT = req.POST.get('subject')
        MESSAGE = req.POST.get('message')
        obj = contact(Name=NAME, Email=EMAIL,Subject=SUBJECT,Message=MESSAGE)
        obj.save()
        messages.success(req, "You have registered your review")
        return redirect(homepage)
def savecheckout(req):
    if req.method== "POST":
        FNAME=req.POST.get('fname')
        SNAME = req.POST.get('sname')
        EMAIL=req.POST.get('email')
        COUNTRY = req.POST.get('country')
        ADDRESS = req.POST.get('address')
        STATE = req.POST.get('state')
        PINCODE = req.POST.get('pincode')
        obj = savecheckoutdb(FName=FNAME,SName=SNAME, Email=EMAIL,Address=ADDRESS,Country=COUNTRY,State=STATE,Pincode=PINCODE)
        obj.save()
        messages.success(req, "You have Successfully Ordered")
        return redirect(homepage)







