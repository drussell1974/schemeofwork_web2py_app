from unittest import TestCase, skip
from shared.models.cls_teacher_permission import TeacherPermissionModel as Model
from shared.models.enums.permissions import SCHEMEOFWORK, LESSON


class test_cls_teacher_permission__check_permission__accept_types(TestCase):

    def setUp(self):
        # act
        self.test = Model(auth_user=2,scheme_of_work_id=11, 
            scheme_of_work_permission=SCHEMEOFWORK.NONE,
            lesson_permission=LESSON.NONE)

        pass

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
        self.assertFalse(self.test.check_permission(SCHEMEOFWORK.EDIT))
        

    def test_can_accept_LESSON_ACCESS_type(self):
        # assert
        self.assertTrue(self.test.check_permission(LESSON.NONE))
        self.assertFalse(self.test.check_permission(LESSON.ADD))

