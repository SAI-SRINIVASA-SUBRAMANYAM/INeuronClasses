import sys
from Config import AppConfig
import mysql.connector as conn
from Logger import Logger, LogType


class MySQLUtil:
    def __init__(self):
        self._conf = AppConfig()
        self.__mysql_create_database()

    def __mysql_create_database(self):
        mydb = conn.connect(**self._conf.get_mysql_connection_details())
        db = self._conf.database_name
        try:
            cur = mydb.cursor()
            cur.execute(f'create database if not exists {db};')
            status = f'Successfully created, database: {db}'
            Logger(status, LogType.Info)
        except Exception as e:
            print(e)
            Logger(str(e), LogType.Error)
            sys.exit("Error while creating database please log for more details")
        finally:
            mydb.close()

    def mysql_create_table_fitbitdata(self):
        mydb = conn.connect(**self._conf.get_mysql_connection_details())
        try:
            cur = mydb.cursor()
            create_table_statement = self._conf.generate_table_statement()
            db = self._conf.database_name
            cur.execute(f'use {db};')
            cur.execute(f'{create_table_statement};')
            message = f'Successfully created, table: {self._conf.table_name_fitbit}'
            Logger(message, LogType.Info)
        except Exception as e:
            print(e)
            Logger(str(e), LogType.Error)
            sys.exit("Error while creating table please log for more details")
        finally:
            mydb.close()


