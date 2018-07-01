class Blind:
    def __init__(self, motor, counter):
        self.motor = motor
	self.counter = counter

    def go_to(self, count, speed):
      if self.counter.get_count() == count:
        return
      self.counter.stop_after(count, self.motor.stop)
      if self.counter.get_count() < count:
        self.motor.forward(speed)
      else:
        self.motor.reverse(speed)
