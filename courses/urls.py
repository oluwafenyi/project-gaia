
from django.urls import path

from .views import (
    GeologyCoursesListView,
    GeophysicsCoursesListView,
    OthersCoursesListView,
    CourseDetailView,
)


urlpatterns = [
    path(
        '<str:category>/<str:code>/',
        CourseDetailView.as_view(),
        name='course_detail',
    ),
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
