from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "country_app"

urlpatterns = [
        path('NewCountry/',
                views.CountryAPISerializer.as_view(),
                name='NewCountry'),

]