import schedule
import time
import data_service as ds
import file_service as fs


def query_setup():
    df_1 = ds.db1_query()
    df_2 = ds.db2_query()
    df_3 = ds.merge_data(df_1, df_2)
    output_df = ds.result_query(df_3)
    fs.save_file(output_df)


def scheduler():
    schedule.every().day.at("10:00").do(query_setup)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    scheduler()
