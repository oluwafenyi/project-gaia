
from django.urls import path

from .views import GeologyCoursesListAPIView


urlpatterns = [
    path(
        'geology/',
        GeologyCoursesListAPIView.as_view(),
        name='geology_course_list_api',
    ),
]
