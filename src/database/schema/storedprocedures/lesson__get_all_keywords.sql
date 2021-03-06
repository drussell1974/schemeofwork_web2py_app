DELIMITER $$
DROP PROCEDURE IF EXISTS lesson__get_all_keywords;

CREATE PROCEDURE `lesson__get_all_keywords`(
 IN p_lesson_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
      SELECT 
            kw.id as id, 
            kw.name as term, 
            kw.definition as definition,
            kw.scheme_of_work_id as scheme_of_work_id,
            kw.published as published,
            kw.created as created
      FROM sow_lesson__has__key_words as lkw 
            INNER JOIN sow_key_word kw ON kw.id = lkw.key_word_id 
      WHERE 
            lkw.lesson_id = p_lesson_id
            AND (p_show_published_state % published = 0 
                   or kw.created_by = p_auth_user)
      ORDER BY kw.name;
END$$
DELIMITER ;
