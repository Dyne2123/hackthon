from tinydb import TinyDB,Query
import random
import string
db = TinyDB('db.json')

data = db.table("data")

users = db.table("users")
query = Query()

documents = db.table("documents")

def generate_unique_key(length=16):
   
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))



def register_users(username,password,role,user_id,user_key):
    if users.contains((query.username == username) & (query.password == password) & (query.user_id == user_id)):
        print("user already exists")
        return "-1"
    users.insert({"username":username,"password":password,"user_key":user_key,"user_id":user_id,"role":role})
    return "1"

def authenticate_users(username,password,role,userkey):
    if users.contains((query.username == username) & (query.password == password) & (query.user_key == userkey)):
        return "1"
    else:
        return "-1"


def get_document(document_id,user_id):
    pass

def storeContent(assignment_number,html_content,copy_content):
    pass

def get_all_documents(userid):
    #return all document ids.
    pass