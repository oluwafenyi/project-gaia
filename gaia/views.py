
from django.views import View
from django.shortcuts import render


class HomePageView(View):

    def get(self, request):
        return render(request, 'gaia/index.html')
