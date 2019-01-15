from unittest import TestCase
from fake_database import FakeDb

# import test context
import sys
sys.path.insert(0, '../../schemeofwork/modules')
import db_keyword
import db_helper

class test_db_keyword__insert(TestCase):

    def setUp(self):
        ' pass function to this fake class to mock the web2py database functions '
        self.fake_db = FakeDb()
        self.fake_db.connect()

    def tearDown(self):
        self.fake_db.close()


    def test__save_new(self):

        # set up
        rows_before = db_keyword.get_options(self.fake_db, topic_id=1)

        # test
        db_keyword.save(self.fake_db, ["foobar"], topic_id=1)

        rows_after = db_keyword.get_options(self.fake_db, topic_id=1)

        self.assertEqual(len(rows_after), len(rows_before) + 1, "should have added a row: before {} and after {} ".format(len(rows_before), len(rows_after)))


    def test_do_not_save_existing(self):
        # setup
        ' create an existing keyword '
        db_keyword.save(self.fake_db, ["FooBar"], topic_id=1)

        rows_before = db_keyword.get_options(self.fake_db, topic_id=1)

        # test
        db_keyword.save(self.fake_db, ["foobar"], topic_id=1)

        # assert
        rows_after = db_keyword.get_options(self.fake_db, topic_id=1)
        self.assertEqual(len(rows_after), len(rows_before), "should *NOT* have added a row. Before and after should be the same: {} before and {} after".format(len(rows_before), len(rows_after)))


    def test__should_save_all_lowercase(self):
        #set up

        # test
        db_keyword.save(self.fake_db, ["FooBar"],topic_id=1)

        rows = db_keyword.get_options(self.fake_db, topic_id=1)

        for item in rows:
            self.assertTrue(item.islower(), "'{}' is not lower case".format(item))


    def test__should_not_save_leading_or_trailing_whitespace(self):
        #set up

        # test
        db_keyword.save(self.fake_db, [" FooBar "], topic_id=1)

        rows = db_keyword.get_options(self.fake_db, topic_id=1)

        for item in rows:
            self.assertEqual(item.lstrip(' ').rstrip(' '), item, "'{}' is not lower case".format(item))


    def test__should_not_save_empty(self):
        #set up

        # test
        db_keyword.save(self.fake_db, [""], topic_id=1)

        rows = db_keyword.get_options(self.fake_db, topic_id=1)

        for item in rows:
            self.assertTrue(len(item) > 0, "should not save empty")