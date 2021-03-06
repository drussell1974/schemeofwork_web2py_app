from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.core.log_handlers import handle_log_info
from shared.models.cls_lesson import LessonDataAccess, LessonModel, handle_log_info
from tests.test_helpers.mocks import *

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_db__publish(TestCase):


    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()
        self.handle_log_info = MagicMock()
        
    def tearDown(self):
        pass


    def test_should_raise_exception(self, mock_auth_user):
        # arrange
        expected_exception = KeyError("Bang!")

        model = LessonModel(0, "")

        with patch.object(ExecHelper, 'update', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                LessonDataAccess.publish(self.fake_db, 1, 123, 99)


    def test_should_call__update(self, mock_auth_user):
         # arrange
        model = LessonModel(123, "CPU, RAM and ")
        
        expected_result = []

        with patch.object(ExecHelper, 'update', return_value=expected_result):
            # act

            actual_result = LessonDataAccess.publish(self.fake_db, 56, 13, 99)
            
            # assert

            ExecHelper.update.assert_called_with(self.fake_db, 
               'lesson__publish'
               , (56, 1, 99)
               , []
            )
            
            self.assertEqual(len(expected_result), len(actual_result))

