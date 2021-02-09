from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_lesson import LessonModel, LessonDataAccess, handle_log_info
from shared.models.cls_department import DepartmentModel
from shared.models.cls_teacher import TeacherModel

@patch("shared.models.cls_teacher.TeacherModel", return_value=TeacherModel(6079, "Dave Russell", department=DepartmentModel(67, "Computer Science")))
class test_db__upsert_pathway_ks123_ids(TestCase):


    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()
        

    def tearDown(self):
        pass


    def test_should_raise_exception(self, mock_auth_user):
        # arrange
        expected_exception = KeyError("Bang!")

        model = LessonModel(0, "")

        with patch.object(ExecHelper, 'insert', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                LessonDataAccess._upsert_pathway_ks123_ids(self.fake_db, model, auth_user_id=99)
    
    
    def test_should_call__reinsert__pathway_ks123_ids(self, mock_auth_user):
         # arrange
        model = LessonModel(10, "")
        model.pathway_ks123_ids = ["201","202"]
        expected_result = []

        with patch.object(ExecHelper, 'insert', return_value=expected_result):
            # act

            actual_result = LessonDataAccess._upsert_pathway_ks123_ids(self.fake_db, model, [], auth_user_id=6079)
            
            # assert
            ExecHelper.insert.assert_called()

            ExecHelper.insert.assert_called_with(self.fake_db, 
             'lesson__insert_ks123_pathway'
             , (10, '202', 6079)
             , handle_log_info)

        self.assertEqual(actual_result, expected_result)
    