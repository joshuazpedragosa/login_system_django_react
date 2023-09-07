from django.urls import path
from api import views

urlpatterns = [
    path('api_request/', views.api_request, name='api_request')
]
