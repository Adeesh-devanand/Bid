import mysql.connector as c

class  Database:
    def __init__(self):

        self.db= db= c.connect(host="localhost", user="root", passwd="Development16")
        self.mc= mc=db.cursor()
        
        self.mc.execute("create database if not exists bid")
        self.mc.execute("use bid")

        try:
            self.mc.execute("create table user(id int primary key AUTO_INCREMENT,name varchar(15),password varchar(255))")
            self.db.commit()
        except:
            print("table already created")

    def checkIfUserExists(self, username):
        self.mc.execute("SELECT * FROM user WHERE name = \"{}\"".format(username))
        query = self.mc.fetchall()
        if(len(query)==0):
            return False
        return True

    def CreateUser(self,username, password):
        if(self.checkIfUserExists(username)):
            print('user already exists')
        else:
            self.mc.execute("SELECT * FROM user")
            query = self.mc.fetchall()
            self.mc.execute("INSERT INTO user values({},\"{}\",\"{}\")".format(len(query)+1,username,password))
            self.db.commit()
    def login(self, username, password):
        if(self.checkIfUserExists(username)):
            self.mc.execute("SELECT * FROM user")
            query = self.mc.fetchall()
            self.mc.execute("select password from user where name = \"{}\"".format(username))
            query = self.mc.fetchall()[0][0]
            if(query== password):
                return True
            return False