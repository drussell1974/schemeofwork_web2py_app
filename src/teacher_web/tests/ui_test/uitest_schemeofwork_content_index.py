from ui_testcase import UITestCase, WebBrowserContext

class uitest_schemeofwork_content_index(UITestCase):

    test_context = WebBrowserContext()

    def setUp(self):
        # set up
        self.do_log_in(f"/institute/{self.test_institute_id}/department/{self.test_department_id}/schemesofwork/{self.test_scheme_of_work_id}/curriculum-content")
        
        self.wait(s=2)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        # tear down
        cls.test_context.close()

    def test_page__should_have__title__title_heading__and__sub_heading(self):
        # test

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'A-Level Computer Science', 'Curriculum')
        self.assertFooterContextText("test@localhost Computer Science")


    def test_page__breadcrumb__navigate_to_schemesofwork_index(self):
        # arrange
        self.test_context.find_element_by_id('lnk-bc-schemes_of_work').click()


        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'Schemes of Work', 'Our shared schemes of work by key stage')


    def test_page__submenu__navigate_to_lesson_new(self):
        # arrange

        # act
        self.test_context.find_element_by_id('btn-new').click()
        self.wait()

        # assert
        self.assertWebPageTitleAndHeadings('Dave Russell - Teach Computer Science', 'A-Level Computer Science', 'Create new content for A-Level Computer Science')


    def test_page__should_have_sidenav(self):
        # arrange
        elem = self.test_context.find_element_by_id('sidebarNav')

        # act

        # assert
        self.assertIsNotNone(elem)


    def test_page__should_have_sidenav__showing_options_for_this_lesson(self):
        # arrange
        self.assertSidebarResponsiveMenu(section_no=1, expected_title="This scheme of work", expected_no_of_items=3)


    def test_page__should_have_sidenav__showing_options_for_this_scheme_of_work(self):
        # arrange
        self.assertSidebarResponsiveMenu(section_no=2, expected_title="Other schemes of work", expected_no_of_items=3)


    def test_page__should_have_sidenav__showing_administrator_links(self):
        # arrange
        self.assertSidebarResponsiveMenu(section_no=3, expected_title="Administrator", expected_no_of_items=1)

        
    def test_page__show_published_only(self):
        # arrange
        section = self.test_context.find_elements_by_class_name('post-preview')
        # assert
        result = len(section)
        self.assertEqual(9, result, "number of curriculum-content elements not as expected")


