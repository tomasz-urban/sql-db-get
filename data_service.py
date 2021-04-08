import configuration as conf
import pandas as pd
import psycopg2


def db1_query():
    conn = psycopg2.connect(database=conf.db1_name, user=conf.db1_user, password=conf.db1_password,
                            host=conf.db1_host, port=conf.db1_port)
    sql_query = pd.read_sql_query(conf.db1_sql_query, conn)
    df_1 = pd.DataFrame(sql_query)
    return df_1


def db2_query():
    conn = psycopg2.connect(database=conf.db2_name, user=conf.db2_user, password=conf.db2_password,
                            host=conf.db2_host, port=conf.db2_port)
    sql_query = pd.read_sql_query(conf.db2_sql_query, conn)
    df_2 = pd.DataFrame(sql_query)
    return df_2


def merge_data(df_1, df_2):
    merge_df = pd.merge(df_1, df_2)
    df_3 = pd.DataFrame(merge_df)
    return df_3


def result_query(df_3):
    output_data = df_3.query(conf.output_query)
    return output_data
