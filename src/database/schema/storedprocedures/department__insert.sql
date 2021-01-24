DELIMITER //

DROP PROCEDURE IF EXISTS department__insert;

CREATE PROCEDURE department__insert (
    OUT p_department_id INT,
    IN p_name VARCHAR(70),
    IN p_teacher_id INT,
    IN p_school_id INT,
    IN p_created DATETIME,
    IN p_created_by INT)
BEGIN
    -- CHECK sow_department
    INSERT INTO sow_department 
    (
        name, 
        head_id, 
        school_id,
        created, 
        created_by
    )
    VALUES
    (
        p_name,
        p_teacher_id,
        p_school_id,
        p_created,
        p_created_by
    );

	INSERT INTO sow_department__has__teacher (auth_user_id, department_id) 
	VALUES (p_teacher_id, LAST_INSERT_ID());
    
    SELECT LAST_INSERT_ID();
END;
//

DELIMITER ;

