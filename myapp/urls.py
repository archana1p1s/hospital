from django.urls import path
from . import views

urlpatterns = [
    path('', views.first_page, name='home'),
    path('about', views.sec_page, name='about'),
    path('booking', views.third_page, name='booking'),
    path('contact', views.fourth_page, name='contact'),
    path('department', views.fifth_page, name='department'),
    path('doctors', views.sixth_page, name='doctors')
]