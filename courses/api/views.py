from django.core.paginator import Paginator, EmptyPage
from django.views import View
from django.http import JsonResponse, HttpResponseBadRequest

from ..models import Course
from ..views import CATEGORIES


class GeologyCoursesListAPIView(View):
    paginate_by = 9

    def get(self, request):
        page = request.GET.get('page')
        if not page:
            page = 1
        courses = Course.objects\
            .filter(category=Course.GEOLOGY).order_by('code')
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
                    'code': course.code,
                    'category': CATEGORIES[course.category],
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
            else:
                _next = None

            data = {
                'data': course_list,
                'next': _next,
                'status': 200
            }
            return JsonResponse(data)
