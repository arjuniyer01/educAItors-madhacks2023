from pymongo import MongoClient

cluster = MongoClient(
    "mongodb+srv://shivam:EDUCATOR1234@cluster0.lglwhpk.mongodb.net/?retryWrites=true&w=majority"
)

db = cluster["educators"]
collection = db["Users"]


def set_user(email: str):
    result = collection.find_one({"email": email})
    if result is None:
        collection.insert_one(
            {
                "email": email,
                "progress": {},
                "role": "student",
                "phone": "",
                "name": "",
                "age": 18,
                "location": "United States",
                "language": "English",
            }
        )


def get_user_id(email: str) -> str:
    return collection.find_one({"email": email})["_id"]


def get_settings(user_id: str) -> dict:
    return collection.find_one({"_id": user_id})


def update_settings(user_id: str, settings: dict):
    collection.update_one({"_id": user_id}, {"$set": settings})


def update_progress(user_id: str, progress: dict):
    collection.update_one({"_id": user_id}, {"$set": {"progress": progress}})


def get_progress(user_id: str) -> dict:
    return collection.find_one({"_id": user_id})["progress"]


def get_email(token: str) -> str:
    result = collection.find_one({"_id": token})
    return result["email"]


def get_phone_number(token: str) -> str:
    result = collection.find_one({"_id": token})
    return result["phone"]


# Takes user token and returns user's role (student/teacher)
def get_role(token: str) -> str:
    result = collection.find_one({"_id": token})
    return result["role"]
