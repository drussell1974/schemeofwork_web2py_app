from ui_testcase import UITestCase, WebBrowserContext

class test_schemeofwork_learningepsiode_index(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # set up
        self.test_path = "/schemesofwork/{}/lessons".format(self.test_scheme_of_work_id)

        self.test_context.get(self.root_uri + self.test_path)
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
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'A-Level Computer Science', 'Lessons')


    def test_page__breadcrumb__navigate_to_schemesofwork_index(self):
        # setup
        self.test_context.find_element_by_id('lnk-bc-schemes_of_work').click()


        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Schemes of Work', 'Our shared schemes of work by key stage')


    def test_page__submenu__navigate_to_learningepisode_new(self):
        # setup
        self.do_log_in(self.test_path)

        # test
        self.test_context.find_element_by_id('btn-new').click()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'A-Level Computer Science', 'Create')


