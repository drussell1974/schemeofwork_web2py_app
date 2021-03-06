DELIMITER //

DROP PROCEDURE IF EXISTS department__get_all;

CREATE PROCEDURE department__get_all (
 IN p_institute_id INT,
 IN p_show_published_state INT,
 IN p_auth_user INT)
BEGIN
    SELECT 
        dep.id as id,
        dep.name as name,
        dep.institute_id as institute_id,
        dep.created as created,
        dep.created_by as created_by,
        usr.first_name as created_by_name,
        dep.published as published
    FROM 
        sow_department as dep
        INNER JOIN auth_user as usr ON usr.id = dep.created_by
    WHERE 
		dep.institute_id = p_institute_id 
        and (p_show_published_state % published = 0 
			or dep.created_by = p_auth_user)
    ORDER BY dep.name;
END;
//

DELIMITER ;

CALL department__get_all(2,32, 2);