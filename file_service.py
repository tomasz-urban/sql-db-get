from datetime import datetime
import configuration as conf


def save_file(output_df):
    date = datetime.now().strftime("%Y-%m-%d_%I-%M-%S_%p")
    file_path = conf.file_path
    saved_file = output_df.to_csv(f'{file_path}{date}.csv')
    return saved_file
