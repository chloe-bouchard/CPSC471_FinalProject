from Database import mysql
from App import app

class Location:
    #set engg type data member (String)
    def __init__(self, PostalCode, City, Address):
        self.PostalCode = PostalCode
        self.City = City
        self.Address = Address
