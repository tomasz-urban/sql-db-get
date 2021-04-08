import psycopg2
import pandas as pd
from datetime import datetime
import input_data as inp


def db1_configuration():
    conn = psycopg2.connect(database=inp.db1_name, user=inp.db1_user, password=inp.db1_password,
                            host=inp.db1_host, port=inp.db1_port)
    sql_query = pd.read_sql_query(inp.db1_sql_query, conn)
    df = pd.DataFrame(sql_query, columns=["emp_no", "title"])
    return df


def db2_configuration():
    conn = psycopg2.connect(database=inp.db2_name, user=inp.db2_user, password=inp.db2_password,
                            host=inp.db2_host, port=inp.db2_port)
    sql_query = pd.read_sql_query(inp.db2_sql_query, conn)
    df = pd.DataFrame(sql_query, columns=["emp_no", "salary"])
    return df


def merge_data():
    merge_df = pd.merge(df_1[["emp_no", "title"]], df_2[["emp_no", "salary"]], on="emp_no")
    df_merge = pd.DataFrame(merge_df)
    return df_merge


def result_query():
    output_data = df_3.query("emp_no == 10001")
    return output_data


def save_file():
    date = datetime.now().strftime("%Y-%m-%d_%I-%M-%S_%p")
    file_path = inp.file_path
    saved_file = output_df.to_csv(f'{file_path}{date}.csv')
    return saved_file


df_1 = db1_configuration()
df_2 = db2_configuration()
df_3 = merge_data()
output_df = result_query()
save_file()