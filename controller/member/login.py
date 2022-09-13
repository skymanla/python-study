import config
import bcrypt

class Login():
    def login(self, hp, pwd):
        _dbConfig = config.dbConfig()        
        _member = _dbConfig.getQuery('getOne', 'select * from tb_member_mst where hp = :hp', [hp])
        if not _member:
            return {'code': 0, 'message': '존재하지 않는 회원입니다'}
        _pwd = pwd.encode('utf-8')
        _hasPwd = _member['PWD'].encode('utf-8')
        if not bcrypt.checkpw(_pwd, _hasPwd):
            return {'code': 0, 'message': '존재하지 않는 회원입니다'}
        
        return _member