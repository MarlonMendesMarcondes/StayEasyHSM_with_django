from django.contrib import admin
from hotel.models import Hotel, Booking, Room, RoomType, ActivityLog, StaffOnDuty,HotelGallery
# Register your models here.

class HotelGalleryInline(admin.TabularInline):
    model = HotelGallery
class HotelAdmin(admin.ModelAdmin):
    inlines = [HotelGalleryInline]
    list_display = ['thumbnail','name' , 'user' ,'status' ]
    prepopulated_fields = {"slug": ("name", )}
    
admin.site.register(Hotel, HotelAdmin)
admin.site.register(Booking)