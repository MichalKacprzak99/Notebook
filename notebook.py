import datetime
import pymongo
#create a database to store notes
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
notes_database = myclient["notes_database"]
notes_col = notes_database["notes"]

#class Note -> just simple note in notebook
class Note:
    def __init__(self, memo):
        '''initialize a note with content, unique id. Automatically set the note's creation date'''
        last_document_id = notes_col.count_documents({})
        note = { "_id": last_document_id, "content": memo, "date_time":  datetime.datetime.utcnow()  }
        notes_col.insert_one(note)
    def match(self, filter):
        '''Determine if this note matches the filter text. Return True if it matches, False otherwise.'''
        filter_doc = {"content": filter}
        if notes_col.find(filter_doc):
            return True

#Note("ala")

print(notes_col.count_documents({}))

