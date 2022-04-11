# from Database import mysql
from App import app
import mysql.connector

#initialize class
class BloodType:
    #set engg type data member (String)
    def __init__(self, Group, Rh, ID, connection):
        self.ID = ID
        self.Group = Group
        self.Rh = Rh
        self.connection = connection

    def executeQuery(self,query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result


    def get_group(self):
        if(self.ID == 1 or self.ID == 2):
            return "A"
        elif(self.ID == 3 or self.ID == 4):
            return "B"
        elif(self.ID == 5 or self.ID== 6):
            return "O"
        elif(self.ID == 7 or self.ID == 8):
            return "AB"
    # def get_group(self):
    #     userQuery = "SELECT group FROM blood_type WHERE 'idblood_type' = " + str(self.ID) + ";"
    #     result = self.executeQuery(userQuery)
    #     convert = str(result)
    #     convert = convert[2:len(convert) - 3]
    #     return convert

    def get_rh(self):
        if(self.ID == 1 or self.ID == 4 or self.ID ==5 or self.ID ==8):
            return "Positive"
        else:
            return "Negative"
    # def get_ID(self):
    #     userQuery = "SELECT idblood_type FROM blood_type WHERE 'group' = '" + str(self.Group) + "';"# "' AND 'rhesus_factor' = '" + str(self.Rh) + 
    #     # result = self.executeQuery(userQuery)
    #     # val = (group)
    #     cursor = self.connection.cursor()
    #     cursor.execute(userQuery)
        
    #     print("convert")
    #     print(cursor.fetchall())
    #     return(cursor.fetchall())
       
    # def get_ID(self):   
    #     userQuery = "SELECT idblood_type FROM blood_type WHERE 'group' = 'A';"
    #     result = self.executeQuery(userQuery)
    #     convert = str(result)
    #     print("print of result")
    #     print(result)
    #     convert = convert[1:len(convert) - 3]
    #     print(convert)
    #     return convert

    def get_ID(self):
        if(self.Group == "A" and self.Rh == "Positive"):
            return 1
        elif (self.Group == "A" and self.Rh == "Negative"):
            return 2
        elif (self.Group == "B" and self.Rh == "Positive"):
            return 4
        elif (self.Group == "B" and self.Rh == "Negative"):
            return 3
        elif (self.Group == "AB" and self.Rh == "Positive"):
            return 8
        elif (self.Group == "AB" and self.Rh == "Negative"):
            return 7
        elif (self.Group == "O" and self.Rh == "Positive"):
            return 5
        elif (self.Group == "O" and self.Rh == "Negative"):
            return 6