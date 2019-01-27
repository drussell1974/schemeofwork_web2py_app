# -*- coding: utf-8 -*-
from datetime import datetime
from cls_reference import ReferenceModel
from db_helper import to_db_null

def get_options(db, scheme_of_work_id, auth_user):

    str_select = "SELECT ref.id as id, ref.title as title, ref.publisher as publisher, ref.year_published as year_published, ref.authors as authors, ref.uri as uri FROM sow_reference as ref WHERE ref.scheme_of_work_id = {scheme_of_work_id} AND (ref.published = 1 OR ref.created_by = {auth_user});"
    str_select = str_select.format(auth_user=to_db_null(auth_user), scheme_of_work_id=scheme_of_work_id)

    rows = db.executesql(str_select)

    data = [];

    for row in rows:
        model = ReferenceModel(id_=row[0], title=row[1], publisher=row[2], year_published=row[3], authors=row[4], uri=row[5], scheme_of_work_id = scheme_of_work_id)
        data.append(model)

    return data


def get_model(db, id_, scheme_of_work_id, auth_user):
    now = datetime.now()
    model = ReferenceModel(id_=0, title="", publisher="", year_published=now.year, authors="", uri="", scheme_of_work_id = scheme_of_work_id)

    str_select = "SELECT" \
                 " ref.id as id," \
                 " ref.title as title," \
                 " ref.publisher as publisher," \
                 " ref.year_published as year_published," \
                 " ref.authors as authors," \
                 " ref.uri as uri " \
                 "FROM sow_reference as ref" \
                 " WHERE ref.id = {id_} AND (ref.published = 1 OR ref.created_by = {auth_user});"
    str_select = str_select.format(id_=id_, auth_user=to_db_null(auth_user))

    rows = db.executesql(str_select)

    for row in rows:
        model = ReferenceModel(id_=row[0], title=row[1], publisher=row[2], year_published=row[3], authors=row[4], uri=row[5], scheme_of_work_id=scheme_of_work_id)

    return model


def save(db, model):
    """
    Upsert the reference
    :param db: database context
    :param model: the ReferenceModel
    :return: the updated ReferenceModel
    """
    if model.is_new() == True:
        model.id = _insert(db, model)
    else:
        _update(db, model)

    return model


def delete(db, id_):
    """

    :param db: the database context
    :param id_: the id of the record to delete
    :return: nothing
    """
    _delete(db, id_);

"""
Private CRUD functions 
"""

def _update(db, model):
    """ updates the sow_learning_episode and sow_learning_episode__has__topics """

    # 1. Update the learning episode

    str_update = "UPDATE sow_reference SET title = '{title}', authors = '{authors}', publisher = '{publisher}', year_published = {year_published}, uri = '{uri}', scheme_of_work_id = {scheme_of_work_id} WHERE id = {id};"
    str_update = str_update.format(
        id=model.id,
        title=model.title,
        authors=to_db_null(model.authors),
        publisher=model.publisher,
        year_published = model.year_published,
        uri=to_db_null(model.uri),
        scheme_of_work_id = model.scheme_of_work_id)

    db.executesql(str_update)

    # 2. upsert related topics
    #if scheme_of_work_id > 0:
    #    _upsert_sow_scheme_of_work__has__reference(db, model, scheme_of_work_id)

    return True


def _insert(db, model):
    """ inserts the sow_reference and sow_scheme_of_work__has__reference """

    ## 1. Insert the reference

    str_insert = "INSERT INTO sow_reference (title, authors, publisher, year_published, uri, scheme_of_work_id, created, created_by) VALUES ('{title}', '{authors}', '{publisher}', {year_published}, '{uri}', {scheme_of_work_id}, '{created}', {created_by});"
    str_insert = str_insert.format(
        title=model.title,
        authors=to_db_null(model.authors),
        publisher=model.publisher,
        year_published = model.year_published,
        uri=to_db_null(model.uri),
        scheme_of_work_id = model.scheme_of_work_id,
        created=model.created,
        created_by=model.created_by_id)

    db.executesql(str_insert)

    rows = db.executesql("SELECT LAST_INSERT_ID();")

    for row in rows:
        model.id = int(row[0])

    ## 2. insert related topics
    #if scheme_of_work_id > 0:
    #    _upsert_sow_scheme_of_work__has__reference(db, model, scheme_of_work_id)

    return model.id

"""
def _upsert_sow_scheme_of_work__has__reference(db, model, scheme_of_work_id):
    ""deletes and reinserts sow_scheme_of_work__has__reference ""

    # delete existing
    str_delete = "DELETE FROM sow_scheme_of_work__has__reference WHERE scheme_of_work_id = {scheme_of_work_id};".format(scheme_of_work_id=scheme_of_work_id)

    db.executesql(str_delete)

    if len(model.related_topic_ids) > 0:
        # reinsert
        str_insert = "INSERT INTO sow_scheme_of_work__has__reference (scheme_of_work_id, reference_id) VALUES"
        str_insert = str_insert + "({scheme_of_work_id}, {reference_id});".format(scheme_of_work_id=scheme_of_work_id, reference_id=model.id)

        db.executesql(str_insert)
"""

def _delete(db, id_):
    str_delete = "DELETE FROM sow_reference WHERE id = {id_};"
    str_delete = str_delete.format(id_=id_)

    rval = db.executesql(str_delete)

    return rval