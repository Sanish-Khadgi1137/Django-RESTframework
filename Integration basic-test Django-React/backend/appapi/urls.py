from django.urls import path
from .views import Get_Message

urlpatterns= [
    path('message/', Get_Message)
]