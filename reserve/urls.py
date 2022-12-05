from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from reserve import views


app_name = 'reserve'
urlpatterns = [
    path('', views.available_rooms, name='available_rooms'),
    path('reserve-room/<int:pk>/', views.reserve_room, name='reserve_room'),
    # path('about-us/', views.about, name='about'),
]
