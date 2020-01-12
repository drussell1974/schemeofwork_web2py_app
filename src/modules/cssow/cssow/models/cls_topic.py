# -*- coding: utf-8 -*-
from django.db import models
from .core.db_helper import sql_safe, execSql

class TopicModel(models.Model):
    def __init__(self, id_, name, created = "", created_by = ""):
        self.id = id_
        self.name = name
        self.created = created
        self.created_by = created_by


    def _clean_up(self):
        """ clean up properties by removing by casting and ensuring safe for inserting etc """

        # id
        self.id = int(self.id)

        # name
        if self.name is not None:
            self.name = sql_safe(self.name)

"""
DAL
"""

def get_options(db, lvl, topic_id = 0):

    str_select = "SELECT id, name, created, created_by FROM sow_topic WHERE lvl = {lvl} and parent_id = {topic_id};"
    str_select = str_select.format(lvl=int(lvl), topic_id=int(topic_id))

    data = []

    try:

        rows = []
        execSql(db, str_select, rows)

        for row in rows:
            model = TopicModel(row[0], row[1], row[2], row[3])
            data.append(model.__dict__)

    except Exception as e:
        raise Exception("Error getting topics", e)


    return data
