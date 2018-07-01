import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

MOTOR1_CONFIG = {"e":11,"f":15,"r":13}
MOTOR2_CONFIG = {"e":22,"f":16,"r":18}
MOTOR3_CONFIG = {"e":19,"f":21,"r":23}
MOTOR4_CONFIG = {"e":32,"f":24,"r":26}

class Motor:
    def __init__(self, pin_config):
        self.pins = {}
        self.pins['e'] = pin_config['e']
        self.pins['f'] = pin_config['f']
        self.pins['r'] = pin_config['r']

        GPIO.setup(self.pins['e'],GPIO.OUT)
        GPIO.setup(self.pins['f'],GPIO.OUT)
        GPIO.setup(self.pins['r'],GPIO.OUT)

	self.PWM = GPIO.PWM(self.pins['e'], 50)
	self.PWM.start(0)

        GPIO.output(self.pins['e'],GPIO.HIGH)
        GPIO.output(self.pins['f'],GPIO.LOW)
        GPIO.output(self.pins['r'],GPIO.LOW)

    def forward(self, speed):
	self.PWM.ChangeDutyCycle(speed)
        GPIO.output(self.pins['f'],GPIO.HIGH)
        GPIO.output(self.pins['r'],GPIO.LOW)

    def reverse(self, speed):
	self.PWM.ChangeDutyCycle(speed)
        GPIO.output(self.pins['f'],GPIO.LOW)
        GPIO.output(self.pins['r'],GPIO.HIGH)

    def stop(self):
        GPIO.output(self.pins['f'],GPIO.LOW)
        GPIO.output(self.pins['r'],GPIO.LOW)

    def id():
        return '' + pins['e'] + pins['f'] + pins['r']
