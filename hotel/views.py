from django.shortcuts import render

from hotel.models import Hotel, Booking, Room, RoomType, ActivityLog, StaffOnDuty

def index(request):
    hotels = Hotel.objects.filter(status = 'Live')
    context = {
        "hotels":hotels
    }
    return render(request, 'hotel/hotel.html', context)
