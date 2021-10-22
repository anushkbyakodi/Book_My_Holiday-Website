from django.contrib import admin
from .models import Place,Customer,Cab_type,Room_type
from . import views

# Register your models here.
class PlacesInstanceAdmin(admin.ModelAdmin):
    list_filter=('place','location','type')

'''class CustomerInstaceAdmin(admin.ModelAdmin):
    list_filter=('customer','room_type','start_date')'''



admin.site.register(Place,PlacesInstanceAdmin)
admin.site.register(Customer)
admin.site.register(Cab_type)
admin.site.register(Room_type)