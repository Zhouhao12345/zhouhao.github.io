from django.conf.urls import patterns, include, url
from teambuilder import views

app_name = 'teambuilder'
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^create-team/$', views.create_team, name='create_team'),
    url(r'^add-course/$', views.add_course, name='add_course'),
    url(r'^profile/(?P<username>[\w\-]+)/$', views.profile, name='profile'),
    url(r'^edit-profile/$', views.edit_profile, name='edit_profile'),
    url(r'^team/(?P<team_name_slug>[\w\-]+)/$', views.team_details, name='team_detail'),
    url(r'^team/(?P<team_name_slug>[\w\-]+)/edit/$', views.edit_team, name='edit_team'),
    url(r'^course/(?P<course_name_slug>[\w\-]+)/$', views.course_details, name='course_detail'),
    url(r'^course/(?P<course_name_slug>[\w\-]+)/edit/$', views.edit_course, name='edit_course'),
    url(r'^course/(?P<course_name_slug>[\w\-]+)/teams/$', views.view_course_teams, name='view_course_teams'),
    url(r'^find-team/$', views.find_team, name='find_team'),
    url(r'^search-team/$', views.search_team, name='search_team'),
    url(r'^team/(?P<team_name_slug>[\w\-]+)/send-request/$', views.join_team, name='join_team'),
    url(r'^team/(?P<team_name_slug>[\w\-]+)/cancel-request/$', views.cancel_request, name='cancel_request'),
    url(r'^team/(?P<team_name_slug>[\w\-]+)/view-requests/$', views.view_requests, name='view_requests'),
    url(r'^team/(?P<team_name_slug>[\w\-]+)/view-members/$', views.view_team_members, name='view_team_members'),
    url(r'^request/(?P<request_id>[\w\-]+)/accept/$', views.accept_request, name='accept_request'),
    url(r'^request/(?P<request_id>[\w\-]+)/reject/$', views.reject_request, name='reject_request'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^unauthorized/$', views.unauthorized, name='unauthorized'),
    url(r'^page-not-found/$', views.page_not_found, name='page_not_found'),
    url(r'^course/(?P<course_name_slug>[\w\-]+)/merge-teams/$', views.merge_teams, name='merge_teams'),

)