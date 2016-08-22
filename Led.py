import Pins

import time
import Adafruit_BBIO.GPIO as GPIO
from multiprocessing import Process

# Do we still have these pins on this project?
NETWORK_LED	= Pins.NETWORK_LED

HB_LED		= Pins.R1_RED_LED

LED_OFF		= 0
LED_ON		= 1

LED_setup = {}


def LED(pin, mode):
	if pin not in LED_setup or LED_setup[pin] == 0:
		GPIO.setup(pin, GPIO.OUT)
		LED_setup[pin] = 1
	if mode == LED_ON:
		#GPIO.setup(pin, GPIO.OUT)
		GPIO.output(pin, GPIO.HIGH)
	if mode == LED_OFF:
		#GPIO.setup(pin, GPIO.OUT)
		GPIO.output(pin, GPIO.LOW)

def Blink(pin, delay):
	LED(pin, LED_ON)
	proc = Process(target=BlinkOff, args=(pin, delay,))
	proc.start()
def BlinkOff(pin, delay):
	time.sleep(delay)
	LED(pin, LED_OFF)

def Wink(pin, delay):
	LED(pin, LED_OFF)
	proc = Process(target=WinkOff, args=(pin, delay,))
	proc.start()
def WinkOff(pin, delay):
	time.sleep(delay)
	LED(pin, LED_ON)

def NetworkOn():
	LED(NETWORK_LED, LED_ON)
def NetworkOff():
	LED(NETWORK_LED, LED_OFF)
def NetworkBlink(delay=1):
	Blink(NETWORK_LED, delay)

def HBOn():
	LED(HB_LED, LED_ON)
def HBOff():
	LED(HB_LED, LED_OFF)
def HBBlink(delay=1):
	Blink(HB_LED, delay)

