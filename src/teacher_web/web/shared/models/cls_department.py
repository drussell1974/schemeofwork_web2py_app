from .core.basemodel import BaseModel
from .core.db_helper import ExecHelper, sql_safe
from shared.models.core.log_handlers import handle_log_info
from shared.models.core.basemodel import BaseModel, BaseContextModel
from shared.models.cls_institute import InstituteModel, InstituteContextModel
from shared.models.enums.publlished import STATE
from shared.models.utils.cache_proxy import CacheProxy

class DepartmentContextModel(BaseContextModel):
    
    name = ""

    def __init__(self, id_, name, description = "", hod_id = 0, created = "", created_by_id = 0, created_by_name = "", published=STATE.PUBLISH, is_from_db=False, ctx=None):
        super().__init__(id_, display_name=name, created=created, created_by_id=created_by_id, created_by_name=created_by_name, published=published, is_from_db=is_from_db, ctx=ctx)
        self.name = name
        self.hod_id = hod_id


    @classmethod
    def empty(cls, published=STATE.DRAFT, ctx=None):
        model = cls(id_=0, name="", published=published, ctx=ctx)
        return model


    @classmethod
    def get_context_model(cls, db, institute_id, department_id, auth_user_id):
        empty_model = cls.empty()

        result = BaseContextModel.get_context_model(db, empty_model, "department__get_context_model", handle_log_info, institute_id, department_id)
        result.institute_id = institute_id
        result.department_id = department_id
        
        return result if result is not None else None


    @classmethod
    def cached(cls, request, db, institute_id, department_id, auth_user_id):

        department = cls.empty()

        cache_obj = CacheProxy.session_cache(request, db, "department", cls.get_context_model, institute_id, department_id, auth_user_id)

        if cache_obj is not None:
            department.from_dict(cache_obj)    

        return department


class DepartmentModel(DepartmentContextModel):

    # default values for api
    name = ""
    description = ""
    number_of_schemes_of_work = 0
    institute_id = 0

    def __init__(self, id_, name, institute, description = "", hod_id = 0, created = "", created_by_id = 0, created_by_name = "", published=STATE.PUBLISH, is_from_db=False, ctx=None):
        super().__init__(id_, name=name, hod_id=hod_id, created=created, created_by_id=created_by_id, created_by_name=created_by_name, published=published, is_from_db=is_from_db, ctx=ctx)
        
        self.description = description
        self.institute = institute
        self.number_of_schemes_of_work = 0
        

    def validate(self, skip_validation = []):
        """ clean up and validate model """
        super().validate(skip_validation)

        # Validate name
        self._validate_required_string("name", self.name, 1, 70)
        self._validate_optional_string("description", self.description, 5000)

        self.on_after_validate()


    def _clean_up(self):
        """ clean up properties by removing by casting and ensuring safe for inserting etc """

        # id
        self.id = int(self.id)

        # name
        if self.name is not None:
            self.name = sql_safe(self.name)

        # description
        if self.description is not None:
            self.description = sql_safe(self.description)


    @staticmethod
    def get_all(db, institute_id, auth_user):
        
        rows = DepartmentDataAccess.get_all(db=db, institute_id=institute_id, show_published_state=auth_user.can_view, auth_user_id=auth_user.auth_user_id)
        data = []
        for row in rows: 
            model = DepartmentModel(id_=row[0],
                                    name=row[1],
                                    institute=InstituteModel(id_=row[2], name=row[5]), # TODO: #329 use institute name
                                    created=row[3],                                                                                                                                                                                                                         
                                    created_by_id=row[4],
                                    created_by_name=row[5],
                                    published=row[6])

            model.institute_id = row[2]

            model.number_of_schemes_of_work = DepartmentModel.get_number_of_schemes_of_work(db, model.id, auth_user)

            data.append(model)
        return data


    @staticmethod
    def get_model(db, department_id, auth_user):   
        
        rows = DepartmentDataAccess.get_model(db, department_id, show_published_state=auth_user.can_view, auth_user_id=auth_user.auth_user_id)

        model = DepartmentModel(0, "", institute=InstituteModel(0, ""))
        for row in rows:

            model = DepartmentModel(id_=row[0],
                                    name=row[1],
                                    hod_id=row[2],
                                    institute=InstituteModel(id_=row[3], name=row[4]), # TODO: #323 use context institute name
                                    created=row[5],
                                    created_by_id=row[6],
                                    created_by_name=row[7],
                                    published=row[8])
            model.institute_id = row[3]
            model.number_of_schemes_of_work = DepartmentModel.get_number_of_schemes_of_work(db, model.id, auth_user)
            
            model.on_fetched_from_db()         
        return model
    

    @staticmethod
    def get_options(db, auth_user):
        rows = DepartmentDataAccess.get_options(db, auth_user_id=auth_user.auth_user_id)
        data = []
        
        for row in rows:
            # TODO: 323 get institute_name
            model = DepartmentModel(row[0], row[1], institute=InstituteModel(auth_user.institute_id, name=""))
            data.append(model)
        return data


    @staticmethod
    def get_number_of_schemes_of_work(db, department_id, auth_user):
        scalar_result = DepartmentDataAccess.get_number_of_schemes_of_work(db, department_id, auth_user.auth_user_id)
        return scalar_result


    @staticmethod
    def save(db, model, teacher_id, auth_user):
        """ save model """
        if model.published == STATE.DELETE:
            data = DepartmentDataAccess._delete(db, model, auth_user.auth_user_id)
        elif model.is_valid == True:
            if model.is_new():
                data = DepartmentDataAccess._insert(db, model, teacher_id, institute_id=auth_user.institute_id, auth_user_id=auth_user.auth_user_id)
                model.id = data[0]
            else:
                data = DepartmentDataAccess._update(db, model, teacher_id, auth_user_id=auth_user.auth_user_id)

        return model


    @staticmethod
    def delete_unpublished(db, institute_id, auth_user):
        rows = DepartmentDataAccess.delete_unpublished(db, institute_id, auth_user_id=auth_user.auth_user_id)
        return rows


    @staticmethod
    def publish_by_id(db, department_id, auth_user):
        return DepartmentDataAccess.publish(db=db, auth_user_id=auth_user.auth_user_id, id_=department_id)      


class DepartmentDataAccess:
    
    @staticmethod
    def get_model(db, id_, auth_user_id, show_published_state = STATE.PUBLISH):
        """
        get scheme of work

        :param db: database context
        :param id_: department identifier
        :param auth_user_id: the user executing the command
        """

        execHelper = ExecHelper()

        select_sql = "department__get"
        params = (id_, int(show_published_state), auth_user_id)

        rows = []
        rows = execHelper.select(db, select_sql, params, rows, handle_log_info)
        return rows


    @staticmethod
    def get_all(db, institute_id, show_published_state, auth_user_id):
        """
        get all inistutions
        """
        
        execHelper = ExecHelper()
        
        select_sql = "department__get_all" 
        params = (institute_id, int(show_published_state), auth_user_id,)

        rows = []
        rows = execHelper.select(db, select_sql, params, rows, handle_log_info)

        return rows


    @staticmethod
    def get_options(db, auth_user_id):
        
        execHelper = ExecHelper()

        str_select = "department__get_options"
        params = (auth_user_id,)

        try:
            rows = []
            rows = execHelper.select(db, str_select, params, rows, handle_log_info)
            
            return rows

        except Exception as e:
            raise Exception("Error getting departments", e)
          
    @staticmethod
    def get_number_of_schemes_of_work(db, department_id, auth_user_id):
        execHelper = ExecHelper()
        execHelper.begin(db)
        
        select_sql = "department__get_number_of_schemes_of_work"
        params = (department_id, auth_user_id)

        result = []
        result = execHelper.scalar(db, select_sql, result, handle_log_info, params)

        if result is not None and len(result) > 0:
            result = result[0]
        return result


    @staticmethod
    def _insert(db, model, teacher_id, institute_id, auth_user_id):
        """ inserts the sow_department """
        execHelper = ExecHelper()

        sql_insert_statement = "department__insert"
        params = (
            model.id,
            model.name,
            teacher_id,
            institute_id,
            model.created,
            auth_user_id,
            int(model.published),
        )
               
        result = execHelper.insert(db, sql_insert_statement, params, handle_log_info)

        return result


    @staticmethod
    def _update(db, model, teacher_id, auth_user_id):
        """ updates the sow_department """
        
        execHelper = ExecHelper()
        
        str_update = "department__update"
        params = (
            model.id,
            model.name,
            model.institute.id,
            int(model.published),
            auth_user_id
        )
        
        result = execHelper.update(db, str_update, params, handle_log_info)

        return result


    @staticmethod
    def _delete(db, model, auth_user_id):

        execHelper = ExecHelper()

        sql = "department__delete"
        params = (model.id, auth_user_id)
    
        #271 Stored procedure
        rows = execHelper.delete(db, sql, params, handle_log_info)
        
        return rows


    @staticmethod
    def delete_unpublished(db, institute_id, auth_user_id):
        """ Delete all unpublished departments """

        execHelper = ExecHelper()
        
        str_delete = "department__delete_unpublished"
        params = (institute_id, auth_user_id)
            
        rval = execHelper.delete(db, str_delete, params, handle_log_info)
        return rval


    @staticmethod
    def publish(db, auth_user_id, id_):
        
        model = DepartmentModel(id_, "", institute=InstituteModel(0, ""))
        model.publish = True

        execHelper = ExecHelper()

        str_update = "department__publish"
        params = (model.id, model.published, auth_user_id)

        rval = []
        rval = execHelper.update(db, str_update, params, handle_log_info)

        return rval