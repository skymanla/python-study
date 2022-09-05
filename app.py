from flask import Flask, request
import config

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!!'

@app.route('/connection')
def connection():
    conn = config.dbconfig.conn()
    conn.execute("""select * from tb_member_mst where member_cd = :member_cd""", member_cd = 361)
    rows = conn.fetchall()
    conn.close()
    return rows
    
if __name__ == '__main__':
    app.run(debug=True)