from django.urls import re_path
from accounts import views as accounts_views
from lists import views

urlpatterns = [
    re_path(r'^$', views.home_page, name='home'),
    re_path(r'^lists/new$', views.new_list, name='new_list'),
    re_path(r'^lists/(\d+)/$', views.view_list, name='view_list'),
    re_path(r'^accounts/send_login_email$', accounts_views.send_login_email, name='send_login_email'),
]
