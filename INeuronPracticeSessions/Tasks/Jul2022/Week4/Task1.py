from conf import DBConf
import mysql.connector as con


def get_all_databases(cursor):
    cursor.execute("show databases")
    databases = cursor.fetchall()
    print(databases)
    return databases

try:
    mydb = con.connect(host=DBConf.MySQL['host'], user=DBConf.MySQL['user'], passwd=DBConf.MySQL['passwd'])
    cursor = mydb.cursor()
    databases = get_all_databases(cursor)

    for db in databases:
        if DBConf.MySQL['clothing_db'] in db:
            break
    else:
        cursor.execute(f"create database {DBConf.MySQL['clothing_db']}")

    get_all_databases(cursor)

except Exception as e:
    print('Exception:',e)


