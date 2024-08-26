import json
import csv
import bson
from pymongo import MongoClient
def read_json():
    # data
    with open("employees.json", 'r') as file:
        data = json.load(file) 

    for employee in data["employees"]:
        print(f"name: {employee["name"]} age: {employee["age"]} city: {employee["city"]}")

def read_csv():
    with open('employees_csv.csv', mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)

def read_bson():
    with open('person_info.bson', 'rb') as file:
        data = json.load(file)  # Decoding BSON data

    # Process and print the data
    print(f"Name: {data['name']}")
    print("Interests:")
    for interest in data['interests']:
        print(f" - {interest}")
    
    print("Address:")
    print(f"  Country: {data['address']['country']}")
    print(f"  City: {data['address']['city']}")
    print(f"  Street: {data['address']['street']}")

def read_mongo_db():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['PersonInfo']
    collection = db['PersonInfo']
     # Retrieve all documents from the collection
    documents = collection.find()
    one_user={
                "name":"Bob", 
                "interests":["playing games", "writing code"], 
                "address":{
                    "country":"USA", 
                    "city": "San Jose", 
                    "street":"1248 corner st"
                }
              }
    # Loop through and print each document
    for document in documents:
        print(document)
    result=collection.insert_one(one_user)
    print(f"Insert user with userid:{result.inserted_id}")


def main():
    # read_json()
    # read_csv()
    read_mongo_db()

if __name__=='__main__':
    main()