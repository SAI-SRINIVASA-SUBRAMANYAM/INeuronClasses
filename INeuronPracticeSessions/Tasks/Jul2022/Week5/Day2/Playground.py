# In this file we will understand the following:
# 1. Design pattern of the application
# 2. Flow of calls to understand, creation of database and tables in mysql & mongodb
# ================================================================
# Config.py: Basic application related configurations like database name, table name, file names.
#             Connection strings for mongodb and mysql server
# Logger.py: Handling log mechanism
# MySQLUtil.py: Connecting to mysql server and creating a database
# LoadFitBitData.py: Reading CSV data, creating table at MySQL server & MongoDB and loading data.
# LoadSuperstoreUSAData.py: Reading excel sheets data, creating table at MySQL server and loading data.
# ================================================================
from LoadFitbitData import FitbitDataLoader
from LoadSuperstoreUSAData import SuperstoreUSADataLoader


d = FitbitDataLoader()
d.read_data_into_mysql()
d.read_data_into_mongodb()
s = SuperstoreUSADataLoader()
s.insert_excel_sheets_into_mysql_tables()
