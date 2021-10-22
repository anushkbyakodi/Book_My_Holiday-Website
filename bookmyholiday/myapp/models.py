from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import datetime

# Create your models here.
class Place(models.Model):
    PLACE_TYPE = (
        ('beach','BEACH'),
        ('hill','HILL STATION'),
        ('heritage','HERITAGE SITE'),
    )
    place = models.CharField(max_length=100,verbose_name='Name of the Place',primary_key=True,help_text='Add the name of the place')
    type = models.TextField(max_length=10,
        choices=PLACE_TYPE,
        blank=False,
        verbose_name='Location Type')
    description = models.TextField(max_length=500, verbose_name='Description of the Place',help_text='Add 50 words escription about the place')
    location = models.CharField(max_length=50)
    url = models.URLField(max_length=100,verbose_name="Image Url",help_text="Add url of the image to be displayed")

    def __str__(self):
        """String for representing the Model object."""
        return(self.place)
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('place-detail', args=[str(self.place)])




class Room_type(models.Model):
    room_type = models.CharField(max_length=10,primary_key=True,verbose_name='Room Type')
    description = models.TextField(max_length=500,verbose_name='Room Description',help_text='Enter Description about the Room')
    child_price = models.IntegerField(verbose_name='price per child')
    adult_price = models.IntegerField(verbose_name='Price per adult')

    def __str__(self):
        """String for representing the Model object."""
        return(self.room_type)




class Cab_type(models.Model):
    cab_type = models.CharField(max_length=30,primary_key=True,verbose_name='Cab Model')
    cab_price = models.IntegerField(verbose_name='Price per day')

    def __str__(self):
        """String for representing the Model object."""
        return(self.cab_type)



class Customer(models.Model):
    
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.ForeignKey(Place,on_delete=models.CASCADE,null=True,verbose_name='Select Places')
    room_type = models.ForeignKey(Room_type,on_delete=models.CASCADE,verbose_name=' Select Room Type')
    no_of_children = models.IntegerField(verbose_name='No of Children')
    no_of_Adults = models.IntegerField(verbose_name='No of Adults')
    start_date = models.DateField(verbose_name="Check in Date")
    end_date = models.DateField(verbose_name="Check out Date")
    breakfast_included = models.BooleanField(verbose_name="Breakfast included",help_text='check if you want breakfast')
    cab_type = models.ForeignKey(Cab_type,on_delete=models.CASCADE,verbose_name="Select Cab Type")
    Total_price = models.IntegerField(verbose_name="Price of the total package")

    class Meta:
        unique_together = [['place', 'room_type', 'start_date', 'end_date']]

    def __str__(self):
        return (str(self.customer))

    
    def date_time_error(self):
        start=self.start_date
        end=self.end_date
        if (start < end):
            return "Check out date cannot be greater than check in date"
        else:
            return "looks good"

    def get_absolute_url(self):
        return reverse('Customer-detail', args=[str(self.customer)])





    










