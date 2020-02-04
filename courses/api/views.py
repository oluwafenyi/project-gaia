
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.views import View
from django.http import JsonResponse, HttpResponseBadRequest

from ..models import Course
from ..views import SearchMixin


class CoursesListAPIView(View, SearchMixin):
    paginate_by = 9
    category = None
    search = False
    query = None

    def get(self, request):
        if self.search:
            try:
                query = self.get_query(request)
                self.query = query
            except ValueError:
                return HttpResponseBadRequest()
        page = request.GET.get('page')
        if not page:
            page = 1
        courses = self.get_queryset()
        paginator = Paginator(courses, self.paginate_by)
        try:
            section = paginator.page(page)
        except EmptyPage:
            return HttpResponseBadRequest()
        else:
            course_list = []
            for course in section:
                course_list.append({
                    'title': course.title,
                    'url': course.get_absolute_url(),
                    'code': course.code,
                    'category': course.verbose_category(),
                    'units': course.units,
                    'description': course.description,
                    'drive_link': course.drive_link,
                    'lecturers': [lecturer.full_name() for lecturer
                                  in course.lecturers.all()]
                })

            if section.has_next():
                _next = '{}?page={}'.format(
                    request.build_absolute_uri('?'), section.next_page_number()
                )
                if self.query:
                    _next += '&query={}'.format(self.query)
            else:
                _next = None

            data = {
                'data': course_list,
                'next': _next,
                'status': 200
            }
            return JsonResponse(data)


class GeologyCoursesListAPIView(CoursesListAPIView):
    category = Course.GEOLOGY


class GeophysicsCoursesListAPIView(CoursesListAPIView):
    category = Course.GEOPHYSICS


class OthersCoursesListAPIView(CoursesListAPIView):
    category = Course.OTHERS


class CourseSearchAPIView(CoursesListAPIView):
    search = True
