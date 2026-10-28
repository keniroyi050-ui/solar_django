
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('error/', views.error, name='error'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('feature/', views.feature, name='feature'),
    path('PHOTOCREDIT/', views.PHOTOCREDIT, name='PHOTOCREDIT'),
    path('project/', views.project, name='project'),
    path('quote/', views.quote, name='quote'),
    path('service/', views.service, name='service'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
]