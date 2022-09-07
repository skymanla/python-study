from flask import Flask, request
import config

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!!'

@app.route('/connection')
def connection():
    _dbConfig = config.dbConfig()
    conn = _dbConfig.conn()
    return _dbConfig.getQuery('getOne', "select * from tb_member_mst where member_gbn = :memberGbn", ['P'])
    
if __name__ == '__main__':
    app.run(debug=True)