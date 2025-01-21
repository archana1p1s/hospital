from django.db import models

# Create your models here.
class Department(models.Model):
    dep_name = models.CharField(max_length=100)
    dep_description = models.TextField()

    def __str__(self):
        return self.dep_name
    
    
class Doctor(models.Model):
    doc_name=models.CharField(max_length=100)
    doc_spec=models.TextField(max_length=200)
    dep_name=models.ForeignKey(Department ,on_delete=models.CASCADE)
    doc_image=models.ImageField(upload_to="doctors",blank=True, null=True)

    def __str__(self):
        return f'Dr{self.doc_name}[{self.dep_name}]'
    
class Booking(models.Model):
    patient_name=models.CharField(max_length=150)   
    patient_number=models.CharField(max_length=10)
    patient_email=models.EmailField()
    doc_name=models.ForeignKey(Doctor, on_delete=models.CASCADE)
    booking_date=models.DateField(blank=True, null=True)
    booked_on=models.DateField(auto_now=True) 
