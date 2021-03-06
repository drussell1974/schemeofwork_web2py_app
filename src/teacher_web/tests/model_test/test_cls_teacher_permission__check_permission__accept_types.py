from unittest import TestCase, skip
from unittest.mock import MagicMock
from shared.models.cls_department import DepartmentModel
from shared.models.cls_institute import InstituteModel
from shared.models.cls_teacher import TeacherModel
from shared.models.cls_teacher_permission import TeacherPermissionModel as Model
from shared.models.cls_schemeofwork import SchemeOfWorkModel
from shared.models.enums.permissions import SCHEMEOFWORK, LESSON
from tests.test_helpers.mocks import fake_ctx_model

class test_cls_teacher_permission__check_permission__accept_types(TestCase):

    def setUp(self):
        # act
        #fake_user_model = TeacherModel(6079, "Dave Russell", department=DepartmentModel(67, "Computer Science", institute = InstituteModel(127671276711, name="Lorum Ipsum")))
        #fake_user_model.get_username = MagicMock(return_value="Dave Russell")
        self.test = Model(teacher_id=343434343, teacher_name="Tom foolery",  scheme_of_work=SchemeOfWorkModel(11), ctx=fake_ctx_model(),
            scheme_of_work_permission=SCHEMEOFWORK.NONE,
            lesson_permission=LESSON.NONE)
        self.test.is_authorised = True

    def tearDown(self):
        pass


    def test_should_raise_exception_when_none_type(self):
        # assert
        with self.assertRaises(TypeError):
            self.test.check_permission(None)

            
    def test_should_raise_exception_when_string_type(self):
        # assert
        with self.assertRaises(TypeError):
            self.test.check_permission("")

            
    def test_should_raise_exception_when_int_type(self):
        # assert
        with self.assertRaises(TypeError):
            self.test.check_permission(99)


    def test_can_accept_SCHEMEOFWORK_ACCESS_type(self):
        # assert
        self.assertTrue(self.test.check_permission(SCHEMEOFWORK.NONE))
        self.assertFalse(self.test.check_permission(SCHEMEOFWORK.EDITOR))
        

    def test_can_accept_LESSON_ACCESS_type(self):
        # assert
        self.assertTrue(self.test.check_permission(LESSON.NONE))
        self.assertFalse(self.test.check_permission(LESSON.OWNER))


    def test_should_be_false__when_is_authorised__false(self):
        # assert

        self.test.is_authorised = False

        self.assertFalse(self.test.check_permission(SCHEMEOFWORK.NONE))
        self.assertFalse(self.test.check_permission(SCHEMEOFWORK.EDITOR))
        self.assertFalse(self.test.check_permission(LESSON.NONE))
        self.assertFalse(self.test.check_permission(LESSON.OWNER))

