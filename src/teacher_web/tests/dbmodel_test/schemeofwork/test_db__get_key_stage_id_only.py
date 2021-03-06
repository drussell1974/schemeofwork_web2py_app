from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_schemeofwork import SchemeOfWorkModel, handle_log_info
from tests.test_helpers.mocks import *

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_db__get_key_stage_id_only(TestCase):
    
    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()

    def tearDown(self):
        self.fake_db.close()


    def test__should_call__select__with_exception(self, mock_auth_user):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'select', side_effect=expected_exception):
            # act and assert

            with self.assertRaises(Exception):
                SchemeOfWorkModel.get_key_stage_id_only(self.fake_db, 999, 99)


    def test__should_call__select__return_no_items(self, mock_auth_user):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            actual_result = SchemeOfWorkModel.get_key_stage_id_only(self.fake_db, 101, mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                "scheme_of_work__get_key_stage_id_only"
                , (101, mock_auth_user.department_id, mock_auth_user.institute_id, mock_auth_user.auth_user_id)
                , []
                , handle_log_info)
            self.assertEqual(0, actual_result)


    def test__should_call__select__return_single_item(self, mock_auth_user):
        # arrange
        expected_result = [[3]]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            actual_result = SchemeOfWorkModel.get_key_stage_id_only(self.fake_db, 6, mock_auth_user)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                "scheme_of_work__get_key_stage_id_only"
                , (6, mock_auth_user.department_id, mock_auth_user.institute_id,  mock_auth_user.auth_user_id)
                , []
                , handle_log_info)
            self.assertEqual(3, actual_result)
