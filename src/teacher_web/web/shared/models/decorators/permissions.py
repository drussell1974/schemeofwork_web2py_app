from django.db import connection as db
from django.shortcuts import redirect
from django.urls import reverse
from shared.models.core.log_handlers import handle_log_info, handle_log_warning, handle_log_error
from shared.models.enums.permissions import SCHEMEOFWORK, LESSON 
from shared.models.cls_teacher import TeacherModel
from shared.models.cls_teacher_permission import TeacherPermissionModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel

DEFAULT_INSTITUTE_ID = 0
DEFAULT_DEPARTMENT_ID = 0
DEFAULT_SCHEME_OF_WORK_ID = 0
DEFAULT_LESSON_ID = 0
UNAUTHORISED_USER_ID = None


def unauthorise_request(func):
    """
    changes to request.user.id to UNAUTHORISED_USER_ID 
    """
        
    def inner(*args, **kwargs):
        for arg in args:   
            if hasattr(arg, 'user') and hasattr(arg.user, 'id'):
                arg.user.id = UNAUTHORISED_USER_ID
        return func(*args, **kwargs)
    return inner


class min_permission_required:
    """ checks the teachers permission on the scheme of work and redirect if user does not have permission """

    def __init__(self, permission, login_url, login_route_name = None):
        """ SCHEMEOFWORK_ACCESS and LESSON_ACCESS decorator argument """
        self._permission = permission
        self._auth_user = 0
        self._scheme_of_work_id = 0
        self._redirect_to_url = login_url
        self._redirect_to_route_name = login_route_name


    def __call__(self, func):
        """ the parent function """

        def inner(*args, **kwargs):
            ''' request must be the first argument in the view function '''

            self.kwargs = kwargs

            self._return_url = args[0].path

            str_err = f"You do not have {str(self._permission).split('.')[1]} permission"
            
            #329 get department and school context and persist in auth_user
            
            self._auth_user = TeacherModel.get_model(db, args[0].user.id, 
                department_id=self.getkeyargs("department_id", default_value=DEFAULT_DEPARTMENT_ID),
                institute_id=self.getkeyargs("institute_id", default_value=DEFAULT_INSTITUTE_ID))
            
            if self._auth_user is None or self._auth_user.is_authorised == False:
                return self.redirect_handler(str_err, 0, permission=self._permission) 
            
            ''' scheme_of_work_id must be included in the view function or default '''
            
            self._scheme_of_work_id = self.getkeyargs("scheme_of_work_id", default_value=DEFAULT_SCHEME_OF_WORK_ID)
            
            scheme_of_work = SchemeOfWorkModel.get_model(db, self._scheme_of_work_id, self._auth_user)

            ''' teacher_id and auth_user are the same in this call '''
            
            model = TeacherPermissionModel.get_model(db, scheme_of_work, teacher=self._auth_user, auth_user=self._auth_user)
            
            if model.check_permission(self._permission) == False:
                ''' redirect if user does not have permissions for this scheme of work '''
                str_err = str_err + f" for this {str(self._permission).split('.')[0]} ({self._scheme_of_work_id}) redirect to {self._redirect_to_url}."
                
                return self.redirect_handler(str_err, scheme_of_work_id=self._scheme_of_work_id, permission=self._permission) 

            # call decorated function
            return func(*args, **kwargs)
            
        return inner
        

    def getkeyargs(self, key, default_value = None):
        if key in self.kwargs.keys():
            return self.kwargs[key]
        elif default_value is not None:
            return default_value
        else:
            raise KeyError(f"'{key}' value must be passed as a keyword argument")


    def redirect_handler(self, error_message, scheme_of_work_id, permission):
        handle_log_warning(db, self._scheme_of_work_id, msg="permission denied", details=error_message)
        if self._redirect_to_route_name is not None and scheme_of_work_id > 0:
            self._redirect_to_url = reverse("team-permissions.login-as", args=[scheme_of_work_id, str(permission)])
        
        return redirect(f"{self._redirect_to_url}?next={self._return_url}")
        