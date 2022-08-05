import pandas as pd
from sqlalchemy import create_engine
from Config import AppConfig
from Logger import Logger, LogType
from MySQLUtil import MySQLUtil

# Task 2 - Superstore_USA
# 1. load this data in sql and in pandas with a relation in sql
# 2. while loading this data you don't have to create a table manually you can use any automated approach to create a table and load a data in bulk in table


class SuperstoreUSADataLoader(MySQLUtil):
    sheet_orders = 'Orders'
    sheet_returns = 'Returns'
    sheet_users = 'Users'

    def __init__(self):
        super().__init__()
        self._conf = AppConfig()
        wb = pd.ExcelFile(self._conf.get_superstore_usa_filename())
        self.df_orders_details = pd.read_excel(wb, sheet_name=self.sheet_orders)
        self.df_orders_summary = self.df_orders_details.groupby('Order ID').sum(['Discount', 'Shipping Cost', 'Profit', 'Quantity ordered new', 'Sales']).rename(columns={'Discount':'Total Discount','Shipping Cost':'Total Shipping Cost','Profit':'Total Profit','Quantity ordered new':'Total Qty Ordered','Sales':'Total Sales'})
        self.df_returns = pd.read_excel(wb, sheet_name=self.sheet_returns)
        self.df_users = pd.read_excel(wb, sheet_name=self.sheet_users)
        Logger("Data frames order, returns, users loaded successfully", LogType.Info)

    def insert_excel_sheets_into_mysql_tables(self):
        try:
            table_name = self._conf.table_name_superstoreusa
            mysql_conn_string = self._conf.get_mysql_connection_string()

            engine = create_engine(mysql_conn_string).connect()
            self.df_orders_summary.to_sql(table_name+"_"+self.sheet_orders.lower()+"_summary", con=engine, if_exists='replace')
            self.df_orders_details.to_sql(table_name+"_"+self.sheet_orders.lower()+"_details", con=engine, if_exists='replace')
            self.df_returns.to_sql(table_name + "_" + self.sheet_returns.lower(), con=engine, if_exists='replace')
            self.df_users.to_sql(table_name + "_" + self.sheet_users.lower(), con=engine, if_exists='replace')
            Logger("Successfully loaded data frames into mysql server", LogType.Info)
            engine.close()
        except Exception as e:
            print(e)
            Logger('Operation connect and insert to database is failed', LogType.Error)

