
from django.conf import settings
from django.views import View
from django.shortcuts import render

from courses.models import Course
from people.models import Executive


class ExtendedView(View):
    contact_context = settings.OUR_CONTACT_INFO


class HomePageView(ExtendedView):

    def get(self, request):
        course_count = Course.objects.all().count()
        exco_count = Executive.objects.all().count()
        context = {'course_count': course_count, 'exco_count': exco_count}
        context.update(self.contact_context)
        return render(request, 'gaia/index.html', context=context)


class ContactPageView(ExtendedView):

    def get(self, request):
        context = {}
        context.update(self.contact_context)
        return render(request, 'gaia/contact.html', context=context)
