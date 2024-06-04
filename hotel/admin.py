from django.contrib import admin
from hotel.models import Hotel, Booking, StaffOnDuty, Room, RoomType
# Register your models here.

class HotelAdmin(admin.ModelAdmin):
    list_display = ['thumbnail','name' , 'user' ,'status' ]
    prepopulated_fields = {"slug": ("name", )}
    
admin.site.register(Hotel, HotelAdmin)
admin.site.register(Booking)