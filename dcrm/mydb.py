import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Abcd1234',  
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE probeq")

print("All Done!")