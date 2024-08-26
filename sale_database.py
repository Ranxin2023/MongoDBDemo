from pymongo import MongoClient
import random
import string
class MongoSaleDatabase:
    def __init__(self) -> None:
        self.client=MongoClient('mongodb://localhost:27017/')
        self.db = self.client['PersonInfo']
        self.collection = self.db['Sales']

    def generate_id(self):
        sale_id=''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        while True:
            if not self.collection.find_one({"sale_id":sale_id}):
                return sale_id

    def insert_sales(self, sale_id, french_fries=0, big_mac=0, double_cheese_burger=0):
        sales_data = [
            {"product":"French Fries","sale_id":sale_id, "company": "Mcdonald's", "price":1.50, "quantity":french_fries},
            {"product":"Big Mac", "sale_id":sale_id,"company": "Mcdonald's", "price":5.15, "quantity":big_mac},
            {"product":"Double Cheese Burger", "sale_id":sale_id,"company": "Mcdonald's", "price":3.49, "quantity":double_cheese_burger}
        ]
        self.collection.insert_many(sales_data)
        print("sales added successfully")

    def analyze_sales(self, sale_id):
        pipeline = [
            {"$match": {"sale_id": sale_id}},
            {
                "$group": {
                    "_id": "sale_id",
                    "total_sales": {"$sum": {"$multiply": ["$quantity", "$price"]}},
                    "average_price": {"$avg": "$price"}
                }
            },
            {"$sort": {"total_sales": -1}}
        ]
        result = self.collection.aggregate(pipeline)

        for doc in result:
            print(doc)

def main():
    db=MongoSaleDatabase()
    while True:
        print("Enter the option:")
        option=input()
        if option=='exit':
            break
        try:
            sale_id=db.generate_id()
            print("Enter the number for franch fries:")
            french_fries=int(input())
            print("Enter the number for bigmac:")
            big_mac=int(input())
            print("Enter the number for double cheese burger:")
            double_cheese_burger=int(input())
            db.insert_sales(sale_id=sale_id, french_fries=french_fries, big_mac=big_mac, double_cheese_burger=double_cheese_burger)
            db.analyze_sales(sale_id=sale_id)
        except ValueError:
            print("Error: cannot convert to number")

if __name__=='__main__':
    main()