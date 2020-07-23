from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper

import shared.models.cls_keyword as test_context 

get_all = test_context.KeywordDataAccess.get_all
handle_log_info = test_context.handle_log_info

class test_db__get_all(TestCase):


    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()

    def tearDown(self):
        self.fake_db.close()


    def test__should_call_execSql_with_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'execSql', side_effect=expected_exception):
            # act and assert

            with self.assertRaises(Exception):
                get_all(self.fake_db)


    def test__should_call_execSql_return_no_items(self):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act
            
            rows = get_all(self.fake_db)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT id as id, name as term, definition as definition FROM sow_key_word kw WHERE published = 1 ORDER BY name;"
                , []
                , log_info=handle_log_info)
                
            self.assertEqual(0, len(rows))


    def test__should_call_execSql_return_single_item(self):
        # arrange
        expected_result = [
            (702, "Fringilla", "purus lacus, ut volutpat nibh euismod.")
            ]

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            actual_results = get_all(self.fake_db)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT id as id, name as term, definition as definition FROM sow_key_word kw WHERE published = 1 ORDER BY name;"
                , []
                , log_info=handle_log_info)
                

            self.assertEqual(1, len(actual_results))

            self.assertEqual(702, actual_results[0].id)
            self.assertEqual("Fringilla", actual_results[0].term),
            self.assertEqual("purus lacus, ut volutpat nibh euismod.", actual_results[0].definition)


    def test__should_call_execSql_return_multiple_item(self):
        # arrange
        expected_result = [
            (1021, "Vestibulum", "nec arcu nec dolor vehicula ornare non."),
            (1022, "Fringilla", "purus lacus, ut volutpat nibh euismod."),
            (1023, "Phasellus", "rutrum lorem a arcu ultrices, id mollis")
        ]

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            actual_results = get_all(self.fake_db, "a")
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT id as id, name as term, definition as definition FROM sow_key_word kw WHERE published = 1 AND name LIKE '%a%' ORDER BY name;"
                 , []
                 , log_info=handle_log_info)

            self.assertEqual(3, len(actual_results))

            self.assertEqual(1021, actual_results[0].id)
            self.assertEqual("Vestibulum", actual_results[0].term),
            self.assertEqual("nec arcu nec dolor vehicula ornare non.", actual_results[0].definition)


            self.assertEqual(1023, actual_results[2].id)
            self.assertEqual("Phasellus", actual_results[2].term),
            self.assertEqual("rutrum lorem a arcu ultrices, id mollis", actual_results[2].definition)


    def test__should_call_execSql_with_empty_search_term(self):
        # arrange
        expected_result = [
            (702, "Fringilla", "purus lacus, ut volutpat nibh euismod.")
            ]

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            actual_results = get_all(self.fake_db, search_term="")
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT id as id, name as term, definition as definition FROM sow_key_word kw WHERE published = 1 ORDER BY name;"
                , []
                , log_info=handle_log_info)

            self.assertEqual(1, len(actual_results))

            self.assertEqual(702, actual_results[0].id)
            self.assertEqual("Fringilla", actual_results[0].term),
            self.assertEqual("purus lacus, ut volutpat nibh euismod.", actual_results[0].definition)


    def test__should_call_execSql_with_default_search_term(self):
        # arrange
        expected_result = [
            (21, "Phasellus", "rutrum lorem a arcu ultrices, id mollis"),
            (22, "Fringilla", "purus lacus, ut volutpat nibh euismod."),
            (23, "Vestibulum", "nec arcu nec dolor vehicula ornare non.")
        ]

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            actual_results = get_all(self.fake_db)
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT id as id, name as term, definition as definition FROM sow_key_word kw WHERE published = 1 ORDER BY name;"
                , []
                , log_info=handle_log_info)

            self.assertEqual(3, len(actual_results))

            self.assertEqual(21, actual_results[0].id)
            self.assertEqual("Phasellus", actual_results[0].term),
            self.assertEqual("rutrum lorem a arcu ultrices, id mollis", actual_results[0].definition)

            self.assertEqual(23, actual_results[2].id)
            self.assertEqual("Vestibulum", actual_results[2].term),
            self.assertEqual("nec arcu nec dolor vehicula ornare non.", actual_results[2].definition)



    def test__should_call_execSql_with_entered_search_term(self):
        # arrange
        expected_result = [
            (702, "Fringilla", "purus lacus, ut volutpat nibh euismod.")
            ]

        with patch.object(ExecHelper, 'execSql', return_value=expected_result):
            # act

            actual_results = get_all(self.fake_db, search_term="Fringilla")
            
            # assert

            ExecHelper.execSql.assert_called_with(self.fake_db,
                "SELECT id as id, name as term, definition as definition FROM sow_key_word kw WHERE published = 1 AND name LIKE '%Fringilla%' ORDER BY name;"
                , []
                , log_info=handle_log_info)

            self.assertEqual(1, len(actual_results))

            self.assertEqual(702, actual_results[0].id)
            self.assertEqual("Fringilla", actual_results[0].term),
            self.assertEqual("purus lacus, ut volutpat nibh euismod.", actual_results[0].definition)
