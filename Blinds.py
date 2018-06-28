from threading import Timer

OPEN = 1;
CLOSE = 0;

class Blind:
    def __init__(self, motor, tto_secs):
        self.motor = motor
        self.tto_secs = tto_secs

    def open(self):
        if is_open():
            return;
        else:
            self.motor.reverse()
            self.schedule_stop(OPEN)

    def close(self):
        if not is_open():
            return;
        else:
            self.motor.forward()
            self.schedule_stop(CLOSE)

    def schedule_stop(end_state):
        timer = Timer(self.tto_secs, self.finish_action, [end_state])

    def finish_action(end_state):
        self.motor.stop
        #  persist: motor.id() -> end_state

    def is_open():
        return True # storage.get(motor.id())
