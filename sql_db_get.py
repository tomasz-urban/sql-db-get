import configuration as c
import schedule
import time


def config():
    df_1 = c.db1_configuration()
    df_2 = c.db2_configuration()
    df_3 = c.merge_data(df_1, df_2)
    output_df = c.result_query(df_3)
    c.save_file(output_df)


def scheduler():
    schedule.every().day.at("10:00").do(config)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    scheduler()
