from django.contrib import admin

from .models import Department
from.models import Doctor
from.models import Booking

# Register your models here.
admin.site.register(Department)
admin.site.register(Doctor)

class BookingAdmin(admin.ModelAdmin):
    list_display=("id","patient_name","patient_number","patient_email","doc_name","booking_date","booked_on")

admin.site.register(Booking,BookingAdmin)
