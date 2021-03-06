DELIMITER //

DROP PROCEDURE IF EXISTS lesson_learning_objective__get_all;

CREATE PROCEDURE lesson_learning_objective__get_all (
 IN p_lesson_id INT,
 IN p_scheme_of_work_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
    SELECT
        lob.id as id,
        lob.description as description,
        solo.id as solo_id,
        solo.name as solo_taxonomy_name,
        solo.lvl as solo_taxonomy_level,
        cnt.id as content_id,
        cnt.description as content_description,
        sow.key_stage_id as key_stage_id,
        ks.name as key_stage_name,
        le.id as lesson_id,
        le.order_of_delivery_id as order_of_delivery, -- lesson_name,
        lob.key_words as key_words,
        lob.notes as notes,
        lob.missing_words_challenge as missing_words_challenge,
        lob.group_name as group_name,
        le_lo.is_key_objective as is_key_objective,
        lob.created as created,
        lob.created_by as created_by_id,
        user.first_name as created_by_name,
        le_lo.published as published
    FROM sow_scheme_of_work as sow  
    INNER JOIN sow_lesson as le ON le.scheme_of_work_id = sow.id
    INNER JOIN sow_learning_objective__has__lesson as le_lo ON le_lo.lesson_id = le.id
    INNER JOIN sow_learning_objective as lob ON lob.id = le_lo.learning_objective_id
    LEFT JOIN sow_key_stage as ks ON ks.id = sow.key_stage_id
    LEFT JOIN sow_solo_taxonomy as solo ON solo.id = lob.solo_taxonomy_id
    LEFT JOIN sow_content as cnt ON cnt.id = lob.content_id
    LEFT JOIN auth_user as user ON user.id = lob.created_by
    WHERE le.id = p_lesson_id AND sow.id = p_scheme_of_work_id 
        AND (
			p_show_published_state % lob.published = 0
			or p_show_published_state % sow.published = 0
			or lob.created_by = p_auth_user or sow.created_by = p_auth_user
		)
	ORDER BY solo_taxonomy_level;
END;
//

DELIMITER ;