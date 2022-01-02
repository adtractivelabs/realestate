from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
def home(request):
    builder_logos = Builder.objects.all()
    about_us      = AboutUs.objects.all()
    banner_vedio  = BannerVideo.objects.all()
    testomonials  = Testimonials.objects.filter().order_by('-id')
    properties    = Property.objects.filter(is_exclusive=True).order_by('-id')[:4]
    enquiry_form  = EnquiryForm()

    return render(request, 'pages/home.html',
                  {'builder_logos': builder_logos, 'about_us': about_us, 'banner_vedio': banner_vedio,
                   'testomonials': testomonials, 'properties': properties, 'enquiry_form': enquiry_form,
                   'title': 'Home'})


def about_us(request):
    about_us = AboutUs.objects.filter()
    about_list = []
    if about_us:
        temp_about = {}
        for about in about_us:
            temp_about['about_logo'] = about.about_logo
            temp_about['about_description'] = about.site_description
            temp_about['about_vision'] = about.vision_text
            temp_about['about_mission'] = about.mission_text
            temp_about['about_philosophy'] = about.philosophy_text
            temp_about['about_video_link'] = about.about_video_link
            about_list.append(temp_about)
    return render(request, 'pages/about_us.html', {'about_list': about_list, 'title': 'About-Us'})


def contact_us(request):
    about_us = AboutUs.objects.all()
    if request.method == 'POST':
        contact_us_form = ContactForm(data=request.POST)
        if contact_us_form.is_valid():
            contact_us_form.save()
            messages.success(request, 'Thanks for Reaching Out to us. We Will Soon get back to you')
            return render(request, 'pages/contact_us.html',
                          {'contact_form': contact_us_form, 'about_us': about_us, 'title': 'Contact Us'})
    else:
        contact_us_form = ContactForm()
    return render(request, 'pages/contact_us.html',
                  {'contact_form': contact_us_form, 'about_us': about_us, 'title': 'Contact Us'})


def enquiry_property(request):
    if request.method == 'POST':
        enquiry_form = EnquiryForm(data=request.POST)
        if enquiry_form.is_valid():
            enquiry_form.save()
            enquiry_form = EnquiryForm()
            return render(request, 'pages/home.html', {'enquiry_form': enquiry_form})
    else:
        enquiry_form = EnquiryForm()
    return render(request, 'pages/home.html', {'enquiry_form': enquiry_form, 'title': 'Enquiry-Form'})


def property_list_builder(request,property_type=None):
    if property_type == 'private':
        builders           = Builder.objects.all()
        private_properties = Property.objects.filter(builder_type__in=list(builders),property_type = property_type)
        return render(request, 'properties/property_types/residential_properties.html',{'private_property': private_properties, 'title': 'Builder Listed Properties'})
    elif property_type== 'commercial':
        builders = Builder.objects.all()
        commercial_properties = Property.objects.filter(builder_type__in=list(builders), property_type=property_type)
        return render(request, 'properties/property_types/commercial_properties.html',{'commercial_property': commercial_properties, 'title': 'Builder Listed Properties'})
    else:
        builders = Builder.objects.all()
        property_list_builder = Property.objects.filter(builder_type__in=list(builders))
        return render(request, 'properties/property_by_builder.html',{'builders': builders, 'property': property_list_builder, 'title': 'Builder Listed Properties'})


def news_letter(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            if NewsLetter.objects.filter(email=email).exists():
                messages.success(request, 'You Already Subscribed')
                return redirect('rportal:property_list_builder',property_type = 'all')
            else:
                email_news = NewsLetter()
                email_news.email = email
                email_news.save()
                messages.success(request, 'Subscription Successful')
                return redirect('rportal:property_list_builder',property_type = 'all')
        else:
            messages.error(request, 'Enter The Valid Mail')
            return redirect('rportal:property_list_builder',property_type = 'all')
    else:
        return redirect('rportal:property_list_builder',property_type = 'all')


def builder_listed_properties(request, builder_name):
    property_list_builder = Property.objects.filter(builder_type__builder_slug=builder_name)
    return render(request, 'properties/all_property_by_builder.html',{'property': property_list_builder, 'title': 'Builder All Listed Properties'})


def property_details(request, builder_name, property_name):
    property_list_builder = Property.objects.filter(property_slug=property_name)
    related_property_list = Property.objects.filter(builder_type__builder_slug=builder_name).exclude(property_name=property_list_builder[0].property_name)
    properties_images     = PropertiesImages.objects.filter(property_name__property_slug = property_list_builder[0].property_slug )
    return render(request, 'properties/property_details.html',{'title': 'Property Details Listings', 'property_details': property_list_builder,'property_list': related_property_list ,'properties_images':properties_images})


def enquire_now_lead(request):
    property_list_builder = Property.objects.filter(is_exclusive=True)
    location_name = Location.objects.all()
    if request.method == 'POST':
        name     = request.POST.get('name')
        email    = request.POST.get('email')
        phone    = request.POST.get('phone')
        location = request.POST.get('location_name')
        builder  = request.POST.get('loc_project')
        property = request.POST.get('loc_property')

        if name and email and phone and location and builder and property:
            lead_form = Lead()
            lead_form.name  = name
            lead_form.phone = phone
            lead_form.email = email
            lead_form.location_name = Location.objects.get(id = location)
            lead_form.property_name = Property.objects.get(id = property)
            lead_form.project_name  = Builder.objects.get(id  = builder)
            lead_form.property_unit_price = ''
            lead_form.save()
            message_code = messages.success(request, 'Thanks for Filling the Form')
            return render(request, 'properties/lead_generation.html',{'property_list_builder': property_list_builder, 'location_name': location_name,'message_code':message_code})
        else:
            message_code = messages.success(request, 'Something Went Wrong !')
            return render(request, 'properties/lead_generation.html',{'property_list_builder': property_list_builder, 'location_name': location_name,'message_code':message_code})
    else:
        return render(request, 'properties/lead_generation.html',{'property_list_builder': property_list_builder, 'location_name': location_name})


def load_builder(request):
    if request.method == "GET":
        try:
            builder_list = Builder.objects.filter(builder_location__location_name=request.GET['location_value'])
        except Exception:
            data = {}
            data['error_message'] = 'error'
            return JsonResponse(data)
        return JsonResponse(list(builder_list.values('id', 'builder_name')), safe=False)


def load_builder_properties(request):
    if request.method == "GET":
        try:
            builder_property_list = Property.objects.filter(builder_type__builder_name=request.GET['builder_name'])
        except Exception:
            data = {}
            data['error_message'] = 'error'
            return JsonResponse(data)
        return JsonResponse(list(builder_property_list.values('id', 'property_name')), safe=False)