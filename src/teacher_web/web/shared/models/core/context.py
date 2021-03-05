from shared.models.cls_institute import InstituteContextModel
from shared.models.cls_department import DepartmentContextModel
from shared.models.cls_schemeofwork import SchemeOfWorkContextModel
from shared.models.cls_teacher_permission import TeacherPermissionModel
from shared.models.enums.permissions import DEPARTMENT, SCHEMEOFWORK, LESSON
from shared.models.enums.publlished import STATE

class Ctx:
    
    def __init__(self, institute_id, department_id, **view_params):
        self.institute_id = institute_id
        self.department_id = department_id
        self.scheme_of_work_id = view_params.get("scheme_of_work_id",0)
        self.auth_user_id = view_params.get("auth_user_id",0)
        # public member
        self.can_view = STATE.PUBLISH


class AuthCtx(Ctx):
    
    def __init__(self, db, request, institute_id, department_id, **view_params):
        super().__init__(institute_id=institute_id, department_id=department_id, **view_params)

        self.request = request
        self.auth_user_id = request.user.id

        if request.user.id is not None:
            self.user_name = request.user.first_name
            # logged in member can view internal and public published
            self.can_view = STATE.PUBLISH_INTERNAL

        # NOTE: get department then get institute to promote can_view

        self.department = DepartmentContextModel.cached(request, db, self.institute_id, self.department_id, self.auth_user_id)
        # TODO: #323 check ownership and set can_view
        self.department_permission = DEPARTMENT.ADMIN if self.auth_user_id == self.department.created_by_id else DEPARTMENT.NONE

        self.institute = InstituteContextModel.cached(request, db, self.institute_id, self.auth_user_id)
        # TODO: #323 check ownership and set can_view
        self.department_permission = DEPARTMENT.ADMIN if self.auth_user_id == self.institute.created_by_id else DEPARTMENT.NONE

        self.scheme_of_work = SchemeOfWorkContextModel.cached(request, db, self.institute_id, self.department_id, self.scheme_of_work_id, self.auth_user_id)
        # TODO: #323 check ownership and set can_view
        self.scheme_of_work_permission = SCHEMEOFWORK.OWNER if request.user.id == self.institute.created_by_id else SCHEMEOFWORK.NONE
        self.lesson_permission = LESSON.OWNER if request.user.id == self.institute.created_by_id else LESSON.NONE

        self.teacher_permission = TeacherPermissionModel.empty(institute_id, department_id, None, self)
        self.teacher_permission.is_authorised = (self.auth_user_id == self.institute.created_by_id)
        
        if self.auth_user_id is not None and self.auth_user_id > 0:
            self.teacher_permission = TeacherPermissionModel.get_model(db, teacher_id=self.auth_user_id, scheme_of_work=self.scheme_of_work, auth_user=self)
            if self.teacher_permission.is_from_db == True:
                self.department_permission =  DEPARTMENT(self.teacher_permission.department_permission)
                self.scheme_of_work_permission = SCHEMEOFWORK(self.teacher_permission.scheme_of_work_permission)
                self.lesson_permission = LESSON(self.teacher_permission.lesson_permission)
        else:
            self.teacher_permission = None
            self.department_permission = DEPARTMENT.NONE
            self.scheme_of_work_permission = SCHEMEOFWORK.NONE
            self.lesson_permission = LESSON.NONE


    def __repr__(self):
        return f"institute_id={self.institute_id}, department_id={self.department_id}"
