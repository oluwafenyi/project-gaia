
from django.urls import path

from .views import (
    GeologyCoursesListView,
    GeophysicsCoursesListView,
    OthersCoursesListView,
    CourseDetailView,
    CourseSearchView,
    AllCoursesView,
)


urlpatterns = [
    path(
        '',
        AllCoursesView.as_view(),
        name='all_courses',
    ),
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
    path(
        'search/',
        CourseSearchView.as_view(),
        name='course_search',
    ),
]
