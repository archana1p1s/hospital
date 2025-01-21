from django.shortcuts import render
from .models import Department
from.models import Doctor
from.models import Booking
from . forms import BookingForm# Create your views here.
def first_page(request):
    return render(request, 'index.html')

def sec_page(request):
    return render(request, 'about.html')
def third_page(request):
    if request.method == "POST":
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
    form = BookingForm()
    dit_form={
        "form":form
    }
    return render(request, 'booking.html', dit_form) 

def fourth_page(request):
    return render(request, 'contact.html') 

def fifth_page(request):
    x = {
        'dep':Department.objects.all()
    }
    return render(request, 'department.html',x)

def sixth_page(request):
    x={
        "doc":Doctor.objects.all()
    }
    return render(request, 'doctors.html',x) 