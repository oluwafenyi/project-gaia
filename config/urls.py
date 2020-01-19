
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from gaia.views import HomePageView, ContactPageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('api/courses/', include('courses.api.urls')),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('courses/', include('courses.urls')),
    path('people/', include('people.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
