from ui_testcase import UITestCase, WebBrowserContext

class uitest_schemeofwork_default_index(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # set up
        self.test_context.get(self.root_uri)
        self.test_context.implicitly_wait(4)


    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()

    def test_page__should_have__title__title_heading__and__sub_heading(self):
        # test
        
        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Teach Computer Science', 'Computing Schemes of Work across all key stages')


    def test_page__navigate_to_all_schemesofwork_index(self):
        # setup
        self.test_context.find_element_by_id('btn-all-schemes-of-work').click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Schemes of Work', 'Our shared schemes of work by key stage')


    def test_page__show_only_published_latest_schemesofwork(self):
        # setup
        section = self.test_context.find_elements_by_class_name('post-preview-schemeofwork')

        # test
        result = len(section)

        # assert
        # ***** less 5 should be visible to test@localhost for testing purposes
        self.assertEqual(2, result, "number of elements not as expected")


    def test_page__show_published_and_owned_latest_schemesofwork(self):
        # setup
        self.do_log_in(redirect_to_uri_on_login="{}/schemesofwork".format(self.root_uri))

        section = self.test_context.find_elements_by_class_name('post-preview')

        # test
        result = len(section)

        # assert
        # ***** less 5 should be visible to test@localhost for testing purposes
        self.assertEqual(3, result, "number of elements not as expected")








