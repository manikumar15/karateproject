  
from django.shortcuts import render

from django.http.response import HttpResponse

from .models import Enquiry
from .forms import Enquiryform


def index(request):
    return render(request, 'index.html')

def Enquiryview(request):
    if request.method == "POST":
        fform=Enquiryform(request.POST)
        if fform.is_valid():
            name=request.POST.get('name')
            email=request.POST.get('email')
            message=request.POST.get('message')

            data=Enquiry(
                name=name,
                email=email,
                message=message,
                )
            data.save()
            fform=Enquiryform()
            fdata = Enquiry.objects.all()
            return render(request,'index.html',{'fform': fform,'fdata': fdata})
        else:
            return HttpResponse('Invalid User Data')
    else:
        fform = Enquiryform()
        fdata = Enquiry.objects.all()
    return render(request, 'index.html',{'fform': fform,'fdata': fdata})