import mysql.connector as c
db= c.connect(host="localhost", database="bid", user="root", passwd="Development16")
mc=db.cursor()
try:
    mc.execute("create table user(id int primary key AUTO_INCREMENT,name varchar(15),password varchar(255))")
    db.commit()
except:
    print("table already created")

def checkIfUserExists(username):
    mc.execute("SELECT * FROM user WHERE name = \"{}\"".format(username))
    query = mc.fetchall()
    print(query)
    if(len(query)==0):
        return False
    return True

def CreateUser(name, password):
    mc.execute("SELECT * FROM user")
    query = mc.fetchall()
    mc.execute("INSERT INTO user values({},\"{}\",\"{}\")".format(len(query)+1,name,password))

def login(name,password):
    if(checkIfUserExists(name)):
        mc.execute("select password from user where name = \"{}\"".format(name))
        query = mc.fetchall()[0][0]
        if(query== password):
            return True
        return False

print(login("chandan","amaatra"))
