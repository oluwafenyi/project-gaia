
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage
from django.views import View
from django.http import JsonResponse

from .models import Course
from gaia.views import ExtendedView


class CoursesListView(ExtendedView):
    paginate_by = 9
    category = None

    def get(self, request):
        category = dict(Course.CATEGORIES)[self.category]
        courses = Course.objects\
            .filter(category=self.category).order_by('code')
        paginator = Paginator(courses, self.paginate_by)
        first_page = paginator.page(1)
        context = {
            'courses': first_page,
            'category': category,
            'next': first_page.has_next(),
        }
        context.update(self.contact_context)
        return render(request, 'courses/course_list.html', context=context)


class GeologyCoursesListView(CoursesListView):
    category = Course.GEOLOGY


class GeophysicsCoursesListView(CoursesListView):
    category = Course.GEOPHYSICS


class OthersCoursesListView(CoursesListView):
    category = Course.OTHERS
