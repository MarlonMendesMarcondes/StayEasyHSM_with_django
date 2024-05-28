from django.db import models
from django.utils.text import slugify
from django.utils.html import mark_safe
import shortuuid
from userauths.models import User
from shortuuid.django_fields import ShortUUIDField
HOTEL_STATUS = (
    ("Draft", "Draft"),
    ("Disable", "Disable"),
    ("Rejected", "Rejected"),
    ("In Review", "Draft"),
    ("Live", "Live"),
)

class Hotel(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)
    name = models.CharField(max_length=100)
    description = models.TextField( null=True,blank=True)
    image = models.ImageField(upload_to="hotel_galley")
    address = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    status = models.CharField(max_length=20, choices=HOTEL_STATUS)
    
    tags= models.CharField(max_length=200, help_text= "Separed tags with commas")
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
