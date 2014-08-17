from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns("",
	url(r"^images/$", views.ImageCreate.as_view()),
	url(r"^images/(?P<uuid>[^/]+)/$", views.GetImage.as_view()),
)
