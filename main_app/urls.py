from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('beans/', views.beans, name='beans'),
  path('beans/<int:bean_id>', views.bean_details, name='details')
]

