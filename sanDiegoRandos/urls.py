from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'permanents$', views.returnPermanents, name="returnPermanents"),
    url(r'gather$', views.gatherPermanents, name="gatherPermanents"),

]
