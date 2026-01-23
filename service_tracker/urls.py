from django.urls import path
from . import views

app_name = 'service_tracker'

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.createJob, name='create-job'),
    path('records/<int:pk>', views.detail, name='detail'),
    path('update/<int:pk>', views.updateJob, name='edit'),
    path('resolve/<int:pk>', views.markResolved, name='mark-resolved'),
]