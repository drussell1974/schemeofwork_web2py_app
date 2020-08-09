import json
from datetime import datetime
from rest_framework import serializers, status
from django.http import Http404
from shared.models.core.log import handle_log_exception, handle_log_warning
from shared.models.core.basemodel import try_int
from shared.viewmodels.baseviewmodel import BaseViewModel
from shared.view_model import ViewModel
from shared.models.cls_content import ContentModel as Model
from shared.models.cls_keystage import KeyStageModel
from shared.models.cls_schemeofwork import SchemeOfWorkModel


class ContentIndexViewModel(BaseViewModel):
    
    def __init__(self, db, scheme_of_work_id, auth_user):
        """ determine and action request """
        
        self.scheme_of_work = SchemeOfWorkModel.get_model(db, scheme_of_work_id, auth_user)

        if self.scheme_of_work is None or self.scheme_of_work.is_from_db == False:
            self.on_not_found(self.scheme_of_work, scheme_of_work_id) 

        self.scheme_of_work_options = SchemeOfWorkModel.get_options(db, auth_user)

        # get model
        self.model = Model.get_all(db, self.scheme_of_work.key_stage_id, auth_user)
        

    def view(self):
        """ return View """

        data = {
            "scheme_of_work_id": self.scheme_of_work.id,
            "curriculum_content": self.model,
            "schemeofwork_options": self.scheme_of_work_options
        }

        return ViewModel("", self.scheme_of_work.name, "Curriculum", data=data)
        

class ContentEditViewModel(BaseViewModel):
    
    is_content_ready = False

    def __init__(self, db, request, scheme_of_work_id, content_id, auth_user):
        
        self.db = db
        self.scheme_of_work_id = scheme_of_work_id
        self.content_id = content_id
        self.auth_user = auth_user

        self.scheme_of_work = SchemeOfWorkModel.get_model(db, scheme_of_work_id, auth_user)
        #248 check associated schemeofwork 
        if self.scheme_of_work is None or self.scheme_of_work.is_from_db == False:
            self.on_not_found(self.scheme_of_work, content_id, scheme_of_work_id)

        if request.method == "GET":

            if content_id > 0:
                model = Model.get_model(self.db, content_id, scheme_of_work_id, self.auth_user)
                #248 check existing instance exists
                if model is None or model.is_from_db == False: 
                    self.on_not_found(self.scheme_of_work, content_id, scheme_of_work_id)
                self.model = model
            else:
                self.model = Model(
                    id_=0, 
                    description="", 
                    key_stage_id=self.scheme_of_work.key_stage_id,
                    created = datetime.now(),
                    created_by_id = request.user.id)

        elif request.method == "POST":
            
            published = request.POST["published"]

            self.model = Model().from_post(request.POST)

            self.model.validate()
            
            if self.model.is_valid == True or published == 2:
                # save to database

                data = Model.save(self.db, self.model, self.auth_user, published)
                self.model = data

                self.is_content_ready = True   

            else:
                handle_log_warning(self.db, "saving resource", "resource is not valid (id:{}, display_name:{}, validation_errors (count:{}).".format(self.model.id, self.model.display_name, len(self.model.validation_errors)))


    def view(self):
        
        #if self.content_id > 0 and self.model is None:            
        #    self.on_not_found(self.model, self.content_id) 

        self.key_stage_options = KeyStageModel.get_options(self.db)

        data = {
            "scheme_of_work_id":self.scheme_of_work.id,
            "key_stage_id":self.scheme_of_work.key_stage_id,
            "content_id":self.content_id,
            "model":self.model
        }

        return ViewModel("", self.scheme_of_work.name, "Edit: {}".format(self.model.description) if self.content_id > 0 else "New", data=data, active_model=self.model)