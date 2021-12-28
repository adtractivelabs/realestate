from .views import  *
from django.urls import path,re_path

app_name = 'rportal'

urlpatterns = [
    path('',home,name='home'),
    path('about-us/',about_us,name='about_us'),
    path('contact-us/',contact_us,name='contact_us'),
    path('builders/<str:property_type>/',property_list_builder,name='property_list_builder'),

    path('builders-properties/<str:builder_name>/',builder_listed_properties,name='builder_listed_properties'),
    path('builder/<str:builder_name>/<str:property_name>/',property_details,name='property_details'),

    path('enquiry-property/',enquiry_property,name='enquiry_property'),
    path('news-letter/',news_letter,name='news_letter'),
    path('enquire-now/',enquire_now_lead,name='enquire_now'),

    path('load-builder/',load_builder,name = 'load_builder'),
    path('load-builder-properties/',load_builder_properties,name = 'load_builder_properties'),

]