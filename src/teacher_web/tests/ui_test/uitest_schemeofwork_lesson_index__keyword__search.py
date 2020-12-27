from ui_testcase import UITestCase, WebBrowserContext

class uitest_schemeofwork_lesson_index__keyword__search(UITestCase):

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


    def test_page__should_show_all_when_keyword_search_is_empty(self):
        # arrange

        # array of expected items per pages

        expected_item_per_page = [10,10,6,0]

        # act

        # enter keyword and click search
        elem = self.test_context.find_element_by_id("ctl-keyword_search")
        elem.clear()
        elem_search = self.test_context.find_element_by_id("btn-search")
        elem_search.click()

        for expected_elems in expected_item_per_page: # cycle pages
            """ cycle each page """

            section = self.test_context.find_elements_by_class_name('post-preview')
            # assert
            result = len(section)
            self.assertEqual(expected_elems, result, "number of elements not as expected")

            elem_next = self.test_context.find_element_by_id("btn-pager--next")
            elem_next.click()
            self.wait()


    def test_page__should__show_only_show_lessons_with_keyword_in_title__no_results(self):
        # arrange

        # array of expected items per pages

        expected_item_per_page = [0]

        # act

        # enter keyword and click search
        elem = self.test_context.find_element_by_id("ctl-keyword_search")
        elem.send_keys("xxxx")
        elem_search = self.test_context.find_element_by_id("btn-search")
        elem_search.click()

        self.wait()

        for expected_elems in expected_item_per_page: # cycle pages
            """ cycle each page """

            section = self.test_context.find_elements_by_class_name('post-preview')
            # assert
            result = len(section)
            self.assertEqual(expected_elems, result, "number of elements not as expected")

            elem_next = self.test_context.find_element_by_id("btn-pager--next")
            elem_next.click()
            self.wait()


    def test_page__should__show_only_show_lessons_with_keyword_in_title_and_keywords_find_results(self):
        # arrange

        # array of expected items per pages

        expected_item_per_page = [3]

        # act

        # enter keyword and click search
        elem = self.test_context.find_element_by_id("ctl-keyword_search")
        elem.send_keys("CpU")
        elem_search = self.test_context.find_element_by_id("btn-search")
        elem_search.click()

        self.wait()

        for expected_elems in expected_item_per_page: # cycle pages
            """ cycle each page """

            section = self.test_context.find_elements_by_class_name('post-preview')
            # assert
            result = len(section)
            self.assertEqual(expected_elems, result, "number of elements not as expected")

            elem_next = self.test_context.find_element_by_id("btn-pager--next")
            elem_next.click()
            self.wait()