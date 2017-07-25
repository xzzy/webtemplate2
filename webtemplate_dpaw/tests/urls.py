from django.conf.urls import patterns, url
from .views import TestPage, TestDBCAPage, TestPage2, TestInternetPage

urlpatterns = patterns(
    '',
    url(r'^test/$', TestPage.as_view(), name='test_page'),
    url(r'^test-dbca/$', TestDBCAPage.as_view(), name='test_dbca_page'),
    url(r'^test2/$', TestPage2.as_view(), name='test_page_2'),
    url(r'^test-internet/$', TestInternetPage.as_view(), name='test_internet_page'),
    # We need the following named URLs to render the base template.
    url(r'^login/$', TestPage.as_view(), name='login'),
    url(r'^logout/$', TestPage.as_view(), name='logout'),
)
