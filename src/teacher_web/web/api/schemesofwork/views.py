from rest_framework.views import APIView
from django.db import connection as db
from django.http import JsonResponse
from shared.models.core.context import AuthCtx
from .viewmodels import SchemeOfWorkGetAllViewModel, SchemeOfWorkGetModelViewModel

class SchemeOfWorkViewSet(APIView):
    ''' API endpoint for a schemeofwork '''

    def get(self, request, institute_id, department_id, scheme_of_work_id, auth_ctx=None):

        # TODO: #367 get auth_ctx from min_permission_required decorator
        auth_ctx = AuthCtx(db, request, institute_id=institute_id, department_id=department_id, scheme_of_work_id=scheme_of_work_id)

        #253 check user id
        schemeofwork_view = SchemeOfWorkGetModelViewModel(db=db, scheme_of_work_id=scheme_of_work_id, auth_user=auth_ctx)
        return JsonResponse({"schemeofwork":schemeofwork_view.model})


class SchemeOfWorkListViewSet(APIView):
    ''' API endpoint for list of lessons '''

    def get (self, request, institute_id, department_id, auth_ctx=None):

        # TODO: #367 get auth_ctx from min_permission_required decorator
        auth_ctx = AuthCtx(db, request, institute_id=institute_id, department_id=department_id)

        #253 check user id
        schemesofwork_view = SchemeOfWorkGetAllViewModel(db=db, auth_user=auth_ctx)
        return JsonResponse({"schemesofwork": schemesofwork_view.model})