from tinydb import TinyDB,Query
import random
import string
db = TinyDB('db.json')

data = db.table("data")

users = db.table("users")
query = Query()

staff = db.table("staff")
documents = db.table("documents")




def register_users_student(username,password):
    if users.contains((query.username == username) & (query.password == password)):
        print("user already exists")
        return "-1"
    print(password)
    users.insert({"username":username,"password":password})
    return "1"

def login_student(username,password,role):
    if users.contains((query.username == username) & (query.password == password)):
        return "1"
    else:
        return "-1"
    
def register_users_staff(username,password):
    if staff.contains((query.username == username) & (query.password == password)):
        print("user already exists")
        return "-1"
    print(password)
    staff.insert({"username":username,"password":password})
    return "1"

def login_staff(username,password,role):
    if staff.contains((query.username == username) & (query.password == password)):
        return "1"
    else:
        return "-1"
    
    


def insert_document(contents,us):
    pass

def get_document(document_id,user_id):
    pass

def storeContent(assignment_number,html_content,copy_content):
    pass

def get_all_documents(userid):
    #return all document ids.
    pass


def compare_documents(document1,document2):
    pass