
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from gaia.views import HomePageView, ContactPageView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('contact/', ContactPageView.as_view(), name='contact'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
