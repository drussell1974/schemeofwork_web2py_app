from django.urls import resolve, reverse
from django.test import TestCase
from api.default.views import KeywordsListViewSet, RelatedTopicsListViewSet

# Create your tests here.
class test_api_route_default_topics(TestCase):

    def test_url_resolves_to_RelatedTopicsListViewSet_view(self):
        url = resolve('/api/institute/127671276711/department/67/related-topics/5')
        self.assertEqual("api.default.related-topics", url.url_name)
        self.assertEqual(type(url.func), type(RelatedTopicsListViewSet.as_view()))

        
    def test_url_resolves_to_RelatedTopicsListViewSet_view__reverse(self):
        url = reverse('api.default.related-topics', args=[127671276711, 67, 5])
        self.assertEqual("/api/institute/127671276711/department/67/related-topics/5", url)