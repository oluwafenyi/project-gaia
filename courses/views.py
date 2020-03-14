
from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views import View
from django.http import (
    HttpResponseRedirect,
    HttpResponseBadRequest
)
from django.urls import reverse
from django.db.models import Q
from django.templatetags.static import static

from .models import Course
from gaia.views import ExtendedView


class QueryAndQuerysetMixin:
    def get_query(self, request):
        try:
            return request.GET.get('query').strip()
        except AttributeError:
            raise ValueError

    def get_queryset(self):
        if self.query:
            lookups = Q(code__icontains=self.query) \
                | Q(title__icontains=self.query)
        elif self.category and self.category.isnumeric():
            lookups = Q(category=self.category)
        elif self.all:
            return Course.objects.all().order_by('code')
        else:
            raise ImproperlyConfigured('Specify Course'
                                       ' Model Category or query')
        return Course.objects.filter(lookups).distinct()\
            .order_by('category', 'code')


class CoursesListView(ExtendedView, QueryAndQuerysetMixin):
    paginate_by = 9
    category = None
    static_banner_path = ''
    query = None
    api_name = ''
    search = False

    def get_banner_path(self):
        if self.static_banner_path:
            return static(self.static_banner_path)
        return None

    def get_category(self):
        if self.category.isnumeric():
            return dict(Course.CATEGORIES)[self.category]
        return self.category

    def get_api(self):
        if self.api_name:
            return reverse(self.api_name)

        elif self.category.isnumeric():
            category = self.get_category()
            return reverse('{}_course_list_api'.format(category.lower()))

        raise ImproperlyConfigured('Specify api_name or Course Model Category')

    def get(self, request):
        if self.search:
            try:
                query = self.get_query(request)
                self.query = query
            except ValueError:
                return HttpResponseBadRequest()
            previous_page = request.META.get('HTTP_REFERER')
            if not query:
                if previous_page:
                    return HttpResponseRedirect(previous_page)
                else:
                    return HttpResponseBadRequest()

        category = self.get_category()
        courses = self.get_queryset()
        paginator = Paginator(courses, self.paginate_by)
        first_page = paginator.page(1)
        banner_image = self.get_banner_path()
        api = self.get_api()
        context = {
            'courses': first_page,
            'category': category,
            'next': first_page.has_next(),
            'banner_image': banner_image,
            'api': api,
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


class CourseSearchView(CoursesListView):
    category = 'Search Results'
    api_name = 'course_search_api'
    search = True


class AllCoursesView(CoursesListView):
    category = 'All Courses'
    api_name = 'all_courses_api'
    all = True


class CourseDetailView(ExtendedView):

    def get(self, request, category, code):
        course = get_object_or_404(Course, code__iexact=code)
        pre = course.prerequisites.split(', ')
        prerequisites = []
        for code in pre:
            try:
                prerequisites.append(Course.objects.get(code=code))
            except Course.DoesNotExist:
                pass
        curriculum = course.curriculum.split('. ') if course.curriculum else\
            None
        context = {
            'course': course,
            'prerequisites': prerequisites,
            'curriculum': curriculum
        }
        context.update(self.contact_context)
        return render(request, 'courses/course_detail.html', context)
