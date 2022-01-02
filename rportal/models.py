from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, BaseUserManager, Permission, AbstractUser)
from datetime import datetime
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from ckeditor_uploader.fields import RichTextUploadingField

from rstate.settings import EMAIL_HOST_USER


# Base Model Structure
class BaseModel(models.Model):
    last_updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_on   = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        abstract = True


# Role Model Structure
class Role(models.Model):
    role_name       = models.CharField(max_length=250)
    create_date     = models.DateTimeField(default=datetime.now)
    update_date     = models.DateTimeField(auto_now=True)
    role_permission = models.ManyToManyField(Permission)

    def __str__(self):
        return self.role_name

    class Meta:
        verbose_name_plural = 'Roles'


# Base User Model Structure
class CustomeUser(BaseUserManager):
    def create_user(self, first_name, last_name, email, username, password):
        if not email:
            raise ValueError("Users must have an email address !!")
        if not username:
            raise ValueError("Users must have a username")

        user = self.model(
            first_name  =   first_name,
            last_name   =   last_name,
            email       =   email,
            username    =   username,
            password    =   password,
            is_active   =   True
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
            email       =   email,
            username    =   username,
            password    =   password,
            first_name  =   first_name,
            last_name   =   last_name,

        )
        user.is_superuser   = True
        user.is_verified    = True
        user.is_active      = True
        user.is_staff       = True
        user.save(using=self._db)
        return user


# User Model Structure
class User(AbstractUser, PermissionsMixin):
    role        = models.ManyToManyField(Role, related_name='user_role')
    username    = models.CharField(max_length=255, unique=True, db_index=True)
    email       = models.EmailField(max_length=255, unique=True)
    password    = models.CharField(max_length=255, unique=True, db_index=True)
    first_name  = models.CharField(max_length=30, blank=True)
    last_name   = models.CharField(max_length=150, blank=True)

    mobile_number = models.CharField(max_length=12)
    profile_image = models.ImageField(upload_to='profile/', default='img/profile.png')

    is_verified  = models.BooleanField(default=False)
    is_active    = models.BooleanField(default=True)
    is_staff     = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    object = CustomeUser()

    USERNAME_FIELD  = 'username'
    EMAIL_FIELD     = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'User'


# Approved Bank Model Structure
class ApprovedBank(models.Model):
    bank_logo  = models.ImageField(upload_to='bank_name', null=True)
    bank_name  = models.CharField(max_length=250, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.bank_name

    class Meta:
        verbose_name_plural = 'Approved Bank'


# Banner Home Model Structure
class BannerVideo(models.Model):
    video_file = models.FileField(upload_to='bank_name')
    video_name = models.CharField(max_length=250, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.video_name

    class Meta:
        verbose_name_plural = 'Banner Video'


# Location Model Structure
class Location(models.Model):
    location_name    = models.CharField(max_length=250, null=True, blank=True)
    location_area    = models.CharField(max_length=250, null=True, blank=True)
    location_pincode = models.CharField(max_length=6, null=True, blank=True)
    created_at       = models.DateTimeField(auto_now_add=True)
    updated_at       = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.location_name

    class Meta:
        verbose_name_plural = 'Location'


# Testimonials Model Structure
class Testimonials(models.Model):
    testo_client_image  = models.ImageField(upload_to='testo/', null=True, blank=True)
    testo_name          = models.CharField(max_length=250, null=True, blank=True)
    testo_email         = models.CharField(max_length=30, null=True)
    testo_phone         = models.CharField(max_length=15, null=True)
    testo_desc          = models.TextField(null=True)
    testo_locations     = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.testo_name

    class Meta:
        verbose_name_plural = 'Testimonials'


# Enquiry Form Model Structure
class Enquiry(models.Model):
    name            = models.CharField(max_length=256, null=True, blank=True)
    phone           = models.CharField(max_length=10, null=True, blank=True)
    email           = models.EmailField(max_length=25, unique=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Enquiries'


# Contact us Model Structure
class Contact_Us(models.Model):
    name            = models.CharField(max_length=256, null=True, blank=True)
    phone           = models.CharField(max_length=10, null=True, blank=True)
    email           = models.EmailField(max_length=25, unique=True)
    purpose         = models.CharField(max_length=300, null=True, blank=True)
    message         = models.TextField()
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Contact Us'


#  About us Model Structure
class AboutUs(models.Model):
    about_logo          = models.ImageField(upload_to='about_logo/', null=True, blank=True)
    site_description    = models.TextField(max_length=1350)

    vision_text         = models.TextField(max_length=1350)
    mission_text        = models.TextField(max_length=1350)
    philosophy_text     = models.TextField(max_length=1350)
    about_video_link    = models.FileField()

    about_phone_no      = models.CharField(max_length=10, null=True, blank=True)
    about_email         = models.EmailField(max_length=30, null=True, blank=True)

    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)

    contact_page_text   = models.TextField()
    home_page_text      = models.TextField()

    def __str__(self):
        return self.site_description

    class Meta:
        verbose_name_plural = 'About Us'


# Builder Model Structure
class Builder(models.Model):
    builder_name        = models.CharField(max_length=250, null=True, blank=True)
    builder_slug        = models.SlugField()
    builder_logo        = models.ImageField(upload_to='builder_logo/')
    builder_location    = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.builder_name

    class Meta:
        verbose_name_plural = 'Builder'


# Amenities Model Structure
class Amenities(models.Model):
    amenities_name   = models.CharField(max_length=250, null=True, blank=True)
    amenities_charge = models.IntegerField(null=True, blank=True)
    created_at       = models.DateTimeField(auto_now_add=True)
    updated_at       = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.amenities_name

    class Meta:
        verbose_name_plural = 'Amenities'


#  BHK and Apartment Model Structure
class BHKApartment(models.Model):
    bhk_name   = models.CharField(max_length=250, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.bhk_name

    class Meta:
        verbose_name_plural = 'BHK/Apartments'


# Property Model structure
class Property(models.Model):
    PROPERTY_TYPE = [
        ('commercial', 'COMMERCIAL'),
        ('private', 'PRIVATE'),
    ]

    PROPERTY_CONSTRUCTION_TYPE = [
        ('under_construction', 'UNDER CONSTRUCTION'),
        ('compeleted', 'COMPLETED'),
        ('developing', 'DEVELOPING'),
    ]

    builder_type                = models.ForeignKey(Builder, on_delete=models.CASCADE, null=True, blank=True,related_name='builder_properties')
    property_name               = models.CharField(max_length=250, null=True, blank=True)
    property_location           = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    property_amenities          = models.ManyToManyField(Amenities, blank=True)
    property_image              = models.ImageField(upload_to='properties_images/')
    property_bhk                = models.ForeignKey(BHKApartment, on_delete=models.CharField, null=True, blank=True)
    property_floor              = models.IntegerField(default=1)
    property_type               = models.CharField(max_length=75, choices=PROPERTY_TYPE, null=True, blank=True)
    property_construction       = models.CharField(max_length=75, choices=PROPERTY_CONSTRUCTION_TYPE, null=True, blank=True)
    property_area_sq_ft         = models.CharField(max_length=250, null=True, blank=True)

    property_description        = RichTextUploadingField()
    property_slug               = models.SlugField()
    property_price              = models.CharField(max_length=250, null=True, blank=True)
    is_exclusive                = models.BooleanField(default=False)
    created_at                  = models.DateTimeField(auto_now_add=True)
    updated_at                  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.property_name

    class Meta:
        verbose_name_plural = 'Property Listing'


# Property Images Model structure
class PropertiesImages(models.Model):
    # builder_name   = models.ForeignKey(Builder,null=True,blank=True,on_delete=models.CASCADE)
    property_name  = models.ForeignKey(Property,null=True,blank=True,on_delete=models.CASCADE)
    property_image = models.ImageField(upload_to='properties_collective_images/',null=True)
    created_at     = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.property_name.property_name)

    class Meta:
        verbose_name_plural = 'Property Images'


# NewsLetter Model Structure
class NewsLetter(models.Model):
    email       = models.EmailField(max_length=30, unique=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = 'News Letters'


# EmailNewsletter Model Structure
class EmailNewsletter(models.Model):
    title_update    = models.CharField(max_length=250, null=True, blank=True)
    subject         = models.CharField(max_length=250, null=True, blank=True)
    message         = models.TextField()
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.subject and self.message and EMAIL_HOST_USER:
            for s in NewsLetter.objects.all():
                try:
                    send_mail(self.subject, self.message, EMAIL_HOST_USER, [str(s.email)], fail_silently=True)
                    super(EmailNewsletter, self).save(*args, **kwargs)
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')

    def __str__(self):
        return self.title_update

    class Meta:
        verbose_name_plural = 'Email Update'


# Lead Model Structure
class Lead(models.Model):
    name                = models.CharField(max_length=260, null=True, blank=True)
    phone               = models.CharField(max_length=260, null=True, blank=True)
    email               = models.EmailField(max_length=260, null=True, blank=True)

    location_name       = models.ForeignKey(Location,max_length=260, null=True, blank=True,on_delete=models.CASCADE)
    project_name        = models.ForeignKey(Builder,max_length=260, null=True, blank=True,on_delete=models.CASCADE)
    property_name       = models.ForeignKey(Property,max_length=260, null=True, blank=True,on_delete=models.CASCADE)

    property_plan_to_by = models.DateTimeField(null=True,blank=True)
    property_unit_price = models.CharField(max_length=260, null=True, blank=True)
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.location_name.location_name)

    class Meta:
        verbose_name_plural = 'Lead Genration'