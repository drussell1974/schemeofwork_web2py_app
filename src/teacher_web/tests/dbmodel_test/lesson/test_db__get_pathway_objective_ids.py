from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_lesson import LessonModel, handle_log_info
from tests.test_helpers.mocks import *

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
@patch.object(TeacherPermissionModel, "get_model", return_value=fake_teacher_permission_model())
class test_db__get_pathway_objective_ids(TestCase):
    
    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()

    def tearDown(self):
        self.fake_db.close()


    def test__should_call_select__with_exception(self, mock_auth_user, mock_teacher_permission):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'select', side_effect=expected_exception):
            # act and assert

            with self.assertRaises(Exception):
                LessonModel.get_pathway_objective_ids(self.fake_db, 21)


    def test__should_call_select__return_no_items(self, mock_auth_user, mock_teacher_permission):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            rows = LessonModel.get_pathway_objective_ids(self.fake_db, 67, mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'lesson__get_pathway_objective_ids'
                , (67, mock_auth_user.auth_user_id)
                , []
                , handle_log_info)
            self.assertEqual(0, len(rows))


    def test__should_call_select__return_single_item(self, mock_auth_user, mock_teacher_permission):
        # arrange

        with patch.object(ExecHelper, 'select', return_value=[("87",)]):
            # act

            actual_results = LessonModel.get_pathway_objective_ids(self.fake_db, 87, mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
            'lesson__get_pathway_objective_ids'
            , (87, mock_auth_user.auth_user_id)
            , []
            , handle_log_info)

            self.assertEqual(1, len(actual_results))

            self.assertEqual(87, actual_results[0])


    def test__should_call_select__return_multiple_item(self, mock_auth_user, mock_teacher_permission):
        # arrange

        with patch.object(ExecHelper, 'select', return_value=[("1034",),("1045",),("12",) ]):
            # act

            actual_results = LessonModel.get_pathway_objective_ids(self.fake_db, 21, fake_ctx_model())
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'lesson__get_pathway_objective_ids'
                , (21, 6079)
                , []
                , handle_log_info)
            
            self.assertEqual(1034, actual_results[0])
            self.assertEqual(12, actual_results[2])
