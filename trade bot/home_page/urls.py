from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [

    path('',views.home_page, name = "home_page"),
    path('register/',views.RegisterUser.as_view(), name = "register"),
    path('bot/',views.ContactFormView.as_view(), name = "bot"),
    path('botik/',views.botik, name = "botik"),

]