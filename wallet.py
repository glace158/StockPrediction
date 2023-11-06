

class Wallet:
    def __init__(self):
        self.balance = 0

    def set_money(self, money):
        if money >= 0:
            self.balance = money
        else:
            print("자산은 음수가 될 수 없습니다.")

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

if __name__ == "__main__":
    # Wallet 클래스를 직접 실행할 때의 코드
    my_wallet = Wallet()

    # 자산 설정
    my_wallet.set_money(1000)

    # 자산 확인
    print("현재 자산:", my_wallet.get_money())

    # 입금
    my_wallet.add_money(500)

    # 자산 확인
    print("현재 자산:", my_wallet.get_money())

    # 지출
    my_wallet.spend_money(300)

    # 자산 확인
    print("현재 자산:", my_wallet.get_money())
