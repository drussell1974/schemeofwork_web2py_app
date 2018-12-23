
from unittest import TestCase
from datetime import datetime
import sys
sys.path.insert(0, '../')

from cls_learningobjective import LearningObjectiveModel

class Test_LearningObjectiveModel_Constructor(TestCase):

    test = None
    current_date_for_test = ""

    """ Shared functions """
    def setUp(self):
        self.current_date_for_test = datetime.today()


    def tearDown(self):
        pass


    def test_validate_for_default_instance_returns_false(self):

        # setup
        test = LearningObjectiveModel(0)

        # test
        test.validate()

        # validate
        self.assertFalse(test.is_valid)


    def test_constructor_default(self):
        # set up
        test = LearningObjectiveModel(0)

        # assert
        self.assertEqual(0, test.id)
        self.assertEqual("", test.description)
        self.assertEqual(0, test.solo_taxonomy_id)
        self.assertEqual("", test.solo_taxonomy_name)
        self.assertEqual("", test.solo_taxonomy_level)
        self.assertEqual(0, test.topic_id)
        self.assertEqual("", test.topic_name)
        self.assertEqual(0, test.parent_topic_id)
        self.assertEqual("", test.parent_topic_name)
        self.assertEqual(0, test.content_id)
        self.assertEqual("", test.content_description)
        self.assertEqual(0, test.exam_board_id)
        self.assertEqual("", test.exam_board_name)
        self.assertEqual(0, test.learning_episode_id)
        self.assertEqual("", test.learning_episode_name)
        self.assertEqual(0, test.key_stage_id)
        self.assertEqual("", test.key_stage_name)
        self.assertEqual(None, test.parent_id)
        self.assertEqual("", test.created)
        self.assertEqual(0, test.created_by_id)
        self.assertEqual("", test.created_by_name)



    def test_constructor_set_valid_values(self):

        # setup
        test = LearningObjectiveModel(1,
                                      description = "lo test description",
                                      solo_taxonomy_id = 1,
                                      solo_taxonomy_name = "Unistructural",
                                      solo_taxonomy_level = "B",
                                      topic_id = 2,
                                      topic_name = "Algorithms",
                                      parent_topic_id = 3,
                                      parent_topic_name = "Programming",
                                      content_id = 4,
                                      content_description = "Understanding Havard Architecture",
                                      exam_board_id = 5,
                                      exam_board_name = "AQA",
                                      learning_episode_id = 6,
                                      learning_episode_name = "Week 30",
                                      key_stage_id = 7,
                                      key_stage_name = "KS7",
                                      parent_id = 99,
                                      created = self.current_date_for_test,
                                      created_by_id = 8,
                                      created_by_name = "Dave Russell")

        # test
        test.validate()

        # assert
        self.assertEqual(test.description, "lo test description", "--- setup --- description failed")
        self.assertEqual(test.solo_taxonomy_id, 1, "--- setup --- solo_taxonomy_id failed")
        self.assertEqual(test.solo_taxonomy_name, "Unistructural", "--- setup --- solo_taxonomy_name failed")
        self.assertEqual(test.solo_taxonomy_level, "B", "--- setup --- solo_taxonomy_level failed")
        self.assertEqual(test.topic_id, 2, "--- setup --- topic_id failed")
        self.assertEqual(test.topic_name, "Algorithms", "--- setup --- topic_name failed")
        self.assertEqual(test.parent_topic_id, 3, "--- setup --- parent_topic_id failed")
        self.assertEqual(test.parent_topic_name,"Programming", "--- setup --- parent_topic_name failed")
        self.assertEqual(test.content_id, 4, "--- setup --- content_id failed")
        self.assertEqual(test.content_description, "Understanding Havard Architecture", "--- setup --- content_name failed")
        self.assertEqual(test.exam_board_id, 5, "--- setup --- exam_board_id failed")
        self.assertEqual(test.exam_board_name, "AQA", "--- setup --- exam_board_name failed")
        self.assertEqual(test.learning_episode_id, 6, "--- setup --- learning_episode_id failed")
        self.assertEqual(test.learning_episode_name, "Week 30", "--- setup --- learning_episode_name  failed")
        self.assertEqual(test.key_stage_id, 7, "--- setup --- key_stage_id failed")
        self.assertEqual(test.key_stage_name, "KS7", "--- setup --- key_stage_name failed")
        self.assertEqual(test.parent_id, 99, "--- setup --- parent_id failed")
        self.assertEqual(test.created, self.current_date_for_test, "--- setup --- created failed")
        self.assertEqual(test.created_by_id, 8, "--- setup --- created_by_id failed")
        self.assertEqual(test.created_by_name, "Dave Russell", "--- setup --- created_by_name failed")

        self.assertTrue(test.is_valid)
