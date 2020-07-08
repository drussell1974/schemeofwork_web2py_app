# -*- coding: utf-8 -*-
from .core.basemodel import BaseModel
from .core.db_helper import sql_safe, execSql

class KS123PathwayModel(BaseModel):
    def __init__(self, id_, objective):
        self.id = id_
        self.objective = objective
        self.is_checked = False


    def _clean_up(self):
        """ clean up properties by removing by casting and ensuring safe for inserting etc """

        # id
        self.id = int(self.id)

        # objective
        if self.objective is not None:
            self.objective = sql_safe(self.objective)

"""
DAL
"""

def get_options(db, year_id, topic_id):

    str_select = "SELECT id, objective FROM sow_ks123_pathway WHERE year_id = {year_id} and topic_id = {topic_id};"\
        .format(year_id=year_id, topic_id=topic_id)

    rows = []
    execSql(db, str_select, rows)

    data = []

    for row in rows:
        model = KS123PathwayModel(row[0], row[1])
        data.append(model)

    return data


def get_linked_pathway_ks123(db, lesson_id):

    select_sql = "SELECT"\
                 " pw.id as id,"\
                 " pw.objective as objective "\
                 "FROM sow_lesson__has__ks123_pathway as le_pw" \
                 " INNER JOIN sow_ks123_pathway AS pw ON pw.id = le_pw.ks123_pathway_id"\
                 " WHERE le_pw.lesson_id = {lesson_id};"

    select_sql = select_sql.format(lesson_id=int(lesson_id))

    rows = []
    execSql(db, select_sql, rows)

    data = []

    for row in rows:
        data.append([int(row[0]), row[1]])

    return data