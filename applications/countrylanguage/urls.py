from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "countrylanguage_app"

urlpatterns = [
            path('NewCl/',
                views.CountryLanguageAPISerializer.as_view(),
                name='NewCountryLenguage'),
]