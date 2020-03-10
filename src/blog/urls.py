from . import views
from django.contrib import admin
from django.urls import path

from .views import contact_us

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('about/', views.about.as_view(), name='about'),
    path('about_page/', views.about_page.as_view(), name='about_page'),
    path('privacy/', views.privacy.as_view(), name='privacy'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('contact_us/1/', views.contact_us, name='contact_us'),
    

]

