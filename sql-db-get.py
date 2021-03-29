# Import libraries
import psycopg2
import pandas as pd

# Input the necessary information about SQL database connection as follows:
# db_name - database name
# db_user - database username
# db_password - database password
# db_host - server IP address
# db_port - connection port (default is 5432)
db_name = ""
db_user = ""
db_password = ""
db_host = ""
db_port = ""

conn = psycopg2.connect(database=db_name, user=db_user, password=db_password, host=db_host, port=db_port)

# Add SQL statement in brackets
sql = """

       """

# The following code reads the SQL statement using connection which were set before
# and writes the data to CSV file.
file_1 = pd.read_sql_query(sql, conn)
conn = None

# Add the path to the destination folder.
file_1.to_csv(r"file_1.csv")