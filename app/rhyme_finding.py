from pymongo import MongoClient

def prepare_connection_to_db_texts():
    client = MongoClient("mongo:27017", username="root", password="example")
    db = client.rhymes_db
    collection = db.done_texts
    return collection

 
