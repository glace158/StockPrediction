from urllib import parse
from ast import literal_eval
import requests
import pandas as pd

class FinanceManager:
    def __init__(self):
        self.data = None

    def get_sise_years(self, code,num_years=3):
        import datetime
        end_time = datetime.date.today()
        start_time = end_time - datetime.timedelta(days=365 * num_years)
        start_time_str = start_time.strftime('%Y%m%d')
        end_time_str = end_time.strftime('%Y%m%d')

        get_param = {
            'symbol': code,
            'requestType': 1,
            'startTime': start_time_str,
            'endTime': end_time_str,
            'timeframe': 'day'
        }
        get_param = parse.urlencode(get_param)
        url = "https://api.finance.naver.com/siseJson.naver?%s" % get_param
        response = requests.get(url)
        data_list = literal_eval(response.text.strip())

        data_dict_list = []
        for data in data_list:
            data_dict = {
                '날짜': data[0],
                '시가': data[1],
                '고가': data[2],
                '저가': data[3],
                '종가': data[4],
            }
            data_dict_list.append(data_dict)
        self.data = pd.DataFrame(data_dict_list)

    def get_sise_days(self, code, days=30):
        import datetime
        end_time = datetime.date.today()
        start_time = end_time - datetime.timedelta(days)
        start_time_str = start_time.strftime('%Y%m%d')
        end_time_str = end_time.strftime('%Y%m%d')

        get_param = {
            'symbol': code,
            'requestType': 1,
            'startTime': start_time_str,
            'endTime': end_time_str,
            'timeframe': 'day'
        }
        get_param = parse.urlencode(get_param)
        url = "https://api.finance.naver.com/siseJson.naver?%s" % get_param
        response = requests.get(url)
        data_list = literal_eval(response.text.strip())

        data_dict_list = []
        for data in data_list:
            data_dict = {
                '날짜': data[0],
                '시가': data[1],
                '고가': data[2],
                '저가': data[3],
                '종가': data[4],
            }
            data_dict_list.append(data_dict)
        self.data = pd.DataFrame(data_dict_list)


    def list_to_df(self, data):
        df = pd.DataFrame(data)
        df = df.rename(columns={'날짜': 'Date', '시가': 'Open', '고가': 'High', '저가': 'Low', '종가': 'Close'})
        self.data = df

    def save_to_csv(self, filename):
        self.data.to_csv(filename, index=False)

    def load_from_csv(self, filename):
        self.data = pd.read_csv(filename)

    def get_column_data(self, column_name):
        if self.data is not None:
            if column_name in self.data.columns:
                return self.data[column_name]
            else:
                return f"Column '{column_name}' not found in the DataFrame."
        else:
            return "DataFrame is empty. Please load or create data first."

    def get_row_by_date(self, date):
        if self.data is not None:
            date_row = self.data[self.data['날짜'] == date]
            if not date_row.empty:
                return date_row
            else:
                return f"No data for the date '{date}'."
        else:
            return "DataFrame is empty. Please load or create data first."

if __name__ == "__main__":
    fm = FinanceManager()
    fm.get_sise_years('005930',1)

    # CSV 파일로 저장
    fm.save_to_csv('stock_data.csv')

    # CSV 파일 불러오기
    fm.load_from_csv('stock_data.csv')

    # 열 데이터 가져오기
    column_data_y = fm.get_column_data('시가')  # Example: Get '시가' column
    column_data_x = fm.get_column_data('날짜')  # Example: Get '시가' column


    # 행 데이터 가져오기
    date_row = fm.get_row_by_date('20230105')  # Example: Get data for the date '20230105'

    # 출력

    print(column_data_y)
    print(column_data_x)

    if not isinstance(date_row, str):
        print(date_row)
