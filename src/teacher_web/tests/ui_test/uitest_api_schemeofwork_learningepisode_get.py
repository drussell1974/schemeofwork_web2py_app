from django.test import tag
from ui_testcase import UITestCase, WebBrowserContext
from django.urls import reverse
#from lessons.views import get


class test_schemeofwork_learningepsiode_get_all(UITestCase):

    test_context = WebBrowserContext()
    
    def setUp(self):
        # set up
        self.test_context.get(self.root_uri + "/api/schemesofwork/{}/lessons".format(self.test_scheme_of_work_id))
        self.test_context.implicitly_wait(4)

        #arrange
        elem = self.test_context.find_element_by_tag_name('pre')
        content = elem.text
        import json
        self.payload = json.loads(content)

        self.last_item_index = len(self.payload["lessons"]) - 1


    def tearDown(self):
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


#    def test__should_resolve_url(self):
#        found = reverse("lessons")
#        self.assertEqual(found, "/api/schemeofwork/11/lessons")

    def test__should_return_a_payload(self):
        # assert
        self.assertIsNotNone(self.payload)


    def test__should_have_multiple_records(self):
        # assert
        self.assertEqual(27, len(self.payload["lessons"]))

    
    def test__first__should_have_title(self):
        # assert
        self.assertEqual('The CPU', self.payload["lessons"][0]["title"])

        
    def test__first__should_have_summary(self):
        # assert
        self.assertEqual('CPU components: ALU, Control Unit, Registers and Buses', self.payload["lessons"][0]["summary"])


    def test__first__should_have_lesson_objectives(self):
        # assert
        self.assertEqual(9, len(self.payload["lessons"][0]["learning_objectives"]))


    def test__first__should_have_zero_resources(self):
        # assert
        self.assertEqual(0, self.payload["lessons"][0]["number_of_resource"])
        
        
    def test__last__should_have_title(self):
        # assert
        self.assertEqual('Strategies for Problem Solving', self.payload["lessons"][self.last_item_index]["title"])

        
    def test__last__should_have_summary(self):
        # assert
        self.assertEqual('Strategies used for finding the best solution or approximate solutions', self.payload["lessons"][self.last_item_index]["summary"])


    def test__last__should_have_lesson_objectives(self):
        # assert
        self.assertEqual(10, len(self.payload["lessons"][self.last_item_index]["learning_objectives"]))


    def test__last__should_have_resources(self):
        # assert
        self.assertEqual(2, self.payload["lessons"][self.last_item_index]["number_of_resource"])