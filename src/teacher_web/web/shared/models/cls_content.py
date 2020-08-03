# -*- coding: utf-8 -*-
from .core.basemodel import BaseModel
from .core.db_helper import ExecHelper, sql_safe
from .core.log import handle_log_info


class ContentModel(BaseModel):
    def __init__(self, id_, description):
        self.id = id_
        self.description = description


    def _clean_up(self):
        """ clean up properties by removing by casting and ensuring safe for inserting etc """

        # id
        self.id = int(self.id)

        # trim description
        if self.description is not None:
            self.description = sql_safe(self.description)

    
    @staticmethod
    def get_options(db, key_stage_id):
        rows = ContentDataAccess.get_options(db, key_stage_id)
        data = []
        for row in rows:
            model = ContentModel(row[0], row[1])
            data.append(model)
        return data


class ContentDataAccess:

    @staticmethod
    def get_options(db, key_stage_id):

        execHelper = ExecHelper()

        str_select = "SELECT cnt.id as id, cnt.description as description FROM sow_content as cnt WHERE key_stage_id = {};".format(int(key_stage_id))

        try:
            rows = []
            rows = execHelper.execSql(db, str_select, rows, handle_log_info)
            last_sql = (str_select, "SUCCESS")
            return rows

        except Exception as e:
            last_sql = (str_select, "FAILED")
            raise Exception("Error getting content", e)
        