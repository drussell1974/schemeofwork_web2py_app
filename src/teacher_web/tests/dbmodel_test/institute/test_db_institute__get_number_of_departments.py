from unittest import TestCase
from shared.models.cls_institute import InstituteModel as Model, handle_log_info
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from tests.test_helpers.mocks import *

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_InstituteDataAccess__get_number_of_departments(TestCase):

    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()


    def tearDown(self):
        self.fake_db.close()


    def test__should_call__scalar__with_exception(self, mock_ctx):

        # arrange
        expected_result = Exception('Bang')
        
        with patch.object(ExecHelper, "scalar", side_effect=expected_result):
            # act and assert
            with self.assertRaises(Exception):
                Model.get_number_of_departments(self.fake_db, key_stage_id = 4)
            

    def test__should_call__scalar__no_items(self, mock_ctx):
        # arrange
        expected_result = (0,)

        with patch.object(ExecHelper, "scalar", return_value=expected_result):
                
            # act
            
            rows = Model.get_number_of_departments(self.fake_db, 578, auth_user = mock_ctx)
            
            # assert

            ExecHelper.scalar.assert_called_with(self.fake_db,
                'institute__get_number_of_departments'
                , []
                , handle_log_info
                , (578, mock_ctx.auth_user_id,))

            self.assertEqual(0, rows)


    def test__should_call__scalar__single_items(self, mock_ctx):
        # arrange
        expected_result = (1,)
        
        with patch.object(ExecHelper, "scalar", return_value=expected_result):
            
            # act

            rows = Model.get_number_of_departments(self.fake_db, 564654, auth_user = mock_ctx)
            
            # assert

            ExecHelper.scalar.assert_called_with(self.fake_db, 
                'institute__get_number_of_departments'
                , []
                , handle_log_info
                , (564654, mock_ctx.auth_user_id,))


            self.assertEqual(1, rows)
            

    def test__should_call__scalar__multiple_items(self, mock_ctx):
        # arrange
        expected_result = (3,)
        
        with patch.object(ExecHelper, "scalar", return_value=expected_result):
            # act
            result = Model.get_number_of_departments(self.fake_db, 82323, auth_user = mock_ctx)
            
            # assert

            ExecHelper.scalar.assert_called_with(self.fake_db, 
                'institute__get_number_of_departments'
                , []
                , handle_log_info
                , (82323, mock_ctx.auth_user_id,))
            
            self.assertEqual(3, result)
