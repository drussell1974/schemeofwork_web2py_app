from django.db import connection as db
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import permission_required
from shared.models.core.django_helper import auth_user_id
from shared.models.core.log import handle_log_warning, handle_log_info
from shared.models.enums.permissions import DEPARTMENT, SCHEMEOFWORK
from shared.viewmodels.decorators.permissions import min_permission_required
from shared.view_model import ViewModel
from app.schemesofwork.viewmodels import SchemeOfWorkEditViewModel
from app.schemesofwork.viewmodels import SchemeOfWorkIndexViewModel
from app.schemesofwork.viewmodels import SchemeOfWorkDeleteUnpublishedViewModel

# Create your views here.

@min_permission_required(DEPARTMENT.NONE, "/accounts/login/")
def index(request):
    #253 check user id
    getall_view =  SchemeOfWorkIndexViewModel(db=db, auth_user=auth_user_id(request))
    
    data = {
        "schemes_of_work":getall_view.model
    }

    view_model = ViewModel("", "Schemes of Work", "Our shared schemes of work by key stage", data=data)

    return render(request, "schemesofwork/index.html", view_model.content)


@permission_required('cssow.change_schemeofworkmodel', login_url='/accounts/login/')
@min_permission_required(DEPARTMENT.HEAD, "/accounts/login/")
def edit(request, scheme_of_work_id = 0):
    """ edit action """
    
    save_view = SchemeOfWorkEditViewModel(db=db, request=request, scheme_of_work_id=scheme_of_work_id, auth_user=auth_user_id(request))
    
    if save_view.saved == True:

        if request.POST.get("next", None) != "None"  and request.POST.get("next", None) != "":
            redirect_to_url = request.POST.get("next", None)
        else:
            redirect_to_url = reverse('schemesofwork.edit', args=[save_view.model.id])
        return HttpResponseRedirect(redirect_to_url)
    
    return render(request, "schemesofwork/edit.html", save_view.view().content)


@permission_required('cssow.delete_schemeofworkmodel', login_url='/accounts/login/')
@min_permission_required(DEPARTMENT.ADMIN, "/accounts/login/")
def delete_unpublished(request):
    """ delete item and redirect back to referer """

    SchemeOfWorkDeleteUnpublishedViewModel(db=db, auth_user=auth_user_id(request))

    return HttpResponseRedirect(reverse("schemesofwork.index"))