from django.urls import path
from accounts import views

urlpatterns = [
    path('register/', views.RegistarAPI.as_view()),
    path('login/', views.LoginAPI.as_view()),
]