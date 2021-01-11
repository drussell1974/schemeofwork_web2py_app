from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, PropertyMock, patch

# test context

from app.schemesofwork.viewmodels import SchemeOfWorkEditViewModel as ViewModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel as Model
from shared.models.cls_keyword import KeywordModel
from shared.viewmodels.decorators.permissions import TeacherPermissionModel

class test_viewmodel_EditViewModel(TestCase):

    def setUp(self):
        pass
        

    def tearDown(self):
        pass


    @patch.object(TeacherPermissionModel, "check_permission", return_value=True)
    def test_execute_called_save__add_model_to_data(self, check_permission):
        
        # arrange

        mock_request = Mock()
        mock_request.method = "POST"
        mock_request.POST = {
                    "id": 99,
                    "name":"Proin id massa metus. Aliqua tincidunt.",
                    "description": "Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur",
                    "exam_board_id": 56,
                    "key_stage_id": 5,
                    "lesson_id": 230
                }

        mock_db = MagicMock()
        mock_db.cursor = MagicMock()

        on_save__data_to_return = Model(99, "Proin id massa metus. Aliqua tincidunt.")
        
        with patch.object(Model, "save", return_value=on_save__data_to_return):

            # act

            test_context = ViewModel(db=mock_db, request=mock_request, scheme_of_work_id=99, auth_user=99)
            test_context.model.key_words.clear()
            
            # assert 

            self.assertEqual("", test_context.error_message)
            self.assertTrue(test_context.saved)
            
            Model.save.assert_called()

            self.assertEqual(99, test_context.model.id)
            self.assertEqual("Proin id massa metus. Aliqua tincidunt.", test_context.model.name)
            self.assertEqual([], test_context.model.key_words)


    @patch.object(TeacherPermissionModel, "check_permission", return_value=True)
    def test_execute_called_save__add_model_to_data__with_keywords(self, check_permission):
        
        # arrange
        mock_request = Mock()
        mock_request.method = "POST"
        mock_request.POST = {
                    "id": 99,
                    "name":"Proin id massa metus. Aliqua tinciduntx.",
                    "description": "Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur",
                    "exam_board_id": 56,
                    "key_stage_id": 5,
                    "lesson_id": 230
                }


        on_save__data_to_return = Model(99, "Proin id massa metus. Aliqua tinciduntx.")
        
        with patch("app.default.viewmodels.KeywordSaveViewModel") as save_keyword:
            with patch.object(Model, "save", return_value=on_save__data_to_return):


                return_keyword_model = KeywordModel(123, "RAM")
                return_keyword_model.is_valid = True

                # act
                save_keyword.execute = Mock(return_value=return_keyword_model)
                save_keyword.model = return_keyword_model

                mock_db = MagicMock()
                mock_db.cursor = MagicMock()

                test_context = ViewModel(db=mock_db, request=mock_request, scheme_of_work_id=99, auth_user=99)
                
                # assert 
                self.assertEqual("", test_context.error_message)

                Model.save.assert_called()

                self.assertEqual(99, test_context.model.id)
                self.assertEqual("Proin id massa metus. Aliqua tinciduntx.", test_context.model.name)


    @patch.object(TeacherPermissionModel, "check_permission", return_value=True)
    def test_execute_called_save__add_model_to_data__return_invalid(self, check_permission):
         
        # arrange

        mock_request = Mock()
        mock_request.method = "POST"
        mock_request.POST = {
                    "id": 99,
                    "name":"Suspendisse nisi dui, lobortis ut",
                    "description": "unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo.",
                    "exam_board_id": 0,
                    "key_stage_id": 3,
                    "lesson_id": 0,
                    "key_words":  '[{"id": 0, "term": "CPU", "definition": "", "published":1}, {"id": 123, "term": "RAM", "definition": "", "published":1}]'
                }

        with patch("app.default.viewmodels.KeywordSaveViewModel") as save_keyword:
            with patch.object(Model, "save", return_value=None):
                    
                # act
                
                return_keyword_model = KeywordModel(4, term="Four")
                return_keyword_model.is_valid = True

                save_keyword.execute = Mock(return_value=return_keyword_model)
                save_keyword.model = return_keyword_model

                mock_db = MagicMock()
                mock_db.cursor = MagicMock()

                test_context = ViewModel(db=mock_db, request=mock_request, scheme_of_work_id=99, auth_user=99)

                # assert 

                self.assertEqual("", test_context.error_message)
                self.assertEqual("validation errors {'exam_board_id': '0 is not a valid range'}", test_context.alert_message)
                self.assertFalse(test_context.saved)

                Model.save.assert_not_called()

                # return the invalid object
                self.assertEqual(99, test_context.model.id)
                self.assertEqual("Suspendisse nisi dui, lobortis ut", test_context.model.name)
                #self.assertEqual(0, test_context.model.lesson_id)
                self.assertFalse(test_context.model.is_valid)
                self.assertEqual(1, len(test_context.model.validation_errors)) 
                self.assertEqual({'exam_board_id': '0 is not a valid range'}, test_context.model.validation_errors) 


    @patch.object(TeacherPermissionModel, "check_permission", return_value=False)
    def test_should_raise_PermissionError(self, check_permission):
        
        # arrange
        
        mock_db = MagicMock()
        mock_db.cursor = MagicMock()

        mock_request = Mock()
        mock_request.method = "POST"
        mock_request.POST = {
                    "id": 99,
                    "name":"Proin id massa metus. Aliqua tinciduntx.",
                    "description": "Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur",
                    "exam_board_id": 56,
                    "key_stage_id": 5,
                    "lesson_id": 230
                }

        # assert
        with self.assertRaises(PermissionError):
    
            # act
            ViewModel(db=mock_db, request=mock_request, scheme_of_work_id=99, auth_user=99)
            

