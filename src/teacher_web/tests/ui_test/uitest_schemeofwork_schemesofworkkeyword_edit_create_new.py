from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext
import unittest

class uitest_schemeofwork_schemesofworkkeyword_edit_create_new(UITestCase):

    test_context = WebBrowserContext()
    
    def setUp(self):
        self.current_learning_objective_id = 0

        # setup
        self.do_log_in(self.root_uri + f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{}/keywords/new".format(self.test_scheme_of_work_id, self.test_lesson_id))
        self.wait(2)


    def tearDown(self):
        
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    """ Test edit """
    
    def test_page__should_stay_on_same_page_if_invalid(self):
        # setup
        elem = self.test_context.find_element_by_tag_name("form")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        ' submit the form '
        elem = self.test_context.find_element_by_id("saveButton")
        elem.send_keys(Keys.RETURN)

        # assert
        ' should still be on the same page '
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'A-Level Computer Science', 'Create new keyword for A-Level Computer Science')

    
    def test_page__should_stay_on_same_page_if_duplicate(self):
        # setup
        elem = self.test_context.find_element_by_tag_name("form")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        ' term Enter Valid '
        elem = self.test_context.find_element_by_id("ctl-term")
        elem.clear()
        elem.send_keys(self.TEST_KEYWORD_TERM)

        ' definition Enter Valid '
        elem = self.test_context.find_element_by_id("ctl-definition")
        elem.clear()
        # first paragraph
        elem.send_keys("Lorem xipsum dolor sit amet, consectetur adipiscing elit. Quisque eros est, feugiat id diam eu, iaculis vulputate dui.")
        # second paragraph
        elem.send_keys(Keys.ENTER)
        elem.send_keys(Keys.ENTER)
        elem.send_keys("Quisque diame lorem, aliquam non tortor vel, tristique vestibulum leo. Integer mattis eros in diam faucibus interdum. Sed nec tortor.")

        ' submit the form '
        elem = self.test_context.find_element_by_id("saveDraftButton")
        elem.send_keys(Keys.RETURN)

        # assert
        ' should still be on the same page '
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'A-Level Computer Science', 'Create new keyword for A-Level Computer Science')
        

    def test_page__should_redirect_to_index_if_valid(self):
        # setup
        elem = self.test_context.find_element_by_tag_name("form")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)


        ' term Enter Valid '

        elem = self.test_context.find_element_by_id("ctl-term")
        elem.clear()
        elem.send_keys("Lorem ipsum do")
        
        ' definition '

        elem = self.test_context.find_element_by_id("ctl-definition")
        elem.send_keys("test_page__should_redirect_to_index_if_valid")

        ' submit the form '
        elem = self.test_context.find_element_by_id("saveDraftButton")
        elem.send_keys(Keys.RETURN)
        self.wait(s=2)
        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'A-Level Computer Science', 'Computing curriculum for A-Level')

        #delete
        elem = self.test_context.find_element_by_id("btn-delete-unpublished")
        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)
        self.wait()

        elem.click()
