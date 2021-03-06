from unittest import skip
from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext


@skip("DO NOT RUN, to eliminate prevent deletion of test data")
class uitest_schemeofwork_schemesofworkkeyword_edit_delete(UITestCase):

    test_context = WebBrowserContext()
    
    def setUp(self):
        
        # setup

        self.do_log_in(self.root_uri + f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/keywords/new", wait=4)

        # create content
        
        elem = self.test_context.find_element_by_tag_name("form")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        ' name '
        elem = self.test_context.find_element_by_id("ctl-term")
        elem.clear()
        elem.send_keys("Lorem ipsum DEL 11")

        elem = self.test_context.find_element_by_id("ctl-definition")
        elem.send_keys("Can be deleted")

        ' submit the form '
        elem = self.test_context.find_element_by_id("saveDraftButton")
        elem.send_keys(Keys.RETURN)
        self.wait(s=2)
        
        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'A-Level Computer Science', 'Computing curriculum for A-Level', wait=4)


    def tearDown(self):
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    """ Test delete """
    
    def test_page__should_redirect_to_index_after_deletion(self):

        #delete

        ' Open edit '
        self.delete_unpublished_item(".unpublished a.edit .fa-edit")
        
        self.wait(s=2)


        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'A-Level Computer Science', 'Computing curriculum for A-Level')
        
        #231: items after should be less than before
        
        items_after = self.test_context.find_elements_by_class_name("card-keyword")
        self.assertEqual(155, len(items_after))