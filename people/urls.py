
from django.urls import path

from .views import ExcosAndLecturersListView


urlpatterns = [
    path('', ExcosAndLecturersListView.as_view(), name='excos_lecturers_list')
]
