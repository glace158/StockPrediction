import matplotlib.pyplot as plt
class ResultPrinter(FinanceManager):
    def __init__(self, wallet):
        super().__init__()
        self.wallet = wallet

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

    def printColumnGraph(self, column_data_x, column_data_y, x_label, y_label, title, figsize=(12, 8)):
        if not isinstance(column_data_x, str) and not isinstance(column_data_y, str):
            plt.figure(figsize=figsize)  # Set the size of the figure
            plt.plot(column_data_x, column_data_y)
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plt.title(title)
            plt.show()
        else:
            print("Error: Invalid column data.")

    def calculate_return_rate(self):
        initial_money = self.wallet.get_initial_money()
        current_money = self.wallet.get_money()

        if initial_money != 0:
            return_rate = ((current_money - initial_money) / initial_money) * 100
            return return_rate
        else:
            print("Initial money is 0. Cannot calculate return rate.")

if __name__ == "__main__":
  # Wallet 클래스를 직접 실행할 때의 코드
    my_wallet = Wallet()
    rp = ResultPrinter(my_wallet)
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
        rp.printColumnGraph(column_data_x, column_data_y, 'Date', 'Open Price', 'Stock Open Price Over Time')
    print(column_data_y)
    print(column_data_x)
    

    # 자산 확인
    my_wallet.add_money(50000)
    print("현재 자산:", my_wallet.get_money())
    print("초기 자산:", my_wallet.get_initial_money())

    # ResultPrinter 클래스를 사용하여 수익률 출력
    result_printer = ResultPrinter(my_wallet)
    return_rate = result_printer.calculate_return_rate()
    if return_rate is not None:
        print("수익률: {:.2f}%".format(return_rate))
