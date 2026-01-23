from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('add-staff/', views.signUp, name='create-staff'),
]
