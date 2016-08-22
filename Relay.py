import Adafruit_BBIO.GPIO as GPIO


RELAY_OFF		= 0
RELAY_ON		= 1

relay_setup = {}


def relay(pin, mode):
	if pin not in relay_setup or relay_setup[pin] == 0:
		GPIO.setup(pin, GPIO.OUT)
		relay_setup[pin] = 1
	if mode == RELAY_ON:
		#GPIO.setup(pin, GPIO.OUT)
		GPIO.output(pin, GPIO.HIGH)
	if mode == RELAY_OFF:
		#GPIO.setup(pin, GPIO.OUT)
		GPIO.output(pin, GPIO.LOW)


