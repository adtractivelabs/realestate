from django.contrib import admin
from django.contrib.auth.models import Group

from rportal.models import *

# Role Admin View
class RoleAdmin(admin.ModelAdmin):
    list_display = ['role_name','create_date','update_date']


# User Admin View
class UserAdmin(admin.ModelAdmin):
    list_display = ['username','email','first_name','last_name',
                    'mobile_number','created_at','updated_at']


# Approved Bank Admin View
class ApprovedBankAdmin(admin.ModelAdmin):
    list_display = ['bank_name','bank_logo','created_at','updated_at']


# Banner Admin View
class BannerAdmin(admin.ModelAdmin):
    list_display = ['video_file','video_name','created_at','updated_at']

# Testimonials Admin View
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ['testo_name','testo_client_image','testo_email',
                    'testo_phone','created_at','updated_at']


# Enquiry Admin View
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ['name','phone','email','created_at','updated_at']


# Contact Admin View
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','phone','email','purpose','created_at','updated_at']


# About Us Admin View
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['id','site_description','vision_text','mission_text','created_at','updated_at']


# Builder Admin View
class BuilderAdmin(admin.ModelAdmin):
    list_display = ['builder_name','builder_logo','builder_location','created_at','updated_at']
    prepopulated_fields = {'builder_slug': ('builder_name',), }

# Location Admin View
class LocationAdmin(admin.ModelAdmin):
    list_display = ['location_name','location_area','location_pincode',
                    'created_at','updated_at']


# Amenities Admin View
class AmenitiesAdmin(admin.ModelAdmin):
    list_display = ['amenities_name','amenities_charge','created_at','updated_at']

# Bhk/Apartment Admin View
class BHKApartmentAdmin(admin.ModelAdmin):
    list_display = ['bhk_name','created_at','updated_at']


# Property Admin View
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['builder_type','property_name','property_location',
                    'property_floor','property_type','property_price',
                    'is_exclusive','created_at','updated_at']

    prepopulated_fields = {'property_slug': ('property_name',), }


# Properties Images Admin View
class PropertiesImagesAdmin(admin.ModelAdmin):
    list_display = ['property_name','created_at', 'updated_at']

# NewsLetters Admin View
class NewsLettersAdmin(admin.ModelAdmin):
    list_display = ['email','created_at','updated_at']


# Email NewsLetter Updater
class EmailsUpdaterAdmin(admin.ModelAdmin):
    list_display = ['title_update','created_at','updated_at']

admin.site.unregister(Group)
admin.site.register(Role, RoleAdmin)

admin.site.register(User,UserAdmin)
admin.site.register(ApprovedBank,ApprovedBankAdmin)
admin.site.register(Testimonials,TestimonialsAdmin)
admin.site.register(Enquiry,EnquiryAdmin)
admin.site.register(Contact_Us,ContactAdmin)

admin.site.register(AboutUs,AboutUsAdmin)
admin.site.register(Builder,BuilderAdmin)
admin.site.register(Location,LocationAdmin)
admin.site.register(Amenities,AmenitiesAdmin)

admin.site.register(BHKApartment,BHKApartmentAdmin)
admin.site.register(Property,PropertyAdmin)
admin.site.register(PropertiesImages,PropertiesImagesAdmin)
admin.site.register(BannerVideo,BannerAdmin)

admin.site.register(NewsLetter,NewsLettersAdmin)
admin.site.register(EmailNewsletter,EmailsUpdaterAdmin)
admin.site.register(Lead)

