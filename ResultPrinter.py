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
     @staticmethod
    def market_watch(wallet, percent, decision):
        if decision is True:
            result = TradeManager.buy(wallet, percent)
            return result
        elif decision is False:
            result = TradeManager.sell(wallet, percent)
            return result
        elif decision is None:
            pass 
