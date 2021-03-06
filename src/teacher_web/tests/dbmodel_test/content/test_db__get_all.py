from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_content import ContentModel, handle_log_info
from tests.test_helpers.mocks import *

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_db__get_all(TestCase):


    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()

    def tearDown(self):
        self.fake_db.close()


    def test__should_call_select_with_exception(self, mock_ctx):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'select', side_effect=expected_exception):
            # act and assert

            with self.assertRaises(Exception):
                ContentModel.get_all(self.fake_db)


    def test__should_call_select_return_no_items(self, mock_ctx):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            rows = ContentModel.get_all(self.fake_db, scheme_of_work_id=34, key_stage_id=7, auth_user=mock_ctx)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'content__get_all'
                , (34, 7, mock_ctx.auth_user_id)
                , []
                , handle_log_info)
                
            self.assertEqual(0, len(rows))


    def test__should_call_select_return_single_item(self, mock_ctx):
        # arrange
        expected_result = [
            (702, "purus lacus, ut volutpat nibh euismod.", "A",0)
            ]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            actual_results = ContentModel.get_all(self.fake_db, scheme_of_work_id=34, key_stage_id=5, auth_user=mock_ctx)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'content__get_all'
                , (34, 5, mock_ctx.auth_user_id)
                , []
                , handle_log_info)
                

            self.assertEqual(1, len(actual_results))

            self.assertEqual(702, actual_results[0].id)
            self.assertEqual("purus lacus, ut volutpat nibh euismod.", actual_results[0].description)
            self.assertEqual("A", actual_results[0].letter_prefix),


    def test__should_call_select_return_multiple_item(self, mock_ctx):
        # arrange
        expected_result = [
            (1021, "nec arcu nec dolor vehicula ornare non.", "X", 0),
            (1022, "purus lacus, ut volutpat nibh euismod.", "Y", 0),
            (1023, "rutrum lorem a arcu ultrices, id mollis", "Z", 0)
        ]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            actual_results = ContentModel.get_all(self.fake_db,  scheme_of_work_id=34,key_stage_id=5, auth_user=mock_ctx)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                'content__get_all'
                , (34, 5, mock_ctx.auth_user_id)
                , []
                , handle_log_info)

            self.assertEqual(3, len(actual_results))

            self.assertEqual(1021, actual_results[0].id)
            self.assertEqual("X", actual_results[0].letter_prefix),
            self.assertEqual("nec arcu nec dolor vehicula ornare non.", actual_results[0].description)
            

            self.assertEqual(1023, actual_results[2].id)
            self.assertEqual("Z", actual_results[2].letter_prefix),
            self.assertEqual("rutrum lorem a arcu ultrices, id mollis", actual_results[2].description)
