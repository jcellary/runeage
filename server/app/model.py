from ming import create_datastore, Session, collection, Field, Document, schema
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature
from passlib.apps import custom_app_context as pwd_context

import settings

class Repository:

    __prod_instance = None
    __test_instance = None
    
    @staticmethod
    def get_instance():
        
        if settings.get_use_test_db() == False:
            return Repository.get_prod_instance()
        else:
            return Repository.get_test_instance()

    @staticmethod
    def get_prod_instance():
        if Repository.__prod_instance is None:
            Repository.__prod_instance = Repository(settings.MONGODB_ADDRESS)
        
        return Repository.__prod_instance
    
    @staticmethod
    def get_test_instance():
        if Repository.__test_instance is None:
            Repository.__test_instance = Repository(settings.MONGODB_TEST_ADDRESS)
        
        return Repository.__test_instance
        
    def hash_password(self, password):
        return pwd_context.encrypt(password)

    def verify_password(self, password, password_hash):
        try:
            return pwd_context.verify(password, password_hash)
        except ValueError:
            return False
        
    def generate_auth_token(self, user_id, expiration = 600):
        s = Serializer(settings.SECRET_KEY, expires_in = expiration)
        return s.dumps({ 'id': user_id })

    def verify_auth_token(self, token):
        s = Serializer(settings.SECRET_KEY)
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None # valid token, but expired
        except BadSignature:
            return None # invalid token
        user = User.m.find(dict(_id=data['id'])).first()
        return user
    
    def __init__(self, db_address):
        bind = create_datastore(db_address)
        session = Session(bind)

        self.OpenGame = collection(
            'OpenGames', session,
            Field('_id', schema.ObjectId),
            Field('target_player_count', int),
            Field('current_players', [dict(
                name=str,
                race=str
            )]))

        self.User = collection(
            'Users', session,
            Field('_id', schema.ObjectId),
            Field('username', str),
            Field('password', str))

#{ target_player_count : 3, current_players : [ { name: 'Player1', race: 'Undead'}, { name: 'Player2', race: 'Undead'}]}