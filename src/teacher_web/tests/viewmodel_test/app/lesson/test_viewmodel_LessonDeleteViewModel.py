import json
from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, PropertyMock, patch
from app.lessons.viewmodels import LessonDeleteViewModel as ViewModel
from shared.models.cls_lesson import LessonModel as Model
from shared.models.enums.publlished import STATE


class test_viewmodel_LessonDeleteViewModel(TestCase):

    def setUp(self):        
        pass
        

    def tearDown(self):
        pass


    def test_init_called_delete__with_exception(self):
        
        # arrange        
        with patch.object(Model, "delete", side_effect=KeyError):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()
            
            with self.assertRaises(KeyError):
                # act
                self.viewmodel = ViewModel(db, auth_user=99, lesson_id=999)


    def test_init_called_delete__no_return_rows(self):
        
        # arrange
        
        data_to_return = None
        
        with patch.object(Model, "delete", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db=db, auth_user=99, lesson_id=101)

            # assert functions was called
            Model.delete.assert_called()
            self.assertIsNone(self.viewmodel.model)


    def test_init_called_delete__return_item(self):
        
        # arrange
        
        data_to_return = Model(912, "How to save the world in a day")
        data_to_return.published = STATE.DELETE

        
        with patch.object(Model, "delete", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Mock()

            # act
            self.viewmodel = ViewModel(db=db, auth_user=99, lesson_id=912)

            # assert functions was called
            Model.delete.assert_called()
            self.assertEqual(912, self.viewmodel.model.id)
            self.assertEqual("How to save the world in a day", self.viewmodel.model.title)
            self.assertEqual(STATE.DELETE, self.viewmodel.model.published)

