from ui_testcase import UITestCase, WebBrowserContext
from selenium.webdriver.common.keys import Keys

class uitest_schemeofwork_lessonkeyword_select__search_term(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # set up
        self.do_log_in(f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/lessons/{self.test_lesson_id}/keywords/select", wait=4)


    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()


    def test_page__should_all_by_default(self):
        # test
        elem = self.test_context.find_elements_by_xpath("//*[contains(@class, 'card-keyword')]")
        
        # assert
        self.assertEqual(155, len(elem))


    def test_page__should_show_none(self):
        
        # test
        elem = self.test_context.find_element_by_id("ctl-keyword_search")
        elem.send_keys("abcd")
        
        elem = self.test_context.find_elements_by_xpath("//*[contains(@style, 'block')]")
        
        # assert
        self.assertEqual(0, len(elem))


    def test_page__should_upper_and_lower_case_matches(self):
        
        # test
        elem = self.test_context.find_element_by_id("ctl-keyword_search")
        elem.send_keys("Ra")

        elem = self.test_context.find_elements_by_xpath("//*[contains(@style, 'block')]")
        
        # assert
        self.assertEqual(24, len(elem))


    def test_page__should_single_item_match(self):
        
        # test
        elem = self.test_context.find_element_by_id("ctl-keyword_search")
        elem.send_keys("Random Access Memory (RAM)")
        
        elem = self.test_context.find_elements_by_xpath("//*[contains(@style, 'block')]")
        
        # assert
        self.assertEqual(1, len(elem))


    def test_page__should_retain_hidden_items_on_save(self):
        
        # test
        elem = self.find_element_by_id__with_explicit_wait("ctl-keyword_search", wait=2)
        elem.send_keys("Random Access Memory (RAM)")
                
        elem = self.test_context.find_elements_by_xpath("//*[contains(@style, 'block')]")
        self.assertEqual(1, len(elem), "page must show only one element before saving")

        # act
        
        ' submit the form '
        elem = self.find_element_by_id__with_explicit_wait("saveButton", wait=2)
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)
        elem.send_keys(Keys.RETURN)
        self.wait(s=2)
        # assert
        ' should still be on the same page '
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Types of CPU architecture', 'Von Neumann architecture and Harvard architecture, and CISC and RISC')

        elem = self.test_context.find_elements_by_class_name("card-keyword")
        self.assertEqual(3, len(elem))