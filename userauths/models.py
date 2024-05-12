from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from shortuuid.django_fields import ShortUUIDField
# Create your models here.

GENDER = (
    ("Feminino", "Feminino"),
    ("Masculino", "Masculino"),
    ("Outros", "Outros"),
)
IDENTIFY_TYPE = (
    ("CPF", "CPF"),
    ("Carteira de Motorista", "Carteira de Motorista"),
    ("Passaporte", "Passaporte"),
)

def user_directory_path(instance, filename):
    ext = filename.split(".")[-1]
    filename = "%s.%s" % (instance.user.id, filename)
    return "user_{0}/{1}".format(instance.user.id, filename)

class User(AbstractUser):
    full_name = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255, unique = True)
    email = models.EmailField(max_length=255, unique = True)
    phone = models.CharField(max_length=30, null = True, blank = True)
    gender = models.CharField(max_length=20, choices=GENDER, default="Outros")
    
    otp = models.CharField(max_length=100,null = True, blank = True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    def __self__(self):
        return self.full_name

class Profile(models.Model):
    pid = ShortUUIDField(max_length=25, alphabet="abcdefghijklmnopqrstuvwxyz123")
    image = models.FileField(upload_to=user_directory_path, default="default.jpg", null = True, blank = True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255, unique = True)
    email = models.EmailField(max_length=255, unique = True)
    phone = models.CharField(max_length=30, null = True, blank = True)
    gender = models.CharField(max_length=20, choices=GENDER, default="Outros")
    country = models.CharField(max_length=100, null = True, blank = True)
    city = models.CharField(max_length=100, null = True, blank = True)
    state = models.CharField(max_length=100, null = True, blank = True)
    address = models.CharField(max_length=100, null = True, blank = True)
    
    identify_type = models.CharField(max_length=200, choices=IDENTIFY_TYPE, null = True, blank = True)
    identify_image = models.FileField(upload_to=user_directory_path, default="id.jpg", null = True, blank = True)
    
    facebook = models.URLField(null = True, blank = True)
    twitter = models.URLField(null = True, blank = True)
    
    wallet = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    verified = models.BooleanField(default=False)
    
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date']
        
    def __self__(self):
        if self.fullname:
            return f"{self.full_name}"
        else:
            return f"{self.user.username}"
        
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    
post_save.connect(create_user_profile,sender=User)
post_save.connect(save_user_profile,sender=User)