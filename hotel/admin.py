from django.contrib import admin
from hotel.models import Hotel, Booking, Room, RoomType, ActivityLog, StaffOnDuty,HotelGallery
# Register your models here.

class HotelGalleryInline(admin.TabularInline):
    model = HotelGallery
class HotelAdmin(admin.ModelAdmin):
    inlines = [HotelGalleryInline]
    list_display = ['thumbnail','name' , 'user' ,'status' ]
    prepopulated_fields = {"slug": ("name", )}

class RoomAdmin(admin.ModelAdmin):
    model = Room
    
admin.site.register(Hotel, HotelAdmin)
admin.site.register(Booking)
admin.site.register(Room)
admin.site.register(RoomType)