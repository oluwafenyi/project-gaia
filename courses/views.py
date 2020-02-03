
from django.shortcuts import render
from django.core.paginator import Paginator
from django.views import View
from django.http import JsonResponse
from django.templatetags.static import static

from .models import Course
from gaia.views import ExtendedView


class CoursesListView(ExtendedView):
    paginate_by = 9
    category = None
    static_banner_path = ''

    def get(self, request):
        category = dict(Course.CATEGORIES)[self.category]
        courses = Course.objects\
            .filter(category=self.category).order_by('code')
        paginator = Paginator(courses, self.paginate_by)
        first_page = paginator.page(1)
        banner_image = static(self.static_banner_path)
        context = {
            'courses': first_page,
            'category': category,
            'next': first_page.has_next(),
            'banner_image': banner_image,
        }
        context.update(self.contact_context)
        return render(request, 'courses/course_list.html', context=context)


class GeologyCoursesListView(CoursesListView):
    category = Course.GEOLOGY
    static_banner_path = 'img/bg-img/bg2.jpg'


class GeophysicsCoursesListView(CoursesListView):
    category = Course.GEOPHYSICS
    static_banner_path = 'img/bg-img/bg5.jpg'


class OthersCoursesListView(CoursesListView):
    category = Course.OTHERS
    static_banner_path = 'img/bg-img/bg6.jpg'


class CourseDetailView(ExtendedView):

    def get(self, request, category, code):
        course = Course.objects.get(code__iexact=code)
        context = {'course': course}
        context.update(self.contact_context)
        return render(request, 'courses/course_detail.html', context)
