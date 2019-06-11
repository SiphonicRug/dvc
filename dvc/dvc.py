import sys, getopt, getpass,mysql.connector

def create(serviceName):
    if serviceName.casefold() == "mysql":
        try:
            hostname = input("Insert the hostname (default 127.0.0.1):")
        except SyntaxError:
            hostname = '127.0.0.1'
        try:
            port = input("Insert the port (default 3306):")
        except SyntaxError:
            port = '3306'
        try:
            username = input("Insert the username (default 'root'):")
        except SyntaxError:
            port = 'root'
        try:
            passwd = getpass.getpass("Insert the password (defaulf none):")
        except Exception as error:
            passwd = ''
        dbname = input("Insert the db name")
        query = """SELECT table_name FROM INFORMATION_SCHEMA.tables WHERE table_schema=`%s`"""
        connection = mysql.connector.connect(host=hostname, database = dbname,user=username,password = passwd,port = port)
        cursor = connection.cursor(prepared=True)
        cursor.execute(query, (dbname))
        tables = cursor.fetchall()
args = sys.argv
if len(sys.argv) != 2:
    print("Invalid number of arguments")
args[0](arg[1])