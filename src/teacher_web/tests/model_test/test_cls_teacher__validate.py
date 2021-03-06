from unittest import TestCase, skip
from tests.model_test.learningobjective_testcase import LearningObjective_TestCase
from shared.models.cls_department import DepartmentModel
from shared.models.cls_institute import InstituteModel
from shared.models.cls_teacher import TeacherModel

@skip("depreciate TeacherModel and use TeacherPermissionModel")
class test_cls_teacher_validate__name(TestCase):

    test = None

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_min__valid_extreme(self):
        # arrange
        test = TeacherModel(6079, "Dave Russell", department=DepartmentModel(67, "Computer Science", institute = InstituteModel(127671276711, name="Lorum Ipsum")))
        
        test.name = "A"

        # act
        test.validate()

        # assert
        self.assertFalse("name" in test.validation_errors, "name should not have validation error %s" % test.validation_errors)
        self.assertTrue(test.is_valid, "is_valid should be True")


    def test_min__valid_extreme_trim_whitespace(self):
        # arrange
        test = TeacherModel(1, "Dave Russell", department=DepartmentModel(67, "Computer Science", institute = InstituteModel(127671276711, name="Lorum Ipsum")))
        
        test.name = " x "

        # act
        test.validate()

        # assert
        self.assertFalse("name" in test.validation_errors, "name should have no validation errors - %s" % test.validation_errors)
        self.assertEqual(test.name, "x")
        self.assertTrue(test.is_valid, "is_valid should be True")


    def test_min__invalid_extreme(self):
        # arrange
        test = TeacherModel(6079, "Dave Russell", department=DepartmentModel(67, "Computer Science", institute = InstituteModel(127671276711, name="Lorum Ipsum")))
        
        test.name = ""

        # act
        test.validate()

        # assert
        self.assertTrue("name" in test.validation_errors, "name should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "should not be is_valid")


    def test_min__invalid_extreme_when_None(self):
        # arrange
        test = TeacherModel(6079, "Dave Russell", department=DepartmentModel(67, "Computer Science", institute = InstituteModel(127671276711, name="Lorum Ipsum")))
        
        test.name = None

        # act
        test.validate()

        # assert
        self.assertTrue("name" in test.validation_errors, "name should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")


    def test_max__valid_extreme(self):
        # arrange
        test = TeacherModel(6079, "Dave Russell", department=DepartmentModel(67, "Computer Science", institute = InstituteModel(127671276711, name="Lorum Ipsum")))
        
        test.name = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse e" # length 70 characters

        # act
        test.validate()

        # assert
        self.assertFalse("name" in test.validation_errors, "name should not have validation error %s" % test.validation_errors)
        self.assertTrue(test.is_valid, "is_valid should be True")


    def test_max__invalid_extreme(self):
        # arrange
        test = TeacherModel(6079, "Dave Russell", department=DepartmentModel(67, "Computer Science", institute = InstituteModel(127671276711, name="Lorum Ipsum")))
        
        test.name = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse el"  # length 71 characters

        # act
        test.validate()

        # assert
        self.assertTrue("name" in test.validation_errors, "name should have validation error %s" % test.validation_errors)
        self.assertFalse(test.is_valid, "is_valid should be False")
