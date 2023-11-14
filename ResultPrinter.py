import matplotlib.pyplot as plt

class ResultPrinter(FinanceManager):
    def __init__(self):
        super().__init__()

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

    def printColumnGraph(self, column_data_x, column_data_y, x_label, y_label, title):
        if not isinstance(column_data_x, str) and not isinstance(column_data_y, str):
            plt.plot(column_data_x, column_data_y)
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plt.title(title)
            plt.show()
        else:
            print("Error: Invalid column data.")

if __name__ == "__main__":
    rp = ResultPrinter()
    rp.get_sise_days('005930')

    # CSV 파일로 저장
    rp.save_to_csv('stock_data.csv')

    # CSV 파일 불러오기
    rp.load_from_csv('stock_data.csv')

    # 열 데이터 가져오기
    column_data_y = rp.get_column_data('종가')  
    column_data_x = rp.get_column_data('날짜')  
    column_data_x = column_data_x.astype(str).str[-4:]
    # 출력
    if not isinstance(column_data_y, str) and not isinstance(column_data_x, str):
        result_printer = ResultPrinter()
        result_printer.printColumnGraph(column_data_x, column_data_y, 'Date', 'Open Price', 'Stock Open Price Over Time')
    print(column_data_y)
    print(column_data_x)
