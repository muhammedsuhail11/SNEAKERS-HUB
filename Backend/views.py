from django.shortcuts import render,redirect
from Backend.models import admindb,categorydb,productdb
from Frontend.models import contact,deatilescustomer,savecheckoutdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
def indexpage(req):
    return render(req,"index.html")
def addadmin(req):
    return render(req,"add_admin.html")
def saveadmin(req):
    if req.method== "POST":
        NAME=req.POST.get('name')
        EMAIL=req.POST.get('email')
        PASSWORD =req.POST.get("password")
        CONFIRMPASSWORD = req.POST.get("conpassword")
        IMAGE = req.FILES['image']
        obj=admindb(Name=NAME,Email=EMAIL,Password=PASSWORD,Confirmpassword=CONFIRMPASSWORD,Image=IMAGE)
        obj.save()
        return redirect(addadmin)
def displayadmin(req):
    data=admindb.objects.all()
    return render(req,"displayadmin.html",{'data':data})
def editadmin(req,dataid):
    data=admindb.objects.get(id=dataid)
    print(data)
    return render(req,"edit_admin.html",{'data':data})
def updateadmin(req,dataid):
    if req.method=="POST":
        NAME = req.POST.get('name')
        EMAIL = req.POST.get('email')
        PASSWORD = req.POST.get("password")
        CONFIRMPASSWORD = req.POST.get("conpassword")
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = admindb.objects.get(id=dataid).image
        admindb.objects.filter(id=dataid).update(Name=NAME,Email=EMAIL,Password=PASSWORD,Confirmpassword=CONFIRMPASSWORD,Image=file)
        return redirect(displayadmin)
def deleteadmin(req,dataid):
    data=admindb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayadmin)
def addcategory(req):
    return render(req, "addcategory.html")
def savecategory(req):
    if req.method== "POST":
        Name=req.POST.get('name')
        DISCRIPTION=req.POST.get('discription')
        IMAGE = req.FILES['image']
        obj = categorydb(Name=Name, Discription=DISCRIPTION,  Image=IMAGE)
        obj.save()
        return redirect(addcategory)
def viewcategory(req):
    data = categorydb.objects.all()
    return render(req, "displaycategory.html",{'data': data})
def editcategory(req,dataid):
    data=categorydb.objects.get(id=dataid)
    print(data)
    return render(req,"edit_category.html",{'data':data})
def updatecategory(req,dataid):
    if req.method=="POST":
        NAME = req.POST.get('name')
        DISCRIPTION = req.POST.get('discription')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = categorydb.objects.get(id=dataid).image
        categorydb.objects.filter(id=dataid).update(Name=NAME,Discription=DISCRIPTION,Image=file)
        return redirect(viewcategory)
def deletecategory(req,dataid):
    data=categorydb.objects.filter(id=dataid)
    data.delete()
    return redirect(viewcategory)

def addproduct(req):
    data=categorydb.objects.all()
    return render(req,"addproduct.html",{"data":data})
def saveproduct(req):
    if req.method== "POST":
        NAME=req.POST.get("name")
        PRICE=req.POST.get("price")
        DISCRIPTION =req.POST.get("discription")
        CATEGORY=req.POST.get("category")
        QUANTITY  = req.POST.get("quantity")
        IMAGE = req.FILES['image']
        IMAGE2 = req.FILES['image2']
        IMAGE3 = req.FILES['image3']
        obj=productdb(Name=NAME,Price=PRICE,Discription=DISCRIPTION,CATEGORY=CATEGORY,Quantity=QUANTITY,Image=IMAGE,Image2=IMAGE2,Image3=IMAGE3)
        obj.save()
        return redirect(addproduct)
def displayproduct(req):
    data = productdb.objects.all()
    return render(req,"displayproduct.html",{'data': data})
def editproduct(req,dataid):
    data=productdb.objects.get(id=dataid)
    da = categorydb.objects.all()
    print(data)
    return render(req,"edit_product.html",{'data':data,'da':da})
def updateproduct(req,dataid):
    if req.method=="POST":
        NAME = req.POST.get('name')
        PRICE = req.POST.get('price')
        DISCRIPTION = req.POST.get('discription')
        CATEGORY = req.POST.get("category")
        QUANTITY = req.POST.get('quantity')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = productdb.objects.get(id=dataid).Image
        productdb.objects.filter(id=dataid).update(Name=NAME,Price=PRICE,Discription=DISCRIPTION,CATEGORY=CATEGORY,Quantity=QUANTITY,Image=file)
        return redirect(displayproduct)
def deleteproduct(req,dataid):
    data=productdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayproduct)

def loginpage(req):
    return render(req,"login.html")
def adminlogin(req):
    if req.method=="POST":
        username_r=req.POST.get('username')
        password_r = req.POST.get('password')
        if User.objects.filter(username__contains=username_r).exists():
            user=authenticate(username=username_r,password=password_r)
            if user is not None:
                login(req,user)
                req.session['username']=username_r
                req.session['password']=password_r
                return redirect(indexpage)
            else:
                return redirect(loginpage)
        else:
            return redirect(loginpage)
def logoutadmin(req):
    del req.session['username']
    del req.session['password']
    return redirect(loginpage)

def displaymessage(req):
    data = contact.objects.all()
    return render(req,"display_complaint.html",{'data': data})

def deletemessage(req,dataid):
    data=contact.objects.filter(id=dataid)
    data.delete()
    return redirect(displaymessage)

def displaycheckout(req):
    data = savecheckoutdb.objects.all()
    return render(req,"checkout_details.html",{'data': data})
def deletedetails(req,dataid):
    data=savecheckoutdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycheckout)




