from ming import create_datastore, Session, collection, Field, Document, schema

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

#{ target_player_count : 3, current_players : [ { name: 'Player1', race: 'Undead'}, { name: 'Player2', race: 'Undead'}]}