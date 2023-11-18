import pandas as pd
import matplotlib.pyplot as plt

class ResultPrinter:
    def __init__(self, date, decision, close):
        #메인에서 받아올 정보들 : 날짜, 매수매도bool, 종가
        self.date = date
        self.decisions = decision
        self.closes = close
        self.result = dict(zip(date, decision))

    def get_result(self):
        return self.result

    def save_to_csv(self, filename):
        df = pd.DataFrame(list(self.result.items()), columns=['Date', 'Decision'])
        df.to_csv(filename, index=False)
        print(f"Result saved to {filename}")

    def load_from_csv(self, filename):
        df = pd.read_csv(filename)
        self.result = dict(zip(df['Date'], df['Decision']))
        print(f"Result loaded from {filename}")

    def plot_graph(self):
        x_values = self.date
        y_values_close = self.close
        y_values_decision = [1 if value else 0 for value in self.decision]

        # True는 빨간색 네모, False는 파란색 네모
        colors = ['red' if value else 'blue' for value in self.decision]
        plt.plot(x_values, y_values_close, label='Close', color='black', marker='o', linestyle='-', linewidth=1)
        plt.scatter(x_values, y_values_close, c=colors, marker='s', label='Decision', s=100)
        for i, value in enumerate(self.decision):
            if value:
                plt.text(x_values[i], y_values_close[i], 'BUY', color='red', ha='center', va='bottom')
            else:
                plt.text(x_values[i], y_values_close[i], 'SELL', color='blue', ha='center', va='top')

        plt.xlabel('Date')
        plt.ylabel('Close')
        plt.title('Close and Decision Over Time')
        plt.legend()
        plt.show()
if __name__ == "__main__":
    # 예시 데이터
    date_list = ['2023-01-01', '2023-01-02', '2023-01-03']
    decision_list = [None, None, True]
    close_list = [100, 120, 90]

    # ResultPrinter 인스턴스 생성
    result_printer = ResultPrinter(date_list, decision_list, close_list)

    # 결과 출력
    print("Result:", result_printer.get_result())

    # CSV로 저장
    result_printer.save_to_csv('result.csv')

    # CSV 불러오기
    result_printer.load_from_csv('result.csv')

    # 그래프 그리기
    result_printer.plot_graph()