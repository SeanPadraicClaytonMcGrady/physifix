import os
import django
import json

#I ran this manually to get hashed passwords for our seed data. 

from django.contrib.auth.hashers import make_password

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "physifix.settings")
django.setup()


def seed_data():
    #Password for all test users.
    hashed_password = make_password('12345')

    lower_back_region = {
        "model" : "server.region",
        "pk" : 1,
        "fields" : {
            "name" : "Lower Back"
        }
    }
    
    load_intolerance = {
        "model" : "server.diagnostic",
        "pk" : 1,
        "fields" : {
            "name" : "Load Intolerance",
            "video" : "https://youtu.be/PV4pUmkbXzc?si=HkBi6HWHJm7mOOch&t=35",
            "description" : "This test assesses your exposure to pain under spinal load.",
            "region": 1
        }
    }
    
    john = {
        "model" : "server.user",
        "pk" : 1,
        "fields" : {
            "first_name": "John",
            "last_name": "Doe",
            "email" : "john@john.com",
            "username" : "john_1",
            "password" : hashed_password,
            "bookmarks" : []
        }
    }
    
    jane = {
        "model" : "server.user",
        "pk" : 2,
        "fields" : {
            "first_name": "Jane",
            "last_name": "Doe",
            "email" : "jane@jane.com",
            "username" : "jane_2",
            "password" : hashed_password,
            "bookmarks" : []
        }
    }
    
    seed_data_users = [john, jane]
    seed_data_regions = [lower_back_region]
    seed_data_diagnostic = [load_intolerance]
    
    with open("server/seed_data/users.json", "w") as json_file:
        json.dump(seed_data_users, json_file, indent=2)
        
    with open("server/seed_data/regions.json", "w") as json_file:
        json.dump(seed_data_regions, json_file, indent=2)
        
    with open("server/seed_data/diagnostics.json", "w") as json_file:
        json.dump(seed_data_diagnostic, json_file, indent=2)
    
    
    
    

if __name__ == '__main__' : 
    seed_data()