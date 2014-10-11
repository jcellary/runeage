from flask import g

API_ROOT_ADDRESS = '/runeage/api/v1.0'
API_TEST_ROOT_ADDRESS = '/runeage/test/api/v1.0'
MONGODB_ADDRESS = 'mongodb://localhost:27017/runeage'
MONGODB_TEST_ADDRESS = 'mongodb://localhost:27017/runeage'

REQ_CONTEXT_USE_TEST_DB = 'use_test_db'

FORCE_TEST_ENVIRONMENT = False

def get_use_test_db():
    if FORCE_TEST_ENVIRONMENT == True:
        return True
        
    return getattr(g, REQ_CONTEXT_USE_TEST_DB, False)