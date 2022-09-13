from contextlib import nullcontext
from typing import final
from dotenv import load_dotenv
import os
import cx_Oracle

os.putenv('NLS_LANG', '.UTF8')

class dbConfig:
    def __init__(self):
        self.user = os.environ.get('DB_USER')
        self.pwd = os.environ.get('DB_PASSWORD')
        self.host = os.environ.get('DB_HOST')
    
    def conn(self):
        connection = cx_Oracle.connect(self.user, self.pwd, self.host, encoding="UTF-8")
        return connection

    def makeDictFactory(self, cursor):
        columnNames = [d[0] for d in cursor.description]
        
        def createRow(*args):
            return dict(zip(columnNames, args))
        
        return createRow
        
    def getQuery(self, _type, _query, _values = []):
        _conn = self.conn()
        try:    
            with _conn.cursor() as cursor:
                cursor.execute(_query, _values)
                cursor.rowfactory = self.makeDictFactory(cursor)
                if (_type == 'getAll'):
                    return cursor.fetchall()
                else:
                    return cursor.fetchone()
        finally:
            _conn.close()