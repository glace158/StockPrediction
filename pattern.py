import numpy as np
from regression import Regression

class FlagPattern():
  def __init__(self):
    self._regression = Regression()
    self._high_datas = []
    self._low_datas = []
    self._compare_minimum = 3
    self._same_rate = 2.0
    

  def set_minimum(self, num):
    self._compare_minimum = num

  def set_same_rate(self, rate):
    self._same_rate = rate

  def pattern_match(self, high_data, low_data):
    print("highs :", self._high_datas)
    print("lows :", self._low_datas)
    print()
    print("------------------high----------------------")
    print()
    is_high_match, high_rate =  self._regression_match(self._high_datas, high_data, True)
    print("-------------------low----------------------")
    print()
    is_low_match, low_rate =  self._regression_match(self._low_datas, low_data, False)

    is_match = is_high_match or is_low_match

    rate = -1.0
    if is_low_match:
      rate = low_rate
    else:
      rate = high_rate

    return is_match, rate

  def _regression_match(self, y_datas, cur_data, is_positive):
    if self._compare_minimum <= len(y_datas):


      self._regression.init_parameter()
      self._regression.update_parameter(np.arange(len(y_datas)),y_datas)
      predict_data = self._regression.predict(len(y_datas))
      rate = self._error_rate_calculation(predict_data, cur_data)
      print()
      print("predict:", predict_data.numpy()[0], "| data:", cur_data, "| rate:", rate.numpy()[0])
      print()

      if self._same_rate < abs(rate) and rate > 0 if is_positive else rate < 0:
        y_datas.clear()
        y_datas.append(cur_data)
        return True, rate.numpy()[0]
      else:
        y_datas.clear()
        y_datas.append(cur_data)
        return False, rate.numpy()[0]
    else:
      y_datas.append(cur_data)
      return None, -1.0

  def _error_rate_calculation(self, pre_data:float, cur_data:float):
    rate = (cur_data - pre_data) / pre_data * 100
    return rate