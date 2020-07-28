# -*- coding: utf-8 -*-
"""
helper routines for retrieving and saving values in the database
"""
import mysql.connector


class ExecHelper:
    #############################
    # TODO: create as singleton #
    #############################
    last_sql = ()
    def _log_it(self, db, sql, enable_logging):
        l = log.Log();
        l.is_enabled = enable_logging
        l.write(db, sql)

    def _execSql(self, db, sql):

        with db.cursor() as cur:
            cur.execute(sql)
            result = cur.fetchall()
        return result


    def _closeSqlConn(self, db, cursor):
            #cursor.close()
            db.close()

    def execCRUDSql(self, db, sql, result=[], log_info=None):
        ''' run the sql statement without results '''

        last_insert_id = 0
        if db != None:

            if log_info != None:
                log_info(db, "executing:{}".format(sql))

            cur = self._execSql(db, sql)
            for tup in cur:
                result.append(tup)
            
            cur_li = self._execSql(db, "SELECT LAST_INSERT_ID();")
            last_insert_id = int(cur_li[0][0])


            db.commit()    
            self._closeSqlConn(db, None)

            if log_info != None:
                log_info(db, "result:{}".format(result))
        
        return (result, last_insert_id)


    def execSql(self, db, sql, result, log_info=None):
        ''' run the sql statement '''
        if db != None:

            if log_info != None:
                log_info(db, "executing:{}".format(sql))
            
            cur = self._execSql(db, sql)
            for tup in cur:
                result.append(tup)
            self._closeSqlConn(db, None)

            if log_info != None:
                log_info(db, "results:{}".format(result))

        # returns appended result
        return result


def to_db_null(val, as_null = None):
    return "NULL" if val is None or val is as_null else sql_safe(val)


def to_empty(val):
    return "" if val is None else val


def to_db_bool(val):
    return 1 if val == True else 0


def from_db_bool(val):
    return True if val == 1 else False


def sql_safe(string):
    return str(string)\
        .strip(' ')\
        .replace("'", "\"")\
        .replace(";", "\;")