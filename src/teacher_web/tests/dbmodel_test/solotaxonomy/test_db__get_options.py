from unittest import TestCase, skip
from unittest.mock import Mock, MagicMock, patch
from shared.models.core.db_helper import ExecHelper

import shared.models.cls_solotaxonomy as test_context 

get_options = test_context.SoloTaxonomyModel.get_options
handle_log_info = test_context.handle_log_info


class test_db__get_options(TestCase):
    
    def setUp(self):
        ' fake database context '
        self.fake_db = Mock()
        self.fake_db.cursor = MagicMock()


    def tearDown(self):
        self.fake_db.close()


    def test__should_call_execSql_with_exception(self):
        # arrange
        expected_exception = KeyError("Bang!")

        with patch.object(ExecHelper, 'select', side_effect=expected_exception):
            # act and assert

            with self.assertRaises(Exception):
                get_options(self.fake_db)


    def test__should_call_execSql_return_no_items(self):
        # arrange
        expected_result = []

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act
            
            rows = get_options(self.fake_db, 6079)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                "solotaxonomy__get_options"
                , (6079,)
                , []
                , handle_log_info)

            self.assertEqual(0, len(rows))


    def test__should_call_execSql_return_single_item(self):
        # arrange
        expected_result = [
            (34, "Extended Abstract", 4)
        ]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            rows = get_options(self.fake_db, 6079)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                "solotaxonomy__get_options"
                , (6079,)
                , []
                , handle_log_info)
            
            self.assertEqual(1, len(rows))

            self.assertEqual(34, rows[0].id)
            self.assertEqual("Extended Abstract", rows[0].name)
            self.assertEqual(4, rows[0].lvl)


    def test__should_call_execSql_return_multiple_item(self):
        # arrange
        expected_result = [
            (45, "Prestructural", 1),
            (56, "Unistructural", 2),
            (89, "Multistructural", 3),
            (90, "Relational", 4),
            (999, "Extended Abstract", 5)
        ]

        with patch.object(ExecHelper, 'select', return_value=expected_result):
            # act

            rows = get_options(self.fake_db, 6079)
            
            # assert

            ExecHelper.select.assert_called_with(self.fake_db,
                "solotaxonomy__get_options"
                , (6079,)
                , []
                , handle_log_info)
            
            self.assertEqual(5, len(rows))

            self.assertEqual(45, rows[0].id)
            self.assertEqual("Prestructural", rows[0].name)
            self.assertEqual(1, rows[0].lvl)

            self.assertEqual(999, rows[4].id)
            self.assertEqual("Extended Abstract", rows[4].name)
            self.assertEqual(5, rows[4].lvl)