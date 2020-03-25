
from django.shortcuts import get_object_or_404, render

from .models import Event
from gaia.views import ExtendedView


class EventDetailView(ExtendedView):

    def get(self, request, slug):
        event = get_object_or_404(Event, slug=slug)
        context = {'event': event}
        context.update(self.contact_context)
        return render(request, 'events/event_detail.html', context)
