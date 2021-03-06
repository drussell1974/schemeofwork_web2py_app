from shared.viewmodels.baseviewmodel import BaseViewModel
from shared.models.core.context import Ctx
from shared.models.cls_lesson import LessonModel
from shared.serializers.srl_lesson import LessonModelSerializer

class LessonGetAllViewModel(BaseViewModel):
    
    def __init__(self, db, scheme_of_work_id, auth_user):

        self.db = db
        
        # get model
        data = LessonModel.get_all(self.db, scheme_of_work_id, auth_user)
        
        srl_list = list(map(lambda m: LessonModelSerializer(m).data, data))
        self.model = srl_list


class LessonGetModelViewModel(BaseViewModel):

    def __init__(self, db, lesson_id, scheme_of_work_id, auth_user, resource_type_id = 0):
        self.db = db
        
        # get model
        model = LessonModel.get_model(self.db, lesson_id, scheme_of_work_id, auth_user, resource_type_id)
        #248 check existing instance exists
        if model is None or model.is_from_db == False:
            self.on_not_found(model, lesson_id, scheme_of_work_id)
        else:
            srl = LessonModelSerializer(model)
            self.model = srl.data

