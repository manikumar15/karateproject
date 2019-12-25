from django import forms
from .models import Enquiry


class Enquiryform(forms.ModelForm):
    class Meta:
        model=Enquiry
        fields = "__all__"