from shared.models.cls_department import DepartmentModel
from shared.models.cls_institute import InstituteModel
from shared.models.cls_teacher import TeacherModel
from shared.models.cls_teacher_permission import TeacherPermissionModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.enums.permissions import DEPARTMENT, SCHEMEOFWORK, LESSON
from shared.models.core.context import Ctx

mock_scheme_of_work = SchemeOfWorkModel(99, name="A-Level Computer Science")

def fake_ctx_model(auth_user_id = 6079, department_permission=DEPARTMENT.HEAD, scheme_of_work_permission=SCHEMEOFWORK.OWNER, lesson_permission=LESSON.OWNER, is_authorised=False):
    
    institute = InstituteModel(127671276711, name="Lorum Ipsum")
    
    department = DepartmentModel(67, name="Computer Science", institute=institute, is_from_db=True)
    
    scheme_of_work = SchemeOfWorkModel(12323232, name="GCSE Computer Science")

    ctx = TeacherPermissionModel(teacher_id=9999, teacher_name="Dave Russell", scheme_of_work=scheme_of_work, is_from_db=True, ctx=Ctx(institute.id, department.id, scheme_of_work.id))
    
    ctx.is_authorised = is_authorised
    ctx.department_permission = department_permission
    ctx.scheme_of_work_permission = scheme_of_work_permission
    ctx.lesson_permission = lesson_permission
    ctx.auth_user_id = auth_user_id
    
    return ctx


def fake_teacher_permission_model(is_from_db=True, is_authorised=True):

    institute = InstituteModel(127671276711, name="Lorum Ipsum")
    
    department = DepartmentModel(67, "Computer Science", institute=institute, is_from_db=True)

    scheme_of_work = SchemeOfWorkModel(14, name="A-Level Computer Science", department_id = department.id, institute_id = institute.id, is_from_db=is_from_db)
    
    return TeacherPermissionModel(teacher_id=56, teacher_name="Jane Mellor" , scheme_of_work=scheme_of_work, is_from_db=is_from_db, ctx=Ctx(127671276711, 34, 14), scheme_of_work_permission=SCHEMEOFWORK.OWNER, lesson_permission=LESSON.OWNER, department_permission=DEPARTMENT.HEAD, is_authorised=is_authorised)