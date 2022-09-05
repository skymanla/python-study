from dotenv import load_dotenv
import os
import cx_Oracle

os.putenv('NLS_LANG', '.UTF8')

def conn():
    connection = cx_Oracle.connect(os.environ.get('DB_USER'), os.environ.get('DB_PASSWORD'), os.environ.get('DB_HOST'), encoding="UTF-8")
    return connection

def makeDictFactory(cursor):
    columnNames = [d[0] for d in cursor.description]
    
    def createRow(*args):
        return dict(zip(columnNames, args))
    
    return createRow