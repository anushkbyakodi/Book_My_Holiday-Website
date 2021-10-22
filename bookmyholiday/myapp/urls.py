from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),

    #path('', views.home, name="home"),

	path('', views.home, name='home'),
    path('beaches/', views.beaches, name='catalog-beaches'),
    path('hillstations/', views.hillstations, name='catalog-hillstations'),
    path('heritage_sites/', views.heritagesites, name='catalog-heritagesites'),

    path("display_heritage/",views.display_heritage,name='display_heritage'),
    url(r'^heritages$', views.display_heritage, name="display_heritage"),
    url(r'^details$', views.details, name="details"),
    #url(r'^display_heritage/<str:pk>$', views.newheritage, name="newheritage"),
    #url(r'^add_customer$', views.newheritage, name="catalog-form"),
    
    path('places/<str:place>', views.newheritage, name='catalog-form'),



]