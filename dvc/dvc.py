import sys, os, getopt, getpass,mysql.connector

def getvalue(message,default):
    try:
        result = input(message)
    except SyntaxError:
        result = default
    return default

def create(serviceName):
    if serviceName.casefold() == "mysql":
        hostname = getvalue("Insert the hostname (default 127.0.0.1):","127.0.0.1")
        port = getvalue("Insert the port (default 3306):","3306")
        username = input("Insert the username (default 'root'):","root")
        try:
            passwd = getpass.getpass("Insert the password (defaulf none):")
        except Exception as error:
            passwd = ''
        try:
            dbname = input("Insert the db name")
        except Exception as error:
            print("Database name not valid: "+error.with_traceback)
            return

        query = """SELECT table_name FROM INFORMATION_SCHEMA.tables WHERE table_schema=`%s`"""
        connection = mysql.connector.connect(host=hostname, database = dbname,user=username,password = passwd,port = port)
        cursor = connection.cursor(prepared=True)
        cursor.execute(query, (dbname))
        tables = cursor.fetchall()
args = sys.argv
if len(sys.argv) != 2:
    print("Invalid number of arguments")
args[0](arg[1])