from unittest import TestCase, skip
from unittest.mock import MagicMock, Mock, patch

# test context

from app.learningobjectives.viewmodels import LearningObjectiveDeleteUnpublishedViewModel as ViewModel
from shared.models.cls_learningobjective import LearningObjectiveModel as Model


class test_viewmodel_DeleteUnpublishedViewModel(TestCase):

    def setUp(self):        
        pass
        

    def tearDown(self):
        pass


    def test_should_call_delete_unpublished(self):
        
        # arrange
        
        data_to_return = Model(56)
        
        with patch.object(Model, "delete_unpublished", return_value=data_to_return):

            db = MagicMock()
            db.cursor = MagicMock()

            self.mock_model = Model(56)

            # act
            self.viewmodel = ViewModel(db=db, lesson_id=56, scheme_of_work_id=13, auth_user=99)

            # assert functions was called
            Model.delete_unpublished.assert_called()
