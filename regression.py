class Regression():
  def __init__(self):
    self._learning_rate = 0.01
    self.init_parameter()

  def set_learning_rate(self, learning_rate):
    self._learning_rate = learning_rate

  def init_parameter(self):
    #self._W = tf.Variable(tf.random.normal((1,), -10., 10.))
    #self._b = tf.Variable(tf.random.normal((1,), -10., 10.))
    self._W = tf.Variable(2.9)
    self._b = tf.Variable(0.5)

  def get_parameter(self):
    return self._W, self._b

  def update_parameter(self, x_datas, y_datas, epoch = 2000):
    cost = 10.0
    i = 1
    while cost > 0.7:
    #for i in range(epoch+1):
        with tf.GradientTape() as tape:
            hypothesis = self._W * x_datas + self._b
            cost = tf.reduce_mean(tf.square(hypothesis - y_datas))
        W_grad, b_grad = tape.gradient(cost, [self._W, self._b])
        self._W.assign_sub(self._learning_rate * W_grad)
        self._b.assign_sub(self._learning_rate * b_grad)
        if i % epoch == 0:
          print("{:5}|{:10.4f}|{:10.4f}|{:10.6f}".format(i, self._W.numpy(), self._b.numpy(), cost))
          #print(i, self._W, self._b, cost)
        i += 1
    print("{:5}|{:10.4f}|{:10.4f}|{:10.6f}".format(i, self._W.numpy(), self._b.numpy(), cost))
    return self._W, self._b

  def predict(self, date):
        return self._W * date + self._b
