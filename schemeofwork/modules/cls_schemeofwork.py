# -*- coding: utf-8 -*-
from basemodel import BaseModel


class SchemeOfWorkModel(BaseModel):
    name = ""
    description = ""
    exam_board_id = 0
    exam_board_name = ""
    key_stage_id = 0
    key_stage_name = ""


    def __init__(self, id_, name = "", description = "", exam_board_id = 0, exam_board_name = "", key_stage_id = 0, key_stage_name = "", created = "", created_by_id = 0, created_by_name = ""):
        self.id = int(id_)
        self.name = name
        self.description = description
        self.exam_board_id = self.try_int(exam_board_id)
        self.exam_board_name = exam_board_name if exam_board_id > 0 else ""
        self.key_stage_id = int(key_stage_id)
        self.key_stage_name = key_stage_name if key_stage_id > 0 else ""
        self.created = created
        self.created_by_id = int(created_by_id)
        self.created_by_name = created_by_name

    def try_int(self, val):
        try:
            val = int(val)
        except:
            val = None
        return val


    def validate(self):
        # set to True while validating
        self.is_valid = True
        self.validation_errors.clear()

        # Validate name

        if self.name is None or len(self.name) == 0:
            self.validation_errors["name"]= "required"
            self.is_valid = False
        elif len(self.name) > 25:
            self.validation_errors["name"] = "is {} characters (cannot exceed 25 characters)".format(len(self.name))
            self.is_valid = False

        # Validate description

        if len(self.description) > 1500:
            self.validation_errors["description"] = "is {} characters (cannot exceed 1500)".format(len(self.description))
            self.is_valid = False

        # Validate exam board
        if self.exam_board_id is not None:
            if self.exam_board_id < 1 or self.exam_board_id > 9999:
                self.validation_errors["exam_board_id"] = "{} is not a valid selection for exam board".format(self.exam_board_id)
                self.is_valid = False

        # Validate key stage
        if self.key_stage_id is None or self.key_stage_id < 1 or self.key_stage_id > 9999:
            self.validation_errors["key_stage_id"] = "{} is not a valid selection for key stage".format(self.key_stage_id)
            self.is_valid = False
