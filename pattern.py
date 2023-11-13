import numpy as np
from regression import Regression

class FlagPattern():
  def __init__(self):
    self._high_regression = Regression()
    self._low_regression = Regression()
    self._regression = Regression()
    self._high_datas = []
    self._low_datas = []
    self._compare_minimum = 3
    self._same_rate = 0.9

  def set_minimum(self, num):
    self._compare_minimum = num

  def set_same_rate(self, rate):
    self._same_rate = rate

  def pattern_match(self, high_data, low_data):
    print("=====================================")
    print("highs :", self._high_datas)
    print("lows :", self._low_datas)
    print("------------------high----------------------")
    is_high_match, high_rate =  self._regression_match(self._high_datas, high_data, True)
    print("-------------------low----------------------")
    is_low_match, low_rate =  self._regression_match(self._low_datas, low_data, False)

    is_match = is_high_match or is_low_match

    rate = -1.0
    if is_low_match:
      rate = low_rate
    else:
      rate = high_rate

    return is_match, rate

  def _regression_match(self, x_datas, cur_data, is_positive):
    if self._compare_minimum <= len(x_datas):
      np_x_datas = np.array(x_datas)
      np_x_datas = np_x_datas * 0.0001
      print(np_x_datas)
      data = cur_data * 0.0001

      self._regression.init_parameter()
      self._regression.update_parameter(np_x_datas, np.arange(len(x_datas)))
      predict_data = self._regression.predict(len(x_datas))
      rate = self._rate_calculation(predict_data, data)
      print("predict:", predict_data, "| data:", data, "| rate:", rate)
      print("----------------------------------------")


      if self._same_rate < abs(rate) and rate > 0 if is_positive else rate < 0:
        x_datas.clear()
        x_datas.append(cur_data)
        return True, rate
      else:
        x_datas.append(cur_data)
        return False, rate
    else:
      x_datas.append(cur_data)
      return False, 0.0

  def _rate_calculation(self, pre_data:float, cur_data:float):
    rate = (cur_data - pre_data) / pre_data * 100
    return rate