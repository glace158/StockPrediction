from urllib import parse
from ast import literal_eval
import requests
import pandas as pd

class FinanceManager:
    def __init__(self):
        pass

    def get_sise_3years(self, code):
        import datetime
        end_time = datetime.date.today()
        start_time = end_time - datetime.timedelta(days=365 * 3)
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
        return data_dict_list

    def list_to_df(self, data):
        df = pd.DataFrame(data)
        df = df.rename(columns={'날짜': 'Date', '시가': 'Open', '고가': 'High', '저가': 'Low', '종가': 'Close'})
        return df

    def save_to_csv(self, df, filename):
        df.to_csv(filename, index=False)

    def load_from_csv(self, filename):
        df = pd.read_csv(filename)
        return df

if __name__ == "__main__":
    fm = FinanceManager()
    data = fm.get_sise_3years('005930')
    df = fm.list_to_df(data)
    
    # CSV 파일로 저장
    fm.save_to_csv(df, 'stock_data.csv')
    
    # CSV 파일 불러오기
    loaded_df = fm.load_from_csv('stock_data.csv')
    print(loaded_df)