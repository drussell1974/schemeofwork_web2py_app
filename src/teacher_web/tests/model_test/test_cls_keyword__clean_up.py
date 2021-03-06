from unittest import TestCase
from shared.models.cls_keyword import KeywordModel


class test_cls_reference__clean_up(TestCase):

    def setUp(self):
        self.test = KeywordModel(1, "", "")


    def test_term__trim_whitespace(self):

        self.test.term = " x "

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x", self.test.term)


    def test_definition__trim_whitespace(self):

        self.test.definition = " x "

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x", self.test.definition)
