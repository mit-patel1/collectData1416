from django.urls import path
from home import views

urlpatterns = [
    path('userdata/', views.UserDataAPI.as_view()),
    path('alldata/', views.PublicUserDataAPI.as_view()),
]