import pandas as pd
from sqlalchemy import create_engine
from Config import AppConfig
from MySQLUtil import MySQLUtil
from Logger import Logger, LogType
import pymongo
import json


# Task 1.
# 1. Read this dataset in pandas, mysql and mongodb
# 2. while creating a table in mysql don't use manual approach to create it  ,always use a automation to create a table in mysql
#  > `Hint`: `Use csvkit library to automate this task and to load a data in bulk in you mysql`
# 3. convert all the dates available in dataset to timestamp format in pandas and in sql you to convert it in date format

class FitbitDataLoader(MySQLUtil):
    def __init__(self):
        super().__init__()
        self._conf = AppConfig()
        self.df_csv = pd.read_csv(self._conf.get_fitbit_filename())
        self.df_csv['ActivityDate'] = pd.to_datetime(self.df_csv['ActivityDate'], format="%m/%d/%Y")

    def read_data_into_mysql(self):
        self.mysql_create_table_fitbitdata()
        try:
            mysql_conn_string = self._conf.get_mysql_connection_string()
            engine = create_engine(mysql_conn_string).connect()
            table_name = self._conf.table_name_fitbit
            self.df_csv.to_sql(name=table_name, con=engine, if_exists='replace')
            Logger(f"Successfully loaded data into MySQL table: {table_name}.", LogType.Info)
        except Exception as e:
            print(e)

    def read_data_into_mongodb(self):
        try:
            mongodb_url = self._conf.get_mongodb_connection_url()
            client = pymongo.MongoClient(mongodb_url)
            database = client[self._conf.database_name]
            collection = database[self._conf.table_name_fitbit]
            collection.drop()
            data_json = json.loads(self.df_csv.to_json(orient='records'))
            collection.insert_many(data_json)
            Logger(f'Data inserted successfully into MongoDB, database: {database}, collection name: {collection}')
        except Exception as e:
            print(e)
