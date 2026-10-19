# ==============================================================================
# FILE: db_lab/db_layer.py
# PURPOSE: Pure MongoDB Client Connection Configuration Layer via PyMongo.
# DETAILS: Instantiates the local driver and provides safety verification checks.
# ==============================================================================

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# Initialize the global MongoDB client pointing to your local database engine instance
# Added low timeout constraint so your application does not hang if the process is down
try:
    client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=3000)
except Exception as e:
    client = None

def get_mongo_collection():
    """
    Utility connector that safely extracts your target collection sandbox block.
    Returns None if the instance driver handshake encounters immediate failure.
    """
    if client is None:
        return None
    try:
        # Force active diagnostic ping call checks to confirm connection viability
        client.admin.command('ping')
        
        # Access database named 'practice_db' and collection named 'practice_collection'
        db = client['practice_db']
        return db['practice_collection']
    except ConnectionFailure:
        return None
