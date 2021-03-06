from unittest.mock import Mock, MagicMock, patch
from unittest import TestCase, skip
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_keyword import KeywordModel, handle_log_info
from shared.models.enums.publlished import STATE
from tests.test_helpers.mocks import *

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_db_keyword__get_options(TestCase):
    
    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()
        KeywordModel.handle_log_info = MagicMock()

    def tearDown(self):
        self.fake_db.close()


    def test__should_call_select__with_exception(self, mock_auth_user):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'select', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                KeywordModel.get_options(self.fake_db)


    def test__should_call_select__return_no_items(self, mock_auth_user):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            rows = KeywordModel.get_options(self.fake_db, 13, mock_auth_user)
            
            # assert
            ExecHelper.select.assert_called_with(self.fake_db,
                'keyword__get_options'
                , (13, 0, int(STATE.PUBLISH), mock_auth_user.auth_user_id)
                , []
                , handle_log_info)

            self.assertEqual(0, len(rows))


    def test__should_call_select__return_single_item(self, mock_auth_user):
        # arrange
        expected_result = [(123, "Binary", "Donec porta efficitur metus, eget consequat ligula maximus eget. Nunc imperdiet sapien sit amet arcu fermentum maximus.", 13, 1, 2, '2020-01-24 07:30:01')]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            rows = KeywordModel.get_options(self.fake_db, 13, mock_auth_user, 777)
            
            # assert
            ExecHelper.select.assert_called_with(self.fake_db,
                'keyword__get_options'
                , (13, 777, int(STATE.PUBLISH), mock_auth_user.auth_user_id)
                , []
                , handle_log_info)
                
            self.assertEqual(1, len(rows))
            self.assertEqual("Binary", rows[0].term)
            self.assertEqual("Donec porta efficitur metus, eget consequat ligula maximus eget. Nunc imperdiet sapien sit amet arcu fermentum maximus.", rows[0].definition)
            self.assertEqual(13, rows[0].scheme_of_work_id)
            self.assertEqual(2, rows[0].number_of_lessons)            


    def test__should_call_select__return_multiple_item(self, mock_auth_user):
        # arrange
        expected_result = [
                (1, "Binary", "Phasellus vitae pretium neque, ut mattis mi.", 13, 0, [], '2020-01-24')
                ,(2,"Decimal", "Donec porta efficitur metus, eget consequat ligula maximus eget. Nunc imperdiet sapien sit amet arcu fermentum maximus.", 13, '2020-01-24 07:32:01', 0, [], 0, '2020-01-24 07:42.01')
                ,(3, "Hexadecimal", "Phasellus mauris lacus, accumsan non viverra non, sagittis nec lorem. Vestibulum tristique laoreet nisi non congue.", 13, '2020-01-24 07:32:02', 1, [123], 1, '2020-01-24 07.42.02')
            ]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            rows = KeywordModel.get_options(self.fake_db, 13, mock_auth_user)
            # assert
            ExecHelper.select.assert_called_with(self.fake_db,
                'keyword__get_options'
                , (13, 0, int(STATE.PUBLISH), mock_auth_user.auth_user_id)
                , []
                , handle_log_info)
            self.assertEqual(3, len(rows))

            self.assertEqual("Binary", rows[0].term)
            self.assertEqual("Hexadecimal", rows[2].term)
