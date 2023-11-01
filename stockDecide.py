#import tensorflow as tf

class RateDecide():# 상승, 하강률에 따른 매수, 매도 전략
    def __init__(self) -> None:
        #rate , moneny_percent, is_buy
        self._rate_strategies = [
            (-3.0, 100.0, False),
            (-2.0, 30.0, False),
            (-1.0, 10.0, False),
            (0.0, 0.0, None),
            (1.0, 10.0, True),
            (2.0, 30.0, True),
            (3.0, 100.0, True)
        ]

    def rate_decide(self, pre_data:float, cur_data:float):
        rate = self._rate_culc(pre_data, cur_data)
        return self._compare_rate_strategy(rate)

    def _compare_rate_strategy(self, rate:float):
        for rate_strategy in self._rate_strategies:
            if rate_strategy[0] >= rate:
                return rate_strategy[1:]
            
        return self._rate_strategies[-1, 1:]

    def _rate_calculation(self, pre_data:float, cur_data:float):
        rate = (cur_data - pre_data) / pre_data * 100
        return rate

class PatternDecide():# 패턴 매치에 따른 매수,매도 전략
    def pattern_calculation(self, *is_match):
        match_rate = is_match.count(True) / len(is_match) * 100
        return match_rate
    
class StockPrediction():#주식 예측
    def __init__(self, w=None,  b=None) -> None:
        self._w = w
        self._b = b

    def set_parameter(self, w, b):
        self._w = w
        self._b = b

    def predict(self, date):
        return tf.matmul(date, self.w) + self.b

class Decide():    
    def __init__(self) -> None:
        self._rate_decide = RateDecide()
        self._pattern_decide = PatternDecide()
        self._stock_prediction = StockPrediction()
        
        self._pettern_rate = 1.0
        self._stock_rate = 1.0
    
    def _update_data(self, date, w, b, cur_data, is_pattern);
        self._match_rate = self._pattern_decide.pattern_calculation(is_pattern)#패턴 정답 비율
        
        self._stock_prediction.set_parameter(w, b)
        predict_data = self._stock_prediction.predict(date)#다음 주식 예측

        self._money_percent, self._is_buy = self._rate_decide.rate_decide(predict_data, cur_data)#예측 주식을 토대로 차이 비교

    def set_strategy_rate(self, pattern, stock_rate):#각 전략 중요도 설정
        self._pettern_rate = pattern
        self._stock_rate = stock_rate

    def _strategy(self):
        result = (self._match_rate * self._pettern_rate()) + (self._money_percent * self._stock_rate) if self._match_rate else 0
        return 100 if result > 100 else result
    
    def decide(self, date, w, b, cur_data, is_pattern):
        self._update_data(date, w, b, cur_data, is_pattern)
        return (self._strategy(), self._is_buy)

