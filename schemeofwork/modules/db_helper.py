# -*- coding: utf-8 -*-

"""
helper routines for retrieving and saving values in the database
"""
last_sql = ()

def to_db_null(val):
    return "NULL" if val is None else val

