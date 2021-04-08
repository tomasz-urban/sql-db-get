# First database info:

db1_name = "db1 name"  # the database name
db1_user = "db1 user"  # the database username
db1_password = "password"  # the database password
db1_host = "host"  # the database host
db1_port = "port"  # the default value is 5432

# Sample query
db1_sql_query = """
         SELECT emp_no, title FROM titles
                WHERE emp_no BETWEEN 10001 AND 10004  
      """


# Second database info:

db2_name = "db2 name"  # the database name
db2_user = "db2 user"  # the database username
db2_password = "password"  # the database password
db2_host = "host"  # the database host
db2_port = "port"  # the default value is 5432

# Sample query
db2_sql_query = """
         SELECT emp_no, salary FROM salaries
                WHERE emp_no BETWEEN 10001 AND 10004
      """

# Output query - to get the needed information from merged DataFrame (sample query)

output_query = "emp_no == 10001"

# Destination folder info:

file_path = ""



