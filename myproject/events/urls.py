from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_event, name='upload_event'),
    path('thanks/', views.event_thanks, name='event_thanks'),
    path('list/', views.approved_events, name='approved_events'),
]