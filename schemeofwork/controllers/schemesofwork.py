# -*- coding: utf-8 -*-
import db_schemeofwork  #= exec_environment('applications/schemeofwork/models/db_schemeofwork.py', request=request)
import db_examboard  #= exec_environment('applications/schemeofwork/models/db_examboard.py', request=request)
import db_keystage  #= exec_environment('applications/schemeofwork/models/db_keystage.py', request=request)

from datetime import datetime
from cls_schemeofwork import SchemeOfWorkModel

def index():
    """ index action """

    key_stage_id = int(request.vars.key_stage_id if request.vars.key_stage_id is not None else 0)

    content = {
        "main_heading":"Schemes of work",
        "sub_heading":"Our shared schemes of work by key stage",
        "strap_line":"",
        "background_img":"home-bg.jpg"
              }

    # get the schemes of work
    data = db_schemeofwork.get_all(db, key_stage_id=key_stage_id)

    key_stage_options = db_keystage.get_options(db)

    return dict(content = content, model = data, key_stage_options = key_stage_options)


def view():
    """ view action (NOT USED) """

    id_ = int(request.vars.id)
    model = db_schemeofwork.get_model(db, id_=id_)

    # check results and redirect if necessary

    if(model == None):
        ' TODO: SEND MESSAGE'
        redirect(URL('index'))

    content = {
        "main_heading":model.name,
        "sub_heading":model.exam_board_name + " " + model.key_stage_name
              }
    return dict(content = content, model = model)


@auth.requires_login()
def edit():
    """ edit action """

    id_ = int(request.vars.id if request.vars.id is not None else 0)
    model = db_schemeofwork.get_model(db, id_)
    if(model == None):
        redirect(URL('index', vars=dict(message="item deleted")))

    examboard_options = db_examboard.get_options(db)
    keystage_options = db_keystage.get_options(db)

    content = {
        "main_heading":model.name if model.name == "" else "New Scheme of work",
        "sub_heading":model.get_ui_sub_heading(),
        "strap_line": "" if model.name == "" else "Create a new scheme of work. Fill out the form below then click next to select or create learning episode."
              }
    return dict(content = content, model = model, examboard_options = examboard_options, keystage_options = keystage_options)


@auth.requires_login()
def save_item():
    """ save_item non-view action """

    # create instance of model from request.vars

    model = SchemeOfWorkModel(
        id_=request.vars.id,
        name=request.vars.name,
        description=request.vars.description,
        exam_board_id=request.vars.exam_board_id,
        key_stage_id=request.vars.key_stage_id,
        created=datetime.now(),
        created_by_id=auth.user_id)

    # validate the model and save if valid otherwise redirect to default invalid

    model.validate()
    if model.is_valid == True:
        model = db_schemeofwork.save(db, model)
    else:
        raise Exception("Validation errors:/n/n %s" % model.validation_errors) # TODO: redirect

    return redirect(URL('learningepisode', 'index', vars=dict(scheme_of_work_id = model.id)))


@auth.requires_login()
def delete_item():
    """ delete_item non-view action """

    id_ = int(request.vars.id)
    db_schemeofwork.delete(db, auth_user_id=auth.user.id, id_ = id_)
    return redirect(URL('index'))
