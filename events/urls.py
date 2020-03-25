
from django.urls import path

from .views import EventDetailView


urlpatterns = [
    path('<str:slug>/', EventDetailView.as_view(), name='event_detail'),
]
