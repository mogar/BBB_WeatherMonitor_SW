#!/usr/bin/python
import Pins
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
import time

class Input_Reader:
	#constructor to set up timing and pins
	def __init__(self):
		# counters for wind and rain
		self.wind_cnt = 0
		self.rain_cnt = 0

		# set up input pins
		GPIO.setup(Pins.WIND_SP, GPIO.IN)
		GPIO.setup(Pins.RAIN_SW, GPIO.IN)
		GPIO.cleanup()
		ADC.setup()

		GPIO.add_event_detect(Pins.WIND_SP, GPIO.FALLING, self.inputCB)
		GPIO.add_event_detect(Pins.RAIN_SW, GPIO.FALLING, self.inputCB)
		
		print("Input Reader ready")
		
	# monitors timing variables to determine if a tag has been read
	def Run(self):
		while(1):
			time.sleep(10)
			print("rain cnt: " + str(self.rain_cnt))
			print("wind cnt: " + str(self.wind_cnt))
			print("wind dir: " + str(ADC.read(Pins.WIND_DIR)))


	def inputCB(self, gpio):
		#print(gpio)
		if gpio == Pins.WIND_SP:
			self.wind_cnt += 1
		elif gpio == Pins.RAIN_SW:
			self.rain_cnt += 1


if __name__ == "__main__":
	r = Input_Reader()
	r.Run()
