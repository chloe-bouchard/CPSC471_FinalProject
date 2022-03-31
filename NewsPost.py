from Database import mysql
from App import app

#initialize class
class NewsPost:
    #set engg type data member (String)
    def __init__(self, ID, Date, Body, Title):
        self.ID = ID
        self.Date = Date
        self.Body = Body
        self.Title = Title
        
