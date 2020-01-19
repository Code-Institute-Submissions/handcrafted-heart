from django.conf.urls import url
from .views import get_inspiration, inspiration_content, create_or_edit_inspiration

urlpatterns = [
    url(r'^$', get_inspiration, name='get_inspiration'),
    url(r'^(?P<pk>\d+)/$', inspiration_content, name='inspiration_content'),
    url(r'^add/$', create_or_edit_inspiration, name='add_inspiration'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_inspiration, name='edit_inspiration'),
]