from Database import mysql
from App import app

#initialize class
class BloodType:
    #set engg type data member (String)
    def __init__(self, Group, Rh):
        self.Group = Group
        self.Rh = Rh
