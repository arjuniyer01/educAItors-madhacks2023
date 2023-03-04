import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://shivam:EDUCATOR1234@cluster0.lglwhpk.mongodb.net/?retryWrites=true&w=majority")

db = cluster["educators"]
collection = db["Users"]


def get_email(token: str) -> str:
    result = collection.find_one({"_id":token})
    return 

def get_phone_number(token: str) -> str:
    result = collection.find_one({"_id":token})
    return result["phone"]

# Takes user token and returns user's progress
def get_progress(token: str) -> dict:
    result = collection.find_one({"_id":token})
    return result["progress"]

# Takes user token and returns user's role (student/teacher)
def get_role(token: str) -> str:
    result = collection.find_one({"_id":token})
    return result["role"]

print(get_progress("shivam10nanda@gmail.com"))