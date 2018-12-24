# -*- coding: utf-8 -*-
from datetime import datetime
from gluon.contrib.appconfig import AppConfig

"""configuration = AppConfig(reload=True)
db = DAL(configuration.get('db.uri'),
     pool_size=configuration.get('db.pool_size'),
     migrate_enabled=configuration.get('db.migrate'),
     check_reserved=['all'])
"""

from cls_examboard import ExamBoardModel

def get_options(db):

    rows = db.executesql("SELECT id, name FROM sow_exam_board;")

    data = [];

    for row in rows:
        model = ExamBoardModel(row[0], row[1])
        data.append(model)

    return data