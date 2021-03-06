from django.urls import resolve, reverse
from django.test import TestCase
from app.eventlogs.views import index, delete

# Create your tests here.
class test_app_route_eventlog_page(TestCase):

    def test_eventlog_index_url_resolves_to_index(self):
        url = resolve('/institute/12711761271176/department/1271176/schemesofwork/99/event-log/')
        self.assertEqual("eventlog.index", url.url_name)
        self.assertEquals(url.func, index)

    
    def test_eventlog_index_resolves_to_index__reverse(self):
        url = reverse("eventlog.index", args=[12711761271176, 1271176, 99])
        self.assertEqual("/institute/12711761271176/department/1271176/schemesofwork/99/event-log/", url)


    def test_eventlog_delete_url_resolves_to_delete(self):
        url = resolve('/institute/12711761271176/department/1271176/schemesofwork/99/event-log/delete')
        self.assertEqual("eventlog.delete", url.url_name)
        self.assertEquals(url.func, delete)

    
    def test_eventlog_delete_resolves_to_delete__reverse(self):
        url = reverse("eventlog.delete", args=[12711761271176, 1271176, 98])
        self.assertEqual("/institute/12711761271176/department/1271176/schemesofwork/98/event-log/delete", url)



        