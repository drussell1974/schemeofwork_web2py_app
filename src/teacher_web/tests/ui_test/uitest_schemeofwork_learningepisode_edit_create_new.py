from selenium.webdriver.common.keys import Keys
from ui_testcase import UITestCase, WebBrowserContext

class test_schemeofwork_lesson_edit_create_new(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # setup
        self.test_path = '/schemesofwork/{}/lessons/new'.format(self.test_scheme_of_work_id)
        self.do_log_in(self.root_uri + self.test_path)


    def tearDown(self):
        #self.do_delete_scheme_of_work()
        pass


    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()

    def test_page__should_has_correct_element(self):

        ' ensure headings are correct '
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science','A-Level Computer Science','New', 'test@localhost')
    
        ' ensure secondary heading appears '
        elem = self.test_context.find_element_by_class_name("secondary-heading")
        self.assertEqual("A-Level Computer Science New", elem.text)

        ' topic dropdown '
        elems = self.test_context.find_elements_by_xpath(".//*[@id='ctl-topic_id']/option")
        self.assertEqual(7, len(elems))

        ' year group dropdown ' 
        elems = self.test_context.find_elements_by_xpath(".//*[@id='ctl-year_id']/option")
        self.assertEqual(3, len(elems))


    def test_page__should_stay_on_same_page_if_invalid(self):
        
        # arrange 
        elem = self.test_context.find_element_by_tag_name("form")
        
        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        ' ctl-key_stage_id - select EMPTY '
        elem = self.test_context.find_element_by_id("ctl-topic_id")
        all_options = elem.find_elements_by_tag_name('option')
        for opt in all_options:
            if opt.text == "- Select an option for topic -":
                 opt.click()

        elem.send_keys(Keys.TAB)


        ' submit the form '
        elem = self.test_context.find_element_by_id("saveButton")
        elem.send_keys(Keys.RETURN)

        # assert
        ' should still be on the same page '
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science','A-Level Computer Science','New')
        

    def test_page__should_redirect_to_index_if_valid(self):

        # arrange
        elem = self.test_context.find_element_by_tag_name("form")

        ' Ensure element is visible '
        self.test_context.execute_script("arguments[0].scrollIntoView();", elem)

        # act

        ' Create valid information '

        ' ctl-year_id - select Yr12 VALID '
        elem = self.test_context.find_element_by_id("ctl-year_id")
        all_options = elem.find_elements_by_tag_name('option')
        for opt in all_options:
            if opt.text == "Yr12":
                 opt.click()
        elem.send_keys(Keys.TAB)

        ' ctl-order_of_delivery_id '
        elem = self.test_context.find_element_by_id("ctl-order_of_delivery_id")
        elem.clear()
        elem.send_keys("1")

        ' ctl-title '
        elem = self.test_context.find_element_by_id("ctl-title")
        elem.clear()
        elem.send_keys("Consectetur adipiscing elit")

        ' ctl-summary '
        elem = self.test_context.find_element_by_id("ctl-summary")
        elem.clear()
        elem.send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam convallis volutpat.")

        ' ctl-key_words '
        #elem = self.test_context.find_element_by_id("ctl-key_words-tokenfield")
        #elem.clear()
        #elem.send_keys("Algorithm")
        #elem.send_keys(Keys.TAB)
        #elem.send_keys("Ipsum")
        #elem.send_keys(Keys.TAB)

        ' ctl-topic_id - select KS4 '
        elem = self.test_context.find_element_by_id("ctl-topic_id")
        all_options = elem.find_elements_by_tag_name('option')
        for opt in all_options:
            if opt.text == "Algorithms":
                 opt.click()
        elem.send_keys(Keys.TAB)

        ' div-pathway_objective_id  - select VALID '
        # expand accordion
        self.test_context.implicitly_wait(4) # wait for accordion to load from ajax call
        elem = self.test_context.find_element_by_id('ks3-heading-text')
        elem.click()

        elem = self.test_context.find_element_by_id('ctl-pathway_objective_id477')
        elem.click()
        elem.send_keys(Keys.TAB)
        
        ' submit the form '
        elem = self.test_context.find_element_by_id("saveButton")
        elem.send_keys(Keys.RETURN)

        # assert
        ' should still be on the same page '
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science','A-Level Computer Science','Edit: Consectetur adipiscing elit')