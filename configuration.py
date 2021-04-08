import input_data as inp
import pandas as pd
import psycopg2
from datetime import datetime


def db1_configuration():
    conn = psycopg2.connect(database=inp.db1_name, user=inp.db1_user, password=inp.db1_password,
                            host=inp.db1_host, port=inp.db1_port)
    sql_query = pd.read_sql_query(inp.db1_sql_query, conn)
    df_1 = pd.DataFrame(sql_query)
    return df_1


def db2_configuration():
    conn = psycopg2.connect(database=inp.db2_name, user=inp.db2_user, password=inp.db2_password,
                            host=inp.db2_host, port=inp.db2_port)
    sql_query = pd.read_sql_query(inp.db2_sql_query, conn)
    df_2 = pd.DataFrame(sql_query)
    return df_2


def merge_data(df_1, df_2):
    merge_df = pd.merge(df_1[["emp_no", "title"]], df_2[["emp_no", "salary"]], on="emp_no")
    df_3 = pd.DataFrame(merge_df)
    return df_3


def result_query(df_3):
    output_data = df_3.query("emp_no == 10001" or "emp_no == 10002")
    return output_data


def save_file(output_df):
    date = datetime.now().strftime("%Y-%m-%d_%I-%M-%S_%p")
    file_path = inp.file_path
    saved_file = output_df.to_csv(f'{file_path}{date}.csv')
    return saved_file

