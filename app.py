from flask import Flask, request
import config
import controller

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!!'

@app.route('/connection')
def connection():
    _dbConfig = config.dbConfig()    
    _data = _dbConfig.getQuery('getOne', "select * from tb_member_mst where member_gbn = :memberGbn", ['P'])
    if (_data == None):
        return {'code': 0, 'message': '존재하지 않는 회원입니다'}
    
    return {'code': 0, 'message': '', 'data': _data}

@app.route('/member/login', methods=['POST'])
def login():
    params = request.get_json()
    if not params:
        return 'No parameter'
    _login = controller.Login()
    return _login.login(params['hp'], params['pwd'])
    
if __name__ == '__main__':
    app.run(debug=True)