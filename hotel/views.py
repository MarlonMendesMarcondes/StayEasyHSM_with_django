from django.shortcuts import render

from hotel.models import Hotel, Booking, Room, RoomType, ActivityLog, StaffOnDuty

def index(request):
    hotels = Hotel.objects.filter(status = 'Live')
    context = {
        "hotels":hotels
    }
    return render(request, 'hotel/hotel.html', context)

def hotel_detail(request, slug):
    hotel = Hotel.objects.get(status = "Live", slug = slug)
    context = {
        "hotel": hotel,
    }
    return render(request, 'hotel/hotel_detail.html', context)