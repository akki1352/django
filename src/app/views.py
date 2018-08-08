from django.shortcuts import render,redirect,render_to_response
from django.http import *
from app.models import Product,Register, NCart
from django.views.generic import TemplateView
from app.forms import userRegister,userLogin
from django.contrib.auth import authenticate, get_user_model, login, logout

def index(request):
  	data = Product.objects.all()
  	return render(request, 'home.html',{'data': data})

def login_view(request):
	print(request.user.is_authenticated)
	form = userLogin(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		#user = form.save(commit=False)
		user = authenticate(username=username,password=password)
		login(request,user)
		print(request.user.is_authenticated)
		return redirect('/')

	return render(request,'login.html',{'form':form}) 

def logout_view(request):
	logout(request)
	data = Product.objects.all()
	return render(request, 'home.html',{'data': data})

def register(request):
	print(request.user.is_authenticated)
	form = userRegister(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		name = form.cleaned_data.get('fullname')
		email = form.cleaned_data.get('email')
		password = form.cleaned_data.get('password')
		phone = form.cleaned_data.get('phone')
		#user.set_password(password)
		user.save()

		new_user = authenticate(fullname = user.fullname,password = user.password)
		login(request,new_user)
		print(request.user.is_authenticated)
		return redirect('/')

	return render(request,'reg_form.html',{'form':form})

def contact(request):
	return render(request, 'contact.html', {})

def about(request):
	return render(request, 'about.html', {})

def cart(request):
	username = None
	if request.user.is_authenticated:
		id = request.GET.get('id')
		username = request.user.username
		pro = Product.objects.get(id=id)
		pname = pro.product
		pprice = pro.price
		qty = 1
		email="akash.1998777@gmail.com"
		print(pname)
		print(pprice)
		print(qty)

		cart_values = NCart(email=email,bookId=id,bookName=username,product=pname,price=pprice,Quantity=qty)
		cart_values.save()
	
	return render(request, 'cart.html', {'uname':username, 'id':id, 'nm':pname})
	

def viewcart(request):
	username = None
	if request.user.is_authenticated:
		id = request.GET.get('id')
		username = request.user.username
		pro = NCart.objects.all()
		
	return render(request, 'cart.html', {'data': pro, 'uname':username})

