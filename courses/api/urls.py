
from django.urls import path

from .views import (
    GeologyCoursesListAPIView,
    GeophysicsCoursesListAPIView,
    OthersCoursesListAPIView,
)


urlpatterns = [
    path(
        'geology/',
        GeologyCoursesListAPIView.as_view(),
        name='geology_course_list_api',
    ),
    path(
        'geophysics/',
        GeophysicsCoursesListAPIView.as_view(),
        name='geophysics_course_list_api',
    ),
    path(
        'others/',
        OthersCoursesListAPIView.as_view(),
        name='others_course_list_api',
    ),
]
