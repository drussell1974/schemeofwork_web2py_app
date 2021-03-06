from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.core.log_handlers import handle_log_info
from shared.models.cls_keyword import KeywordModel as Model
from shared.models.enums.publlished import STATE
from tests.test_helpers.mocks import *

@patch("shared.models.core.django_helper", return_value=fake_ctx_model())
class test_db__save__lesson(TestCase):
    

    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()
        
        
    def tearDown(self):
        pass


    def test_should_raise_exception(self, mock_auth_user):
        # arrange
        expected_exception = KeyError("Bang!")

        model = Model(0, term="", definition="Mauris ac velit ultricies, vestibulum.")
        model.published = STATE.PUBLISH
        model.is_new = Mock(return_value=True)

        with patch.object(ExecHelper, 'insert', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(KeyError):
                # act 
                Model.save(self.fake_db, model, lesson_id=0, auth_user=mock_auth_user)


    def test_should_call__upsert__when__is_new__true(self, mock_auth_user):
        # arrange

        model = Model(0, term="Mauris", definition="Mauris ac velit ultricies, vestibulum.", scheme_of_work_id=13)
        model.published = STATE.PUBLISH
        model.is_new = MagicMock(return_value=True)
        model.is_valid = MagicMock(return_value=True)
        
        model.belongs_to_lessons.append(10)

        expected_result = ([], "100")

        with patch.object(ExecHelper, 'insert', return_value=expected_result):
            # act

            actual_result = Model.save(self.fake_db, model, lesson_id=0, auth_user=mock_auth_user)

            # assert

            ExecHelper.insert.assert_called_with(
                self.fake_db,
                'lesson__insert_keywords'
                , ([], 10, 13, mock_auth_user.auth_user_id)
                , handle_log_info)
                
            self.assertNotEqual(0, actual_result.id)

