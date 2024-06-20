from django.db import models
from django.utils.text import slugify
from django.utils.html import mark_safe
from userauths.models import User
from shortuuid.django_fields import ShortUUIDField
from django_ckeditor_5.fields import CKEditor5Field
import shortuuid
from taggit.managers import TaggableManager
HOTEL_STATUS = (
    ("Draft", "Draft"),
    ("Disable", "Disable"),
    ("Rejected", "Rejected"),
    ("In Review", "In Review"),
    ("Live", "Live"),
)

ICON_TYPE = (
    ("Bootstrap Icons", "Draft"),
    ("Fontawesome Icons", "Disable"),
    ("Box Icons", "Rejected"),
    ("Remi Icons", "Remi Icons"),
    ("Flat Icons", "Flat Icons"),
)

PAYMENT_STATUS = (
    ("paid", "Paid"),
    ("pending", "Pending"),
    ("processing", "Processing"),
    ("cancelled", "Cancelled"),
    ("initiated", "Initiated"),
    ("failed", "Failed"),
    ("refunding", "Refunding"),
    ("refunded", "Refunded"),
    ("expired", "Expired"),
)

class Hotel(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)
    name = models.CharField(max_length=100)
    description = CKEditor5Field(null=True,blank=True, config_name='extends')
    image = models.ImageField(upload_to="hotel_galley")
    address = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    status = models.CharField(max_length=20, choices=HOTEL_STATUS)
    
    tags= TaggableManager(blank = True)
    views = models.IntegerField(default=0)
    featured = models.BooleanField(default=False)
    hid = ShortUUIDField(unique=True, max_length=22, alphabet="abcdefghijklmnopqrstuvwxyz123")
    slug = models.SlugField(unique=True)
    data = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.slug == "" or self.slug == None:
            uuid_key = shortuuid.uuid()
            uniqueid = uuid_key[:4]
            self.slugs = slugify(self.name) + ' - ' + str(uniqueid.lower())
            
        super(Hotel, self).save(*args, **kwargs)
        
    def thumbnail(self):
        return mark_safe("<img src='%s' width='50' height='50' style = 'object-fit: cover; border-radius: 6px;' />" % (self.image.url))
    
    def hotel_gallery(self):
        return HotelGallery.objects.filter(hotel=self)

    
class HotelGallery(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    image = models.FileField(upload_to="hotel_gallery")
    hid = ShortUUIDField(unique=True, max_length=22, alphabet="abcdefghijklmnopqrstuvwxyz123")
    
    def __str__(self):
        return str(self.hotel.name)
    
    class Meta:
        verbose_name_plural = "Hotel Gallery"
        
        
class HotelFeature(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    icon_type = models.CharField(max_length=100, null=True, blank=True, choices=ICON_TYPE)
    icon = models.CharField(max_length=100, null=True, blank =True)
    name = models.CharField(max_length=100, null=True,blank=True)
    
    def __str__(self):
        return str(self.hotel.name)
    
    class Meta:
        verbose_name_plural = "Hotel Feature"
        
class HotelFaqs(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    question = models.CharField(max_length=1000)
    answer = models.CharField(max_length=1000, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.question)
    class Meta:
        verbose_name_plural = "Hotel Gallery"
        
class RoomType(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    type = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=12, decimal_places=2,)
    number_of_beds = models.PositiveIntegerField(default=0)
    rtid = ShortUUIDField(unique=True, max_length=22, alphabet="abcdefghijklmnopqrstuvwxyz123")
    slug = models.SlugField(unique=True)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.type} - {self.hotel.name} - {self.price}"
    
    class Meta:
        verbose_name_plural = "Room Type"
        
    def rooms_count(self):
        Room.objects.filter(room_type = self).count()
        
class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10000)
    is_avaliable = models.BooleanField(default=True)
    rid = ShortUUIDField(unique=True, max_length=22, alphabet="abcdefghijklmnopqrstuvwxyz123")
    
    def __str__(self):
        return f"{self.room_type.type} - {self.hotel.name} - {self.room_number} - {self.is_avaliable}"
    class Meta:
        verbose_name_plural = "Rooms"
        
    def price(self):
        return self.room_types.price
    
    def number_of_beds(self):
        return self.room_types.number_of_beds
    
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null = True, blank = True)
    payment_status = models.CharField(max_length= 100, choices=PAYMENT_STATUS)
    fullname = models.CharField(max_length=1000)
    email = models.EmailField(max_length=1000)
    phone = models.CharField(max_length=20)
    
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, on_delete= models.SET_NULL, null= True, blank= True)
    room = models.ManyToManyField(Room)
    before_discount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    saved = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    
    total_days = models.PositiveIntegerField(default=0)
    num_adult = models.PositiveIntegerField(default=1)
    num_chieldren = models.PositiveIntegerField(default=0)
    
    check_in = models.BooleanField(default=False)
    check_out = models.BooleanField(default=False)
    
    is_active = models.BooleanField(default=False)
    
    date = models.DateField(auto_now_add=True)
    striped_payment_intent = models.CharField(max_length=1000,null=True,blank=True)
    success_id = models.CharField(max_length=1000,null=True,blank=True)
    booking_id = ShortUUIDField(unique=True, max_length=22, alphabet="abcdefghijklmnopqrstuvwxyz123")
    
    def __str__(self):
        return f"{self.booking_id}"
    
    def rooms(self):
        return self.room.all().count()
    
class ActivityLog(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    guess_out = models.DateTimeField(auto_now_add=True)
    guess_in = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True,blank=True)
    
    def __str__(self):
        return f"{self.booking}"
    
class StaffOnDuty(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    staff_id = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.staff_id}"