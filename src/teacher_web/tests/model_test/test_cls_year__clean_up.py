from unittest import TestCase
from shared.models.cls_year import YearModel


class test_cls_year__clean_up(TestCase):

    def setUp(self):
        self.test = YearModel(1, "")


    def test_name__trim_whitespace(self):

        self.test.name = " x "

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x", self.test.name)

