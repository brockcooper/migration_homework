import psycopg2

# Purpose of class is to take a sql file path and postgres connection information
# and execute the sql file. This is a Class incase there needs to be any expansion
# of this simple use case. Many of these functions could be used if we were to expand
# this class to include other basic transform steps that occur frequently
class RunPostgreSQL():
    def __init__(self, host, dbname, user, password ):
        self.connection = self.make_connection(host, dbname, user, password)
        self.cursor = self.connection.cursor()

    def make_connection(self, host, dbname, user, password):
        conn_string = self.create_connection_string(host, dbname, user, password)
        return psycopg2.connect(conn_string)

    # Requires Python 3.6 if using f-strings
    def create_connection_string(self, host, dbname, user, password):
        return f"host='{host}' dbname='{dbname}' user='{user}' password='{password}'"

    def run_sql_file(self, sql_file):
        self.sql_file = sql_file
        sql_text = self.get_sql_file_text()
        return self.cursor.execute(sql_text)

    def get_sql_file_text(self):
        file = open(self.sql_file, 'r')
        return file.read()


# Set up variables for the RunPostgreSQL class here:
sql_file = 'migration_homework.sql'
host = '192.54.86.246' # This is a fake ip address
dbname = 'account_balances'
user = 'postgres_user'
password = 'password123'

# Trigger object creation and running run_sql_file function:
postgres = RunPostgreSQL(host, dbname, user, password)
postgres.run_sql_file(sql_file)
