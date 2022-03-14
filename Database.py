def checkIfUserExists(username, mc):
    mc.execute("SELECT * FROM user WHERE name = \"{}\"".format(username))
    query = mc.fetchall()
    print(query)
    if(len(query)==0):
        return False
    return True

def CreateUser(name, password, mc):
    mc.execute("SELECT * FROM user")
    query = mc.fetchall()
    mc.execute("INSERT INTO user values({},\"{}\",\"{}\")".format(len(query)+1,name,password))

def login(name,password, mc):
    if(checkIfUserExists(name, mc)):
        mc.execute("select password from user where name = \"{}\"".format(name))
        query = mc.fetchall()[0][0]
        if(query== password):
            return True
        return False