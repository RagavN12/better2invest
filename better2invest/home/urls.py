from django.urls import path
from . import views

urlpatterns = [
    path("", views.mainpage),
    path('home/', views.mainpage),
    path("login/", views.loginpage, name="login"),
    path("signup/",views.signupPage, name="signup")
]