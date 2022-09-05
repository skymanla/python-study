from flask import Flask, request
import config

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!!'

@app.route('/connection')
def connection():
    conn = config.dbconfig.conn()
    with conn.cursor() as cursor:
        cursor.execute("""select * from tb_member_mst where member_gbn = 'P'""")
        cursor.rowfactory = config.dbconfig.makeDictFactory(cursor)
        return cursor.fetchall()
    
if __name__ == '__main__':
    app.run(debug=True)