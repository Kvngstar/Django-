from django.urls import path
from jonesapp.views import *

urlpatterns = [
    path("", index, name="index"),
    path("about/",about, name="about"),
    path("contact/",contact, name="contact"),
    path("products/",products, name="products"),
    path("register/",register, name="register"),
    path("signIn/",signIn, name="signIn"),
    path("video/",video, name="video"),
    path("processregister",processregister, name="processregister"),
    # path('logout', logout, name= 'logout')
]