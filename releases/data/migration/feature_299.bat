mysql -u drussell1974 -p cssow_api < ../../database/schema/tables/alter_table__sow_lesson__has__keywords.sql
mysql -u drussell1974 -p cssow_api < ../../database/schema/storedprocedures/keyword__delete_unpublished.sql
mysql -u drussell1974 -p cssow_api < ../../database/schema/storedprocedures/keyword__publish.sql
mysql -u drussell1974 -p cssow_api < ../../database/schema/storedprocedures/keyword__get.sql
mysql -u drussell1974 -p cssow_api < ../../database/schema/storedprocedures/keyword__get_options.sql
mysql -u drussell1974 -p cssow_api < ../../database/schema/storedprocedures/lesson__get_by_keyword.sql
mysql -u drussell1974 -p cssow_api < ../../database/schema/storedprocedures/lesson__get_all_keywords.sql
mysql -u drussell1974 -p cssow_api < ../../database/schema/storedprocedures/lesson_learning_objective__get_all.sql
mysql -u drussell1974 -p cssow_api < ../../database/schema/storedprocedures/keyword__merge_duplicates.sql
