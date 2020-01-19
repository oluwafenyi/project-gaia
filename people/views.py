
from django.shortcuts import render

from .models import Executive, Lecturer
from courses.models import Course
from gaia.views import ExtendedView


class ExcosAndLecturersListView(ExtendedView):

    def get(self, request):
        excos = Executive.objects.all()
        lecturers = Lecturer.objects.filter(courses__category__in=[
            Course.GEOLOGY, Course.GEOPHYSICS
        ]).distinct()
        context = {'excos': excos, 'lecturers': lecturers}
        context.update(self.contact_context)
        return render(request, 'people/people.html', context)
