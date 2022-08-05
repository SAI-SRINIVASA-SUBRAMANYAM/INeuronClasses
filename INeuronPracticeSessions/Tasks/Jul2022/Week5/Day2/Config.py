import subprocess
from Logger import Logger, LogType


class AppConfig:
    __FitbitData_Filename = r'FitBitData.csv'
    __SuperstoreUSA_Filename = r'Superstore_USA.xlsx'
    database_name = 'machine_learning'
    table_name_fitbit = 'fitbitdata'
    table_name_superstoreusa = 'superstoreusa'

    def get_fitbit_filename(self):
        return self.__FitbitData_Filename

    def get_superstore_usa_filename(self):
        return self.__SuperstoreUSA_Filename

    def generate_table_statement(self):
        create_table_statement_bstr = subprocess.check_output(f'csvsql --dialect mysql --snifflimit 100000 {self.__FitbitData_Filename}')
        create_table_statement = create_table_statement_bstr.decode('utf-8')
        create_table_statement = create_table_statement.replace('CREATE TABLE', 'CREATE TABLE IF NOT EXISTS')
        Logger(f"Successfully created MySQL CREATE TABLE... statement from file {self.__FitbitData_Filename}.", LogType.Info)
        return create_table_statement

    def get_mysql_connection_details(self):
        mysql = {
            'host': "localhost",
            'user': "root",
            'passwd': "root"
        }
        return mysql

    def get_mongodb_connection_url(self):
        __user_name = '<<your_user_name>>'
        __password = '<<your_password>>'
        __cluster_name = '<<your_cluster>>'
        url = f'mongodb+srv://{__user_name}:{__password}@{__cluster_name}.34cpv.mongodb.net/?retryWrites=true&w=majority'
        return url

    def get_mysql_connection_string(self):
        mysql_conn_string = "mysql+mysqlconnector://{user}:{passwd}@localhost/{db}" \
            .format(user=self.get_mysql_connection_details().get('user'),
                    passwd=self.get_mysql_connection_details().get('passwd'),
                    db=self.database_name
                    )
        return mysql_conn_string