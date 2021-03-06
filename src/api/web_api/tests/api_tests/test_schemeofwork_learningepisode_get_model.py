from django.test import tag
from ui_testcase import UITestCase, WebBrowserContext
from django.urls import reverse
#from lessons.views import get

@tag("lesson")
class test_schemeofwork_learningepsiode_get(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # set up
        self.do_get(f"http://localhost:8000/api/schemeofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}", wait=2)
        
        #arrange
        elem = self.test_context.find_element_by_tag_name('pre')
        content = elem.text
        import json
        self.payload = json.loads(content)


    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


#    def test__should_resolve_url(self):
#        found = reverse("lessons")
#        self.assertEqual(found, "/api/schemeofwork/11/lessons")


    @tag("lesson should return a payload")
    def test__should_return_a_payload(self):
        # assert
        self.assertIsNotNone(self.payload)
        
    
    @tag("lesson should have title")
    def test__should_have_title(self):
        # assert
        self.assertEqual('The CPU', self.payload["lesson"]["title"])

        
    @tag("lesson should have summary")
    def test__should_have_summary(self):
        # assert
        self.assertEqual('CPU components: ALU, Control Unit, Registers and Buses', self.payload["lesson"]["summary"])

    @tag("lesson should have learning objectives")
    def test__should_have_learning_objectives(self):
        # assert
        self.assertEqual(9, len(self.payload["lesson"]["learning_objectives"]))


    @tag("lesson should have resources")
    def test__should_have_resources(self):
        # assert
        self.assertEqual(14, len(self.payload["lesson"]["resources"]))
        