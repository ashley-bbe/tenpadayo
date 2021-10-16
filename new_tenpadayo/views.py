from django.shortcuts import  render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import NewUserForm, ProductForm, WishlistForm
from .models import Product, Wishlist
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages #import messages
from django.contrib.auth.forms import AuthenticationForm
from cloudinary.forms import cl_init_js_callbacks
from django.db.models import Q
from django.contrib.auth.models import User

def start(request):
    return render(request=request, template_name='start.html')


@login_required
def home(request):
    return render(request=request, template_name='home.html')
    

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful.")
			return redirect("login")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm
	return render (request=request, template_name="register.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})


def logout_request(request):
	logout(request)
	return render(request=request, template_name="logout.html")


def routine(request):
	query = request.GET.get ('search')

	if query:
		queryset = (Q(hair_type__icontains=query))|(Q(hair_texture__icontains=query))|(Q(hair_porosity__icontains=query))
		results = Product.objects.filter(queryset).distinct()

	else:
		results = []

	return render(request, 'routine.html', {'results':results, 'query':query})



def search(request):
	query = request.GET.get('search')

	if query:
		queryset = (Q(product_type__icontains=query))|(Q(product_brand__icontains=query))
		results = Product.objects.filter(queryset).distinct()
		
	else:
		results = []
	return render(request, 'search.html', {'results':results, 'query':query})



def add_to_wishlist(request, user_id, product_id):
	product = Product.objects.get(id=product_id)
	user = User.objects.get(id=user_id)
	product_brand = product.product_brand
	product_url = product.product_url
	image = product.image
	wishlist = Wishlist()
	
	wishlist.product = product
	wishlist.userid = user
	wishlist.product_brand = product_brand
	wishlist.product_url = product_url
	wishlist.image = image
	wishlist.save()
	messages.info(request, f"The product has been added to the wishlist.")

	return HttpResponseRedirect(request.META['HTTP_REFERER'])


def wishlist(request, user_id):
    wishlist = Wishlist()
    user = User.objects.get(id=user_id)
    print(user_id)
    wishlist = Wishlist.objects.filter(userid=user_id)
	
    return render(request, 'wishlist.html', {'wishlists':wishlist, 'user':user})


def del_wishlist(request,product_id):
	product = Wishlist.objects.filter(product=product_id)
	product.delete()
	messages.info(request, f"The product has been deleted from your wishlist !")
	return HttpResponseRedirect(request.META['HTTP_REFERER'])




def add_to_wishlist_routine(request, user_id, product_id):
	product = Product.objects.get(id=product_id)
	user = User.objects.get(id=user_id)
	product_brand = product.product_brand
	product_url = product.product_url
	image = product.image
	wishlist = Wishlist()
	
	wishlist.product = product
	wishlist.userid = user
	wishlist.product_brand = product_brand
	wishlist.product_url = product_url
	wishlist.image = image
	wishlist.save()
	messages.success(request, f"The product has been added to the wishlist.")

	return HttpResponseRedirect(request.META['HTTP_REFERER'])



def product(request):
	if request.method == 'POST':
		form = ProductForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			messages.info(request, f"The product has been registered.")
		
		else:
			return HttpResponseRedirect(form.errors.as_json())
	
	product = Product.objects.all().order_by('created_at').all()
	return render(request, 'product.html/',
                  {'products': product})



def edit(request, id):
	product = Product.objects.get(id=id)
	if request.method == 'POST':
		form = ProductForm(request.POST, request.FILES, instance=product)
		if form.is_valid():
			form.save()
			messages.info(request, f"The product has been edited")
			return redirect('product')
		
		else:
			return HttpResponseRedirect(form.errors.as_json())
	
	else:
		form = ProductForm
	
	return render(request, 'edit.html', {'product':product, 'form':form} )


def delete(request, id):
	product = Product.objects.get(id=id)
	product.delete()
	messages.info(request, f"The product has been deleted")
	return redirect('product')


			
