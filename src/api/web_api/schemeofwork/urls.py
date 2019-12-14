from django.urls import path

from .views import SchemeOfWorkViewSet


app_name = "schemeofwork"

# app_name will help us do a reverse look-up latter.

urlpatterns = [
    path('schemeofwork/<int:scheme_of_work_id>', SchemeOfWorkViewSet.as_view(), name="schemeofwork"),
]