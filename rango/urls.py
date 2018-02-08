from django.conf.urls import url
from rango import views

#Items on page 48 may need to be added

urlpatterns = [
	url(r'^$', views.index, name='index'),
        url(r'^about/',views.about,name='about'),
]
