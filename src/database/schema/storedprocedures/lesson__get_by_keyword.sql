DELIMITER //

DROP PROCEDURE IF EXISTS lesson__get_by_keyword;

CREATE PROCEDURE lesson__get_by_keyword (
 IN p_key_word_id INT,
 IN p_scheme_of_work_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
     SELECT  
        le.id as id, 
        le.title as title, 
        le.order_of_delivery_id as order_of_delivery_id, 
        le.scheme_of_work_id as scheme_of_work_id, 
        sow.name as scheme_of_work_name, 
        le.content_id as content_id,
        cnt.description as content_description,
        top.id as topic_id, 
        top.name as topic_name, 
        pnt_top.id as parent_topic_id, 
        pnt_top.name as parent_topic_name, 
        sow.key_stage_id as key_stage_id, 
        yr.id as year_id, yr.name as year_name, 
        le.summary as summary, 
        le.created as created, 
        le.created_by as created_by_id, 
        user.first_name as created_by_name, 
        le.published as published 
    FROM sow_lesson as le  
    INNER JOIN sow_lesson__has__key_words as lkw ON lkw.lesson_id = le.id
    INNER JOIN sow_scheme_of_work as sow ON sow.id = le.scheme_of_work_id 
    INNER JOIN sow_year as yr ON yr.id = le.year_id 
    LEFT JOIN sow_topic as top ON top.id = le.topic_id  
    LEFT JOIN sow_topic as pnt_top ON pnt_top.id = top.parent_id  
    LEFT JOIN sow_content as cnt ON cnt.id = le.content_id
    LEFT JOIN auth_user as user ON user.id = sow.created_by  
    WHERE 
		lkw.key_word_id = p_key_word_id
        AND 
        le.scheme_of_work_id = p_scheme_of_work_id
        AND (p_show_published_state % sow.published = 0 
				or p_show_published_state % le.published = 0 
                or sow.created_by = p_auth_user 
				or le.created_by = p_auth_user 
			)
    ORDER BY le.year_id, le.order_of_delivery_id;
END;
//

DELIMITER ;