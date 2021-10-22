from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from .models import *
from .forms import  *

# Create your views here.
from .models import *
from .forms import  CreateUserForm


def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('/login')
			

		context = {'form':form}
		return render(request, 'myapp/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'myapp/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')


@login_required(login_url='login')
def home(request):
	return render(request, 'myapp/base.html')


@login_required(login_url='login')
def beaches(request):
    beaches = Place.objects.all()
    context = {
        'beaches' : beaches,
    }
    return render(request,'myapp/beach.html',context)


@login_required(login_url='login')
def hillstations(request):
    return render(request, 'myapp/hill.html')

@login_required(login_url='login')
def heritagesites(request):
    return render(request, 'myapp/heritage.html')

def error_404_view(request, exception):
    data = {"name": "BOOK MY HOLIDAY"}
    return django.views.defaults.page_not_found(request, 'myapp/404_error.html')

def catalogFormView(request,place):
    form = Customer.objects.all()
    context = {
        'forms': form,
        'place': place,
    }
    return render(request, 'myapp/customerform.html', context)

@login_required(login_url='/login')
def display_heritage(request):
    items = Place.objects.filter(type="heritage")
    context = {
        'items': items,
        'header': 'HERITAGE SITE',
    }
    return render(request, 'myapp/newheritage.html', context)


def details(request, cls):
    if request.method == "POST":
        form = cls(request.POST)
#'customer','place','room_type','no_of_children','no_of_Adults','start_date','end_date','breakfast_included','cab_type','Total_price'
        if form.is_valid():
            #form.save()
            customer=form.cleaned_data['customer']
            place=form.cleaned_data['place']
            room_type=form.cleaned_data['room_type']
            no_of_children=form.cleaned_data['no_of_children']
            no_of_Adults=form.cleaned_data['no_of_Adults']
            start_date=form.cleaned_data['start_date']
            end_date=form.cleaned_data['end_date']
            breakfast_included=form.cleaned_data['breakfast_included']
            cab_type=form.cleaned_data['cab_type']
            Total_price=form.cleaned_data['Total_price']
            value=Customer.objects.create(customer=customer,place=place,room_type=room_type,no_of_children=no_of_children, no_of_Adults=no_of_Adults, start_date=start_date, end_date=end_date,breakfast_included=breakfast_included,cab_type=cab_type,Total_price=Total_price)
            value.save()
            return redirect('display_heritage')

    else:
        form = cls()
        return render(request, 'myapp/customerform.html', {'form' : form})


def newheritage(request, place):
    return details(request, CatalogForm)



