from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Product,OrderItem
from django.contrib.auth.models import User
from django.urls import reverse
# Create your views here.

def home(request):
    p=Product.objects.all()
    return render(request,'home.html',{'products':p})

def addToCart(request):
    if request.user.is_authenticated:
        c=OrderItem.objects.all().filter(userid=request.user)
        p=[]
        for i in c:
            p.append(i.product)  
        pid=request.POST['productid']
        pdetail=Product.objects.get(id=pid)
        uid=request.user
        order=OrderItem(userid=uid,product=pdetail)
        if order.product not in p:
            order.save()
        else:
            order.update(quantity=order.quantity+1)
        return redirect('/')
    else:
        return redirect('users/login')

def deleteFromCart(request):
    pid=request.POST['productid']
    pdetail=Product.objects.get(id=pid)
    uid=request.user
    order=OrderItem.objects.get(userid=uid,product=pdetail)
    order.delete()    
    return redirect('/cart')


class orderprodetail:
    def __init__(self,product,quantity):
        self.productdetail=product
        self.productquantity = quantity
def showCart(request):  
    c=OrderItem.objects.all().filter(userid=request.user)
    p=[]
    for i in c:
        obj=orderprodetail(i.product,i.quantity)
        p.append(obj)
        
    return render(request,'cart.html',{'products':p})