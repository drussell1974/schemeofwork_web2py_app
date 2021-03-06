from unittest import skip
from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext


class uitest_schemeofwork_resources_edit_cancel(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        #231: TODO: open existing resource
        self.do_log_in(self.root_uri + f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/resources/{self.test_reference}/edit")


    def tearDown(self):
        #self.do_delete_scheme_of_work()
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    """ Test edit """
    
    def test_page__should_stay_on_same_page_if_stay(self):
        # setup
        elem = self.test_context.find_element_by_tag_name("form")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)
        self.wait(s=2)
        ' Open Modal '

        elem = self.test_context.find_element_by_id("cancelButton")
        elem.click()

        ' click no '        
        
        elem = self.test_context.find_element_by_id("cancelModalStayButton")
        elem.click()
        
        self.wait(s=2)

        # assert
        ' should still be on the same page '
        #231: assert we're still on the same page
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Types of CPU architecture', 'Edit: OCR AS and A Level Computer Science')


    def test_page__should_redirect_to_index_if_continue(self):
        # setup
        elem = self.test_context.find_element_by_tag_name("form")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        # TODO: improve performance
        self.wait()

        ' Open Modal '

        elem = self.test_context.find_element_by_id("cancelButton")
        elem.click()

        ' click no (finding button appears to cancel dialog) '        
        
        elem = self.test_context.find_element_by_id("cancelModalContinueButton")
        elem.click()
        # TODO: improve performance
        self.wait()

        # assert
        ' should be redirected '
        self.assertWebPageTitleAndHeadings('', 'Log in', 'Register to create schemes of work and lessons')
