from django.contrib.auth.decorators import permission_required
from django.db import connection as db
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from shared.view_model import ViewModel
from shared.models import cls_lesson, cls_schemeofwork, cls_ks123pathway, cls_learningobjective, cls_keyword, cls_topic, cls_year
from shared.models.core import validation_helper
from datetime import datetime

# Create your views here.        
def index(request, scheme_of_work_id):
    """ Get lessons for scheme of work """

    scheme_of_work_name = cls_schemeofwork.get_schemeofwork_name_only(db, scheme_of_work_id)

    lessons = cls_lesson.get_all(db, scheme_of_work_id, auth_user=request.user.id)
    schemeofwork_options = cls_schemeofwork.get_options(db, auth_user=request.user.id)
    
    
    data = {
        "scheme_of_work_id":int(scheme_of_work_id),
        "schemeofwork_options": schemeofwork_options,
        "lessons": lessons,
        "topic_name": "",
    }

    view_model = ViewModel("", scheme_of_work_name, "Lessons", data=data)
    
    return render(request, "lessons/index.html", view_model.content)

@permission_required('cssow.add_lessonmodel', login_url='/accounts/login/')
def new(request, scheme_of_work_id):
    ''' Create a new lesson '''
    
    scheme_of_work = cls_schemeofwork.get_model(db, scheme_of_work_id, request.user.id)
    
    lesson = cls_lesson.get_model(db, 0, request.user.id)
    lesson["key_stage_id"] = scheme_of_work.key_stage_id
    lesson["scheme_of_work_id"] = scheme_of_work.id
    year_options = cls_year.get_options(db, scheme_of_work.key_stage_id)
    topic_options = cls_topic.get_options(db, lvl=1)
    key_words = cls_keyword.get_options(db)

    print("edit... key_words:", key_words)
    print("edit... lesson['key_words']:", lesson["key_words"])

    data = {
        "scheme_of_work_id": int(scheme_of_work_id),
        "lesson_id": int(lesson["id"]),
        "key_stage_id": scheme_of_work.key_stage_id,
        "topic_options": topic_options,
        "selected_topic_id": 0, 
        "year_options": year_options,
        "selected_year_id": 0,
        "lesson": lesson,
        "key_words": key_words,
    }
    
    view_model = ViewModel("", scheme_of_work.name, "New", data=data)
    
    return render(request, "lessons/edit.html", view_model.content)


@permission_required('cssow.change_lessonmodel', login_url='/accounts/login/')
def edit(request, scheme_of_work_id, lesson_id):
    ''' Edit the lesson '''

    lesson = cls_lesson.get_model(db, lesson_id, request.user.id)

    scheme_of_work = cls_schemeofwork.get_model(db, scheme_of_work_id, request.user.id)
    year_options = cls_year.get_options(db, lesson["key_stage_id"])
    topic_options = cls_topic.get_options(db, lvl=1)
    key_words = cls_keyword.get_options(db)
    ks123_pathways = cls_ks123pathway.get_options(db, lesson["year_id"], lesson["topic_id"])
    
    data = {
        "scheme_of_work_id": scheme_of_work_id,
        "lesson_id": lesson["id"],
        "key_stage_id": scheme_of_work.key_stage_id,
        "topic_options": topic_options,
        "selected_topic_id": lesson["topic_id"], 
        "year_options": year_options,
        "selected_year_id": lesson["year_id"],
        "lesson": lesson,
        "key_words": key_words,
        "ks123_pathways": ks123_pathways,
        "show_ks123_pathway_selection": lesson["key_stage_id"] in (1,2,3)
    }
    
    view_model = ViewModel("Dave Russell - Computer Science", scheme_of_work.name, "Edit: {}".format(lesson["title"]), data=data)
    
    return render(request, "lessons/edit.html", view_model.content)

    
@permission_required('cssow.add_lessonmodel', login_url='/accounts/login/')
def copy(request, scheme_of_work_id, lesson_id):
    ''' Copy the lesson '''
    lesson = cls_lesson.get_model(db, lesson_id, request.user.id)
    lesson["id"] = 0 # reset id

    scheme_of_work = cls_schemeofwork.get_model(db, scheme_of_work_id, request.user.id)
    year_options = cls_year.get_options(db, lesson["key_stage_id"])
    topic_options = cls_topic.get_options(db, lvl=1)
    key_words = cls_keyword.get_options(db)
    
    data = {
        "scheme_of_work_id": scheme_of_work_id,
        "lesson_id": 0,
        "key_stage_id": scheme_of_work.key_stage_id,
        "topic_options": topic_options,
        "selected_topic_id": lesson["topic_id"], 
        "year_options": year_options,
        "selected_year_id": lesson["year_id"],
        "lesson": lesson,
        "key_words": key_words,
    }
    
    view_model = ViewModel("Dave Russell - Computer Science", scheme_of_work.name, "Copy: {}".format(lesson["title"]), data=data)
    
    return render(request, "lessons/edit.html", view_model.content)


@permission_required('cssow.publish_lessonmodel', login_url='/accounts/login/')
def publish(request, scheme_of_work_id, lesson_id):
    ''' Publish the lesson '''
    
    view_model = ViewModel("", "A-Level Computer Science", "Publish")
    # TODO: redirect
    return render(request, "lessons/edit.html", view_model.content)


@permission_required('cssow.delete_lessonmodel', login_url='/accounts/login/')
def delete(request, scheme_of_work_id, lesson_id):
    """ delete item and redirect back to referer """
    
    redirect_to_url = request.META.get('HTTP_REFERER')

    cls_lesson.delete(db, request.user.id, lesson_id)

    return HttpResponseRedirect(redirect_to_url)
    
def lessonplan(request, scheme_of_work_id, lesson_id):
    ''' Display the lesson plan '''

    view_model = ViewModel("", "", "lesson plan")
    
    return render(request, "lessons/lessonplan.html", view_model.content)

    
def whiteboard(request, scheme_of_work_id, lesson_id):
    ''' Display the lesson plan on the whiteboard '''
    model =  cls_lesson.get_model(db, lesson_id, request.user.id)
    data = {
        "key_words":model["key_words"],
        "learning_objectives":model["learning_objectives"],
        "resources": model["resources"],
    }

    view_model = ViewModel("", model["title"], model["topic_name"], data=data)
    
    return render(request, "lessons/whiteboard_view.html", view_model.content)


@permission_required('cssow.publish_lessonmodel', login_url='/accounts/login/')
def save(request, scheme_of_work_id, lesson_id):
    """ save_item non-view action """

    published = int(request.POST["published"] if request.POST["published"] is not None else 1)
    
    # TODO: replace request.POST[key] with request.POST.get(key, default)
    model = cls_lesson.LessonModel(
        id_ = request.POST["id"],
        orig_id = int(request.POST["orig_id"]),
        title = request.POST["title"],
        order_of_delivery_id = request.POST["order_of_delivery_id"],
        scheme_of_work_id = request.POST["scheme_of_work_id"],
        topic_id = request.POST["topic_id"],
        related_topic_ids = request.POST["related_topic_ids"],
        key_stage_id= request.POST.get("key_stage_id", 0),
        year_id = request.POST.get("year_id", 0),
        summary = request.POST["summary"],
        created = datetime.now(),
        created_by_id = request.user.id
    )

    model.key_words = request.POST.getlist("key_words")

    model.pathway_ks123_ids = request.POST.getlist("pathway_ks123_ids")

    # reset id if a copy
    if int(request.POST["orig_id"]) > 0:
        model.id = int(request.POST["orig_id"])

    model.validate()

    if model.is_valid == True:
        ' save the lesson '
        model = cls_lesson.save(db, model, request.user.id, published)
        
        if request.POST["next"] != "None"  and request.POST["next"] != "":
            redirect_to_url = request.POST["next"]
        else:
            redirect_to_url = reverse('lesson.edit', args=(scheme_of_work_id, model.id))
    else:
        """ redirect back to page and show message """
        request.session.alert_message = validation_helper.html_validation_message(model.validation_errors) #model.validation_errors
        redirect_to_url = reverse('lesson.edit', args=(scheme_of_work_id,lesson_id))

    return HttpResponseRedirect(redirect_to_url)


def initialise_keywords(request, scheme_of_work_id):
    lessons = cls_lesson.get_all(db, scheme_of_work_id, auth_user=request.user.id)

    for lesson in lessons:
       cls_lesson._upsert_key_words(db, lesson)

    scheme_of_work_name = cls_schemeofwork.get_schemeofwork_name_only(db, scheme_of_work_id)
    schemeofwork_options = cls_schemeofwork.get_options(db, auth_user=request.user.id)
    
    data = {
        "scheme_of_work_id":int(scheme_of_work_id),
        "schemeofwork_options": schemeofwork_options,
        "lessons": lessons,
        "topic_name": "",
    }

    view_model = ViewModel("", scheme_of_work_name, "Lessons", data=data)
    
    return render(request, "lessons/index.html", view_model.content)


@permission_required('cssow.delete_lessonmodel', login_url='/accounts/login/')
def delete_unpublished(request, scheme_of_work_id):
    """ delete item and redirect back to referer """

    redirect_to_url = request.META.get('HTTP_REFERER')

    cls_lesson.delete_unpublished(db, scheme_of_work_id, request.user.id)

    return HttpResponseRedirect(redirect_to_url)