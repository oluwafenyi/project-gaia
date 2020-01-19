
from django.urls import path

from .views import (
    GeologyCoursesListView,
    GeophysicsCoursesListView,
    OthersCoursesListView,
)


urlpatterns = [
    path(
        'geology/',
        GeologyCoursesListView.as_view(),
        name='geology_course_list',
    ),
    path(
        'geophysics/',
        GeophysicsCoursesListView.as_view(),
        name='geophysics_course_list',
    ),
    path(
        'others/',
        OthersCoursesListView.as_view(),
        name='others_course_list',
    ),
]
