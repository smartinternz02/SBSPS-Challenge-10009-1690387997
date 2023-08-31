def showall():
    sql="SELECT * from EV_STATION table"
    stmt= ibm_db.exec_immediate(conn,sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary !=False:
        print("The name is :" , dictionary["NAME"])
        print("The Email is :" , dictionary["EMAIL"])
        print("The password is :" , dictionary["PASSWORD"])
        dictionary = ibm_db.fetch_both(stmt)
        
def getdetails(email,password):
    sql = "select * from  EV_STATION where email='{}' and password ='{}'".format(email,password)
    stmt = ibm_db.exec_immediate(conn,sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary !=False:
       print("The name is :" , dictionary["NAME"])
       print("The Email is :" , dictionary["EMAIL"])
       print("The password is :" , dictionary["PASSWORD"])
       dictionary = ibm_db.fetch_both(stmt)
       
def insertdb(conn,name,email,password):
    sql= "INSERT into EV_STATION VALUES('{}','{}','{}')".format(name,email,password) 
    stmt = ibm_db.exec_immediate(conn,sql)
    print("Number of rows affected :",ibm_db.num_rows(stmt))
    
try:
    import ibm_db
    conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=b70af05b-76e4-4bca-a1f5-23dbb4c6a74e.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32716;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=krt20248;PWD=RmlGVZFSSuUlQySV",'','')
    print(conn)
    print("Connection Successful..")
    insertdb(conn, "Hari", "hari@gmail.com", "Hari123") 
    getdetails("Hari@gmail.com","Hari123")
    
    
except:
    print("Error connecting to the database")        
           