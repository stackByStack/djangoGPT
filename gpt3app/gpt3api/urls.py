from django.urls import path
from . import views

urlpatterns = [
    path('gpt3/', views.gpt3_request, name='gpt3_request'),
]