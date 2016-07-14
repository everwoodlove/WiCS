from django.conf.urls import url
from wicsWebsite import views

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^aboutus/$', views.about_us, name='about_us'),
    url(r'^documents/$', views.documents, name='documents'),
    url(r'^events/$', views.events, name='events'),
    url(r'^outreach/$', views.outreach, name='outreach'),
    url(r'^imagearchive/$', views.image_archive, name='image_archive'),
]

