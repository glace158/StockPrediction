class Wallet:
    def __init__(self):
        self.balance = 10000000
        self.initial_balance = 10000000

    def get_initial_money(self):
        return self.initial_balance

    def get_money(self):
        return self.balance

    def add_money(self, money):
        if money >= 0:
            self.balance += money
        else:
            print("입금 금액은 음수가 될 수 없습니다.")

    def spend_money(self, money):
        if money >= 0:
            if self.balance >= money:
                self.balance -= money
            else:
                print("잔액이 부족합니다.")
        else:
            print("지출 금액은 음수가 될 수 없습니다.")

class TradeManager:
     def buy(self, percent):
        buy_amount = int(self.money * percent / 100)
        print(f"Wallet buy: {buy_amount} won")
        return buy_amount
     def sell(self, percent):
        sell_amount = int(self.money * percent / 100)
        print(f"Wallet sell: {sell_amount} won")
        return sell_amount
     def calculate_dividend_yield(annual_dividend, current_price):
     try:
        dividend_yield = (annual_dividend / current_price) * 100
        return dividend_yield
     except ZeroDivisionError:
        print("Error: 현재 주가는 0이 될 수 없습니다.")
        return None


