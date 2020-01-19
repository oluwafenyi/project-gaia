
from django.urls import path

from .views import GeologyCoursesListView


urlpatterns = [
    path(
        'geology/',
        GeologyCoursesListView.as_view(),
        name='geology_course_list',
    ),
]
