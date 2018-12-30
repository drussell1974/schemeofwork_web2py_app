from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase

class test_schemeofwork_learningobjective_edit_existing(UITestCase):

    test_context = webdriver.Chrome()

    def setUp(self):
        # setup
        self.try_log_in("http://127.0.0.1:8000/schemeofwork/learningobjective/edit?id=460&learning_episode_id={}&scheme_of_work_id={}".format(self.test_learning_episode_id, self.test_scheme_of_work_id))


    def tearDown(self):
        #self.do_delete_scheme_of_work()
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

        ' name (cause validation error by entering blank '
        elem = self.test_context.find_element_by_id("ctl-description")
        elem.clear()
        elem.send_keys("")

        ' ctl-parent_id - select VALID '

        elem = self.test_context.find_element_by_id("ctl-parent_id")
        all_options = elem.find_elements_by_tag_name('option')
        for opt in all_options:
            if opt.text == "Define the term sequence":
                 opt.click()
        elem.send_keys(Keys.TAB)

        ' ctl-solo_taxonomy_id - SELECT VALID '

        elem = self.test_context.find_element_by_id("ctl-solo_taxonomy_id")
        all_options = elem.find_elements_by_tag_name('option')
        for opt in all_options:
            if opt.text == "Multistructural: Describe, List":
                 opt.click()
        elem.send_keys(Keys.TAB)

        ' ctl-topic_id - SELECT VALID '

        elem = self.test_context.find_element_by_id("ctl-topic_id")
        all_options = elem.find_elements_by_tag_name('option')
        for opt in all_options:
            if opt.text == "Algorithms":
                 opt.click()
        elem.send_keys(Keys.TAB)

        ' ctl-content_id SKIP '

        elem = self.test_context.find_element_by_id("ctl-content_id")
        elem.send_keys(Keys.TAB)

        ' ctl-exam_board_id SKIP '

        elem = self.test_context.find_element_by_id("ctl-exam_board_id")
        elem.send_keys(Keys.TAB)

        ' Submit '

        elem = self.test_context.find_element_by_id("saveButton")

        ' submit the form '
        elem.send_keys(Keys.RETURN)

        # assert
        ' should still be on the same page '
        self.assertWebPageTitleAndHeadings('schemeofwork', 'Learning objective', 'for A-Level Computer Science - Week 1 - Algorithms')



    def test_page__should_stay_on_same_page_if_valid(self):
        # setup
        elem = self.test_context.find_element_by_tag_name("form")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        ' name (cause validation error by entering blank '
        elem = self.test_context.find_element_by_id("ctl-description")
        elem.send_keys("test_page__should_stay_on_same_page_if_valid")

        ' ctl-parent_id - select VALID '

        elem = self.test_context.find_element_by_id("ctl-parent_id")
        all_options = elem.find_elements_by_tag_name('option')
        for opt in all_options:
            if opt.text == "Define the term sequence":
                 opt.click()
        elem.send_keys(Keys.TAB)

        ' ctl-solo_taxonomy_id - SELECT VALID '

        elem = self.test_context.find_element_by_id("ctl-solo_taxonomy_id")
        all_options = elem.find_elements_by_tag_name('option')
        for opt in all_options:
            if opt.text == "Multistructural: Describe, List":
                 opt.click()
        elem.send_keys(Keys.TAB)

        ' ctl-topic_id - SELECT VALID '

        elem = self.test_context.find_element_by_id("ctl-topic_id")
        all_options = elem.find_elements_by_tag_name('option')
        for opt in all_options:
            if opt.text == "Algorithms":
                 opt.click()
        elem.send_keys(Keys.TAB)

        ' ctl-content_id SKIP '

        elem = self.test_context.find_element_by_id("ctl-content_id")
        elem.send_keys(Keys.TAB)

        ' ctl-exam_board_id SKIP '

        elem = self.test_context.find_element_by_id("ctl-exam_board_id")
        elem.send_keys(Keys.TAB)

        ' Submit '
        elem = self.test_context.find_element_by_id("saveButton")

        ' submit the form '
        elem.send_keys(Keys.RETURN)

        # assert
        ' should still be on the same page '
        self.assertWebPageTitleAndHeadings('schemeofwork', 'Learning objectives', 'for A-Level Computer Science - Week 1 - Algorithms')