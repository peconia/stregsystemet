from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.kiosk),
    url(r'^random$', views.find_random_image),
    url(r'^next$', views.find_next_image),
]
