from dotenv import load_dotenv
import os
import cx_Oracle

os.putenv('NLS_LANG', '.UTF8')

def conn():
    connection = cx_Oracle.connect(os.environ.get('DB_USER'), os.environ.get('DB_PASSWORD'), os.environ.get('DB_HOST'))
    cursor = connection.cursor()
    return cursor