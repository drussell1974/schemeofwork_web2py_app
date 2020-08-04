from unittest import TestCase
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper
from shared.models.cls_keyword import KeywordModel
from shared.models.cls_lesson import LessonModel, LessonDataAccess, handle_log_info

_upsert_key_words = LessonDataAccess._upsert_key_words


class test_db___upsert_key_words(TestCase):


    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()
        

    def tearDown(self):
        pass


    def test_should_raise_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        model = LessonModel(0, "")

        with patch.object(ExecHelper, 'execCRUDSql', side_effect=expected_exception):
            
            # act and assert
            with self.assertRaises(Exception):
                # act 
                _upsert_key_words(self.fake_db, model, auth_user_id=99)


    def test_should_call_execCRUDSql__delete_only__when__no__key_words(self):
         # arrange
        model = LessonModel(101, "")
        
        expected_result = 1

        with patch.object(ExecHelper, 'execCRUDSql', return_value=expected_result):
            # act

            actual_result = _upsert_key_words(self.fake_db, model, [], auth_user_id=99)
            
            # assert
            ExecHelper.execCRUDSql.assert_called()

            ExecHelper.execCRUDSql.assert_called_with(self.fake_db, 
             "DELETE FROM sow_lesson__has__key_words WHERE lesson_id = 101;"
             , []
             , log_info=handle_log_info)

        self.assertEqual(actual_result, expected_result)
    
    
    def test_should_call_execCRUDSql__reinsert__key_words(self):
         # arrange
        model = LessonModel(10, "")
        
        model.key_words = [
            KeywordModel(id_=12, term="CPU", definition=""), 
            KeywordModel(id_=13, term="FDE", definition="")
        ]
        
        expected_rows = []

        with patch.object(ExecHelper, 'execCRUDSql', return_value=expected_rows):
            # act

            actual_result = _upsert_key_words(self.fake_db, model, [], auth_user_id=99)
            
            # assert
            ExecHelper.execCRUDSql.assert_called()

            ExecHelper.execCRUDSql.assert_called_with(self.fake_db, 
             "DELETE FROM sow_lesson__has__key_words WHERE lesson_id = 10;" \
                "INSERT INTO sow_lesson__has__key_words (lesson_id, key_word_id) VALUES (10, 12);" \
                "INSERT INTO sow_lesson__has__key_words (lesson_id, key_word_id) VALUES (10, 13);"
             , []
             , log_info=handle_log_info)

        self.assertEqual([], actual_result)

    
    
    def test_should_call_execCRUDSql__reinsert__key_words__insert_new(self):
         # arrange
        model = LessonModel(79, "")
        model.key_words = [KeywordModel(id_ = 12, term="CPU", definition="")]
        
        expected_result = []

        with patch.object(ExecHelper, 'execCRUDSql', return_value=[]):
            # act

            actual_result = _upsert_key_words(self.fake_db, model, [], auth_user_id=99)
            
            # assert
            ExecHelper.execCRUDSql.assert_called()

            ExecHelper.execCRUDSql.assert_called_with(self.fake_db, 
             "DELETE FROM sow_lesson__has__key_words WHERE lesson_id = 79;" \
                "INSERT INTO sow_lesson__has__key_words (lesson_id, key_word_id) VALUES (79, 12);"
             , []
             , log_info=handle_log_info)

        self.assertEqual(actual_result, expected_result)
    