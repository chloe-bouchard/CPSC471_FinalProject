from Database import mysql
from App import app
#Author: Gibran Akmal

#initialize class
class Donor:
    #set engg type data member (String)
    def __init__(self, FirstName, LastName, Birthdate, Gender, Password, Email, HealthNumber, Weight):
        self.account = Account(FirstName, LastName, Birthdate, Gender, Password, Email)
        self.HealthNumber = HealthNumber
        self.Weight = Weight
