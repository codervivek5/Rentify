from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.home, name='home'),
    path('post/', views.post_property, name='post_property'),
    path('my-properties/', views.my_properties, name='my_properties'),
    path('update/<int:property_id>/', views.update_property, name='update_property'),
    path('delete/<int:property_id>/', views.delete_property, name='delete_property'),
    path('property/<int:property_id>/', views.property_detail, name='property_detail'),
    path('like/<int:property_id>/', views.like_property, name='like_property'),
]
