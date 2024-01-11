from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('beans/', views.beans, name='beans'),
  path('beans/<int:bean_id>/', views.bean_details, name='details'),
  path('beans/create/', views.BeanCreate.as_view(), name='beans_create'),
  path('beans/<int:pk>/update/', views.BeanUpdate.as_view(), name='beans_update'),
  path('beans/<int:pk>/delete/', views.BeanDelete.as_view(), name='beans_delete'),
]

