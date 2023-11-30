from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "language_app"

urlpatterns = [
            path('NewLanguage/',
                views.LanguageAPISerializer.as_view(),
                name='NewLanguage'),
]