from pattern import FlagPattern
from FinanceManager import FinanceManager
from ResultPrinter import ResultPrinter
from stockDecide import Decide
from Wallet_walletManager import WalletManager

class MainFlow():
  def __init__(self) -> None:
    self.finance_manager = FinanceManager()
    self.flag_pattern = FlagPattern()
    self.decide = Decide()
    self.wallet_manager = WalletManager()
    #self.result_printer = ResultPrinter()

    self.data_init()
    self.data_dict = {}
        
  def data_init(self):
    df = self.finance_manager.get_sise_years('005930')
    df = self.finance_manager.list_to_df(df)
    self.finance_manager.save_to_csv(df, 'stock_data.csv')

    self.date_datas = self.finance_manager.get_datas("날짜")
    self.high_datas = self.finance_manager.get_datas("고가")
    self.low_datas = self.finance_manager.get_datas("저가")
    self.close_datas = self.finance_manager.get_datas("종가")
    
  def run(self):
    
    for i in range(len(self.date_datas)):
      print("===================================================")
      print(self.date_datas[i])
      is_match, _ = self.flag_pattern.pattern_match(self.high_datas[i], self.low_datas[i])
      money_percent, is_buy = self.decide.get_decide(self.close_datas[i], is_match)
      print(money_percent, is_buy)
      print()
      self.record(i, is_buy)

  def record(self, i, is_buy):
    if is_buy != None:
      self.data_dict[self.date_datas[i]] = is_buy
      
    for k, v in self.data_dict.items():
      print(k, ":", v)
      
if __name__ == "__main__":
  main_flow = MainFlow()
  main_flow.run()