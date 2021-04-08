# sql-db-get
Getting data from two databases on different servers using Python and SQL statements


The aim of this project is to get the data from two databases located on two different servers. An output is a CSV file with the information that joins the data from those databases. That information will be gathered periodically using time schedule. Files will be stored in the format of: YYYY-MM-DD_HH-MM-SS_(AM or PM).csv

INSTRUCTIONS:

1. Update the `configuration.py` with the information about databases:

    * db_name - name of the database
    * db_user - database username (used for authentication)
    * db_password = database password used to authenticate
    * db_host - database host address (defaults to UNIX socket if not provided)
    * db_port - connection port number (defaults to 5432 if not provided)

    * output_query - to get the needed information from merged DataFrame

    * db_sql_query - sql query for each database

    * file_path - the destination folder

2. Run `sql_db_get.py` file to execute script