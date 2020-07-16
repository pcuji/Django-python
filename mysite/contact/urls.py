from django.contrib import admin
from django.urls import path
from django.conf.urls import url
# from .views import emailView, successView

from .import views

app_name = 'contact'

urlpatterns = [
        url(r'^$',views.email_view, name = "email"),
]
