from django.conf.urls import url
from cbvapp import views
app_name = 'cbvapp'

urlpatterns = [

    url(r'^$', views.SchoolListView.as_view(), name='list'),
    url(r'^create/', views.SchoolCreateView.as_view(), name='create'),
    url(r'^stucreate/', views.StudentCreateView.as_view(), name='stucreate'),
    url(r'^(?P<pk>[-\w]+)/$', views.SchoolDetailsView.as_view(), name='detail'),
    url(r'^update/(?P<pk>[-\w]+)/$', views.SchoolUpdateView.as_view(), name='update'),
    url(r'^stuupdate/(?P<pk>[-\w]+)/$', views.StudentUpdateView.as_view(), name='stuupdate'),
    url(r'^delete/(?P<pk>[-\w]+)/$', views.SchoolDeleteView.as_view(), name='delete'),

]
