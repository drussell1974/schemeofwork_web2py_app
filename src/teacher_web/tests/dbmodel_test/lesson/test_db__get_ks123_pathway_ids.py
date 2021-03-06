from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_lesson import LessonModel, handle_log_info 
from shared.models.enums.publlished import STATE
from tests.test_helpers.mocks import *

# TODO: #329 - remove global references
get_ks123_pathway_objective_ids = LessonModel.get_ks123_pathway_objective_ids


@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_db__get_ks123_pathway_ids(TestCase):
    
    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()


    def tearDown(self):
        self.fake_db.close()


    def test__should_call_select__with_exception(self, mock_ctx):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'select', side_effect=expected_exception):
            # act and assert

            with self.assertRaises(Exception):
                get_ks123_pathway_objective_ids(self.fake_db, 21)


    def test__should_call_select__return_no_items(self, mock_ctx):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            rows = get_ks123_pathway_objective_ids(self.fake_db, 67, mock_ctx)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'lesson__get_ks123_pathway_objective_ids'
                , (67, int(STATE.PUBLISH), mock_ctx.auth_user_id)
                , []
                , handle_log_info)

            self.assertEqual(0, len(rows))


    def test__should_call_select__return_single_item(self, mock_ctx):
        # arrange
        expected_result = [("87",)]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            actual_results = get_ks123_pathway_objective_ids(self.fake_db, 87, mock_ctx)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'lesson__get_ks123_pathway_objective_ids'
                , (87, int(STATE.PUBLISH), mock_ctx.auth_user_id)
                , []
                , handle_log_info)

            self.assertEqual(1, len(actual_results))

            self.assertEqual(87, actual_results[0])


    def test__should_call_select__return_multiple_item(self, mock_ctx):
        # arrange
        expected_result = [("1034",),("1045",),("12",)]


        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            actual_results = get_ks123_pathway_objective_ids(self.fake_db, 21, mock_ctx)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'lesson__get_ks123_pathway_objective_ids'
                , (21, int(STATE.PUBLISH), mock_ctx.auth_user_id)
                , []
                , handle_log_info)
            
            self.assertEqual(1034, actual_results[0])
            self.assertEqual(12, actual_results[2])
