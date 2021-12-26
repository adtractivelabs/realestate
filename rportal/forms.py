from django import forms
from .models import *


# EnquiryForm
class EnquiryForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "text-center p-2",
        "type": "text",
        "id": "name",
        "placeholder": "Name"
    }), error_messages={'required': 'Please enter your full name'}, required=True)

    phone = forms.CharField(widget=forms.TextInput(attrs={
        "class ": "text-center p-2",
        "type": "text",
        "id": "phone",
        "placeholder": "Phone No"
    }))

    email = forms.EmailField(widget=forms.TextInput(attrs={
        "class ": "text-center p-2",
        "type": "email",
        "id": "email",
        "placeholder": "Email Address"
    }), error_messages={'required': 'Please enter your email'}, required=True)

    class Meta:
        model = Enquiry
        fields = ['name', 'phone', 'email']

    def clean_name(self):
        name = self.cleaned_data['name']
        if name == '':
            raise forms.ValidationError("Name is Required !! ")
        return name

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if phone == '':
            raise forms.ValidationError("Phone No is Required !! ")
        if len(phone) > 10:
            raise forms.ValidationError("Enter Valid Phone Number ")
        return phone

    def clean_email(self):
        email = self.cleaned_data['email']
        if email == '':
            raise forms.ValidationError("Email is Required !! ")
        if Enquiry.objects.filter(email=email).exists():
            raise forms.ValidationError("Your Enquiry is already in process ")
        return email


# Contact Us Form
class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        "class"       : "text-center p-2",
        "type"        : "text",
        "id"          : "name",
        "placeholder" : "Name"
    }), error_messages={'required': 'Please enter your full name'}, required=True)

    phone = forms.CharField(widget=forms.TextInput(attrs={
        "class ": "text-center p-2",
        "type": "text",
        "id": "phone",
        "placeholder": "Phone No"
    }))

    email = forms.EmailField(widget=forms.TextInput(attrs={
        "class ": "text-center p-2",
        "type"  : "email",
        "id"    : "email",
        "placeholder": "Email Address"
    }), error_messages={'required': 'Please enter your email'}, required=True)

    purpose = forms.CharField(widget=forms.TextInput(attrs={
        "class ": "text-center p-2",
        "type": "text",
        "id": "purpose",
        "placeholder": "Purpose of Subject"
    }))

    message = forms.CharField(widget=forms.TextInput(attrs={
        "class ": "text-left p-4",
        "type": "text",
        "id": "message",
        "placeholder": "Message"
    }))

    class Meta:
        model = Contact_Us
        fields = ['name', 'phone', 'email', 'purpose', 'message']

    def clean_name(self):
        name = self.cleaned_data['name']
        if name == '':
            raise forms.ValidationError("Name is Required !! ")
        return name

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if phone == '':
            raise forms.ValidationError("Phone No is Required !! ")
        if len(phone) > 10:
            raise forms.ValidationError("Enter Valid Phone Number ")
        return phone

    def clean_email(self):
        email = self.cleaned_data['email']
        if email == '':
            raise forms.ValidationError("Email is Required !! ")
        if Contact_Us.objects.filter(email=self.email).exists():
            raise forms.ValidationError("Your Request is already in process ")
        return email

    def clean_purpose(self):
        purpose = self.cleaned_data['purpose']
        if purpose == '':
            raise forms.ValidationError("Purpose is Required !! ")
        return purpose

    def clean_message(self):
        message = self.cleaned_data['message']
        if message == '':
            raise forms.ValidationError("Message is Required !! ")
        return message

