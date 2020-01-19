
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage
from django.views import View
from django.http import JsonResponse
from django.urls import reverse

from .models import Course
from gaia.views import ExtendedView


CATEGORIES = {
    '1': 'Geology',
    '2': 'Geophysics',
    '3': 'Others',
}


class GeologyCoursesListView(ExtendedView):
    paginate_by = 9

    def get(self, request):
        category = CATEGORIES[Course.GEOLOGY]
        courses = Course.objects\
            .filter(category=Course.GEOLOGY).order_by('code')
        paginator = Paginator(courses, self.paginate_by)
        first_page = paginator.page(1)
        context = {
            'courses': first_page,
            'category': category,
            'next': first_page.has_next(),
            'category_api': reverse('{}_course_list_api'
                                    .format(category.lower())),
        }
        context.update(self.contact_context)
        return render(request, 'courses/course_list.html', context=context)
