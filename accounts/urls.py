from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
app_name = 'accounts'
urlpatterns = [
    # path('add-staff/', views.signUp, name='create-staff'),
    path('add-staff/', views.CreateStaffView.as_view(), name='create-staff'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='accounts:login'), name='logout'),
    path('force-password-change/', views.ForcePasswordChangeView.as_view(), name='force-password-change'),
]
