import sys
sys.path.append('../../schemeofwork/modules')
sys.path.append('../')

from learningobjective_testcase import LearningObjective_TestCase


class test_learningobjective__clean_up__topic_name(LearningObjective_TestCase):

    def setUp(self):
        self.test = self._construct_valid_object()

    def test__trim_whitespace(self):
        test = self._construct_valid_object()

        test.topic_name = " x "

        # test
        test._clean_up()

        # assert
        self.assertEqual(test.topic_name, "x")


    def test__escape_sqlterminator(self):

        self.test.topic_name = "x;"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x\;", self.test.topic_name)


    def test__escape_quote(self):

        self.test.topic_name = "'x'"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual('"x"', self.test.topic_name)


class test_learningobjective__clean_up__parent_topic_name(LearningObjective_TestCase):

    def setUp(self):
        self.test = self._construct_valid_object()

    def test__trim_whitespace(self):
        test = self._construct_valid_object()

        test.parent_topic_name = " x "

        # test
        test._clean_up()

        # assert
        self.assertEqual(test.parent_topic_name, "x")


    def test__escape_sqlterminator(self):

        self.test.parent_topic_name = "x;"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x\;", self.test.parent_topic_name)


    def test__escape_quote(self):

        self.test.parent_topic_name = "'x'"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual('"x"', self.test.parent_topic_name)


class test_learningobjective__clean_up__content_description(LearningObjective_TestCase):

    def setUp(self):
        self.test = self._construct_valid_object()

    def test__trim_whitespace(self):
        test = self._construct_valid_object()

        test.content_description = " x "

        # test
        test._clean_up()

        # assert
        self.assertEqual(test.content_description, "x")


    def test__escape_sqlterminator(self):

        self.test.content_description = "x;"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x\;", self.test.content_description)


    def test__escape_quote(self):

        self.test.content_description = "'x'"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual('"x"', self.test.content_description)


class test_learningobjective__clean_up__exam_board_name(LearningObjective_TestCase):

    def setUp(self):
        self.test = self._construct_valid_object()

    def test__trim_whitespace(self):
        test = self._construct_valid_object()

        test.exam_board_name = " x "

        # test
        test._clean_up()

        # assert
        self.assertEqual(test.exam_board_name, "x")


    def test__escape_sqlterminator(self):

        self.test.exam_board_name = "x;"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x\;", self.test.exam_board_name)


    def test__escape_quote(self):

        self.test.exam_board_name = "'x'"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual('"x"', self.test.exam_board_name)


class test_learningobjective__clean_up__learning_episode_name(LearningObjective_TestCase):

    def setUp(self):
        self.test = self._construct_valid_object()

    def test__trim_whitespace(self):
        test = self._construct_valid_object()

        test.learning_episode_name = " x "

        # test
        test._clean_up()

        # assert
        self.assertEqual(test.learning_episode_name, "x")


    def test__escape_sqlterminator(self):

        self.test.learning_episode_name = "x;"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x\;", self.test.learning_episode_name)


    def test__escape_quote(self):

        self.test.learning_episode_name = "'x'"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual('"x"', self.test.learning_episode_name)


class test_learningobjective__clean_up__key_stage_name(LearningObjective_TestCase):

    def setUp(self):
        self.test = self._construct_valid_object()

    def test__trim_whitespace(self):
        test = self._construct_valid_object()

        test.key_stage_name = " x "

        # test
        test._clean_up()

        # assert
        self.assertEqual(test.key_stage_name, "x")


    def test__escape_sqlterminator(self):

        self.test.key_stage_name = "x;"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x\;", self.test.key_stage_name)


    def test__escape_quote(self):

        self.test.key_stage_name = "'x'"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual('"x"', self.test.key_stage_name)


class test_learningobjective__clean_up__key_words(LearningObjective_TestCase):

    def setUp(self):
        self.test = self._construct_valid_object()

    def test__trim_whitespace(self):
        test = self._construct_valid_object()

        test.key_words = " x "

        # test
        test._clean_up()

        # assert
        self.assertEqual("x", test.key_words)


    def test__multiple_items(self):
        test = self._construct_valid_object()

        test.key_words = "w x, y, z "

        # test
        test._clean_up()

        # assert
        self.assertEqual("w x,y,z", test.key_words)


    def test__escape_sqlterminator(self):

        self.test.key_words = "x;"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual("x\;", self.test.key_words)


    def test__escape_quote(self):

        self.test.key_words = "'x'"

        # test
        self.test._clean_up()

        # assert
        self.assertEqual('"x"', self.test.key_words)
