from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.db import connection as db
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from shared.models.core.context import AuthCtx

# TODO: use view models
from shared.models.cls_learningobjective import LearningObjectiveModel
from shared.models.cls_ks123pathway import KS123PathwayModel
from shared.models.cls_lesson import LessonModel 

# view models
from .viewmodels import LessonGetModelViewModel, LessonGetAllViewModel

class LessonViewSet(APIView):
    ''' API endpoint for a lesson '''

    def get(self, request, institute_id, department_id, scheme_of_work_id, lesson_id, auth_ctx=None):

        # TODO: #367 get auth_ctx from min_permission_required decorator
        auth_ctx = AuthCtx(db, request, institute_id=institute_id, department_id=department_id, scheme_of_work_id=scheme_of_work_id)
        
        resource_type_id = request.GET.get("resource_type_id", 0)

        #253 check user id
        get_lesson_view = LessonGetModelViewModel(db=db, lesson_id=lesson_id, scheme_of_work_id=scheme_of_work_id, auth_user=auth_ctx, resource_type_id=resource_type_id)
        return JsonResponse({ "lesson": get_lesson_view.model })
    
    
class LessonListViewSet(APIView):
    ''' API endpoint for list of lessons '''

    def get (self, request, institute_id, department_id, scheme_of_work_id, auth_ctx=None):

        # TODO: #367 get auth_ctx from min_permission_required decorator
        auth_ctx = AuthCtx(db, request, institute_id=institute_id, department_id=department_id, scheme_of_work_id=scheme_of_work_id)

        #253 check user id
        get_lessons_view = LessonGetAllViewModel(db=db, scheme_of_work_id=scheme_of_work_id, auth_user=auth_ctx)
        return JsonResponse({"lessons": get_lessons_view.model})


class LessonPathwayObjectivesViewSet(APIView):
    ''' API endpoint for list of lessons pathway objectives'''

    def get(self, request, institute_id, department_id, scheme_of_work_id, lesson_id, key_stage_id, key_words = None, auth_ctx=None):

        # TODO: #367 get auth_ctx from min_permission_required decorator
        raise DeprecationWarning("verify usage")
    
        auth_ctx = AuthCtx(db, request, institute_id=institute_id, department_id=department_id, scheme_of_work_id=scheme_of_work_id)

        ''' get the pathway objectives '''
        pathwayobjectives = LearningObjectiveModel.get_all_pathway_objectives(db, key_stage_id = key_stage_id, key_words = key_words, auth_user = auth_ctx)
        should_be_checked = LessonModel.get_pathway_objective_ids(db, lesson_id, auth_ctx)

        return JsonResponse({
            "pathway-objectives": pathwayobjectives, 
            "should-be-checked": should_be_checked 
        })


class LessonPathwayKs123ViewSet(APIView):


    def get(self, request, institute_id, department_id, scheme_of_work_id, lesson_id, key_stage_id, topic_id, auth_ctx=None):

        # TODO: #367 get auth_ctx from min_permission_required decorator
        raise DeprecationWarning("Not referenced. Confirm usage")

        auth_ctx = AuthCtx(db, request, institute_id=institute_id, department_id=department_id, scheme_of_work_id=scheme_of_work_id)

        data = KS123PathwayModel.get_options(db, key_stage_id = key_stage_id, topic_id = topic_id, auth_user=auth_ctx)
        should_be_checked = KS123PathwayModel.get_linked_pathway_ks123(db, lesson_id, auth_user=auth_ctx)

        ks123pathway = []
        for item in data:
            for check in should_be_checked:
                if item.id == check[0]:
                    item.is_checked = True
                else:
                    item.is_checked = False

            ks123pathway.append(item)

        #return dict(view_model=view_model)
        return JsonResponse({"ks123-pathway": ks123pathway})
