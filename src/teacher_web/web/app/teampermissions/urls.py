from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="team-permissions.index"),
    path("schemeofwork/<int:scheme_of_work_id>/teacher/<str:permission>/login", views.TeamPermissionRequestLoginView.as_view(), name="team-permissions.login-as"),
    path('schemeofwork/<int:scheme_of_work_id>/teacher/<int:teacher_id>/edit', views.edit, name='team-permissions.edit'),
    path('schemeofwork/<int:scheme_of_work_id>/teacher/<int:teacher_id>/delete', views.delete, name='team-permissions.delete'),
    path("schemeofwork/<int:scheme_of_work_id>/teacher/<str:permission>/request-access", views.request_access, name="team-permissions.request-access"),
]