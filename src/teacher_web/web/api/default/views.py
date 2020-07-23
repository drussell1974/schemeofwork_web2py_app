from rest_framework.views import APIView
from django.db import connection as db
from django.http import JsonResponse

# TODO: use view model
from shared.models import cls_topic

# view models
from .viewmodels import KeywordGetOptionsListViewModel, TopicGetOptionsListViewModel

class KeywordsListViewSet(APIView):
    ''' API endpoint for list of keywords '''
    def get (self, request):

        keywords = KeywordGetOptionsListViewModel(db)
        
        return JsonResponse({"keywords": keywords.data }, safe = False)


class RelatedTopicsListViewSet(APIView):
    ''' API endpoint for list of related topics '''
    def get (self, request, topic_id):

        topics = TopicGetOptionsListViewModel(db, topic_id)

        return JsonResponse({"related-topics": topics.data}, safe = False)
    