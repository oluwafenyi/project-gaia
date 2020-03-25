
from django.conf import settings
from django.contrib.messages import success
from django.views import View
from django.shortcuts import render
from django.utils import timezone

from courses.models import Course
from people.models import Executive
from events.models import Event
from .forms import ContactForm


class ExtendedView(View):
    contact_context = settings.OUR_CONTACT_INFO


class HomePageView(ExtendedView):

    def get(self, request):
        course_count = Course.objects.all().count()
        exco_count = Executive.objects.all().count()
        events = Event.objects.filter(end_date__gte=timezone.now())\
            .order_by('start_date')[:3]
        try:
            next_event = events[0]
        except IndexError:
            next_event = None

        context = {
            'course_count': course_count,
            'exco_count': exco_count,
            'upcoming_events': events,
            'next_event': next_event,
        }
        context.update(self.contact_context)
        return render(request, 'gaia/index.html', context=context)


class ContactPageView(ExtendedView):

    def get(self, request):
        context = {}
        context.update(self.contact_context)
        return render(request, 'gaia/contact.html', context=context)

    def post(self, request):
        context = {}
        context.update(self.contact_context)

        form = ContactForm(request.POST)
        if form.is_valid():
            mail_sent = form.send_mail()
            if mail_sent:
                context.update({'form': ContactForm()})
                success(request, 'Email sent successfully.')
                return render(request, 'gaia/contact.html', context)
        context.update({'form': form})
        return render(request, 'gaia/contact.html', context)
