
from App import app

import mysql.connector

class Login:
    #Ctor for Login
    def __init__(self, username, password, connection):
        self.username = username
        self.password = password
        self.connection = connection
        print(self.username)


    #function to execute an SQL Query
    #Returns the Query result
    def executeQuery(self,query):
#         connection = mysql.connector.connect(host = "localhost", database = 'newdb', user = "root",passwd = "replace with your own password") #make sure to change password to correct one

        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        # cursor.commit()
        return result


    #Cross checks if a username and password correspond with eachother
    #return boolean result
    def authenticate(self):
        userQuery = "SELECT Password FROM account WHERE Email_Address = '" + self.username + "';"
        result = self.executeQuery(userQuery)
        convert = str(result)
        convert = convert[3:len(convert) - 4] #remove useless characters from front and end
        if(self.password == convert):
            return 1 #password matches with the one in table
        elif (self.user_exist() == False):
            return 0 #username does not exist
        else:
            return -1 #password does not match


    # Check if username and password combination exists
    def validate(self):
        query="SELECT * FROM Account WHERE Email='" + self.username + "' AND Password='" + self.password + "'"
        result=self.executeQuery(query)

        return result


    def isAdmin(self):
        userQuery = "SELECT admin FROM account WHERE Email_Address = '" + self.username + "';"
        result = self.executeQuery(userQuery)
        convert = str(result)
        convert = convert[2:len(convert) - 3]
        print(convert)
        return convert

    #For debugging. Prints all users in the user Table
    def printUsers(self):
        userQuery = "SELECT Email, Password FROM Account;"
        table_result = self.executeQuery(userQuery)
        for x in table_result:
            print(x)


    #check if user is already in the database table
    def user_exist(self):
        userQuery = "SELECT 1 FROM Account WHERE Email_Address = '"+ self.username +"';"
        result = self.executeQuery(userQuery)
        if(len(result) == 0):
            return False
        else:
            return True


    #Adds user to the table, given a username and password
    #Returns false if request was not possible (usename already exists)
    def add_login(self, name, lastname, age, birthday, gender, accountType):
        if(self.user_exist() == False):
            userQuery = "INSERT INTO Account (First_Name, Last_Name, BirthDate, Gender, Password, Age, Email_Address, admin) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            if(accountType == "Administrator"):
                accountType = True
            else:
                accountType = False
            val = (name, lastname, birthday, gender, self.password, 10, self.username, accountType)
            # userQuery = "INSERT INTO Account VALUES ('" + name + "','" + lastname + "','" + birthday+ "','" +  gender + "','" + self.password+  "','" +  age + "','" + self.username+ "');"
            cursor = self.connection.cursor()
            cursor.execute(userQuery, val)
            # self.executeQuery(userQuery)
            print("added new user") #for debugging
            self.connection.commit()
            return True
        else:
            print("this username already exists") #for debugging
            return False


    #Sets the password. Can be used if a user wants to change their password
    def set_password(self,password):
        userQuery = "UPDATE Account SET Password = '"+password + "' WHERE Email_Address = '"+self.username +"';"
        self.executeQuery(userQuery)

   
