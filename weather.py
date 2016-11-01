#!/usr/bin/env python

import time
import pdb
from termcolor import colored
from datetime import datetime

import Adafruit_CharLCD as LCD
import Adafruit_GPIO.MCP230xx as MCP

import pyowm

#####################################################################
# MCP23017 not working as advertised. Shows up as i2C device 
# but lcd functions dont work properly. Investigate later, use gpios to 
# drive LCD for now
#####################################################################

# Default: Initialize the LCD using the pins 
lcd = LCD.Adafruit_CharLCDPlate()

lcd.clear()

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

empty_space = '                '
##############################################################################
# Openweather API Key
api_key = 'f5d11783a8eac21d0380c314d73c4ebb'
owm = pyowm.OWM(api_key) 

def post_weather(temp, humidity):
	
	# Clear LCD, reset cursor
	
	lcd.clear()
	#pdb.set_trace()
	# Set LCd backlight color to blue 
	lcd.set_color(1.0,1.0,0.0)
	#print colored(elem + ": " + price + " " + change, 'red')
	
	# Quote on first line + price info on second line
	lcd.message('Temp: ' + str(temp) + chr(223) + 'F' + '\n' + 'Humidity: ' + str(humidity) + '%')
        return 0

##############################################################################

# Run in a loop
while 1:
	observation = owm.weather_at_place('Folsom,ca')
	try:
		w = observation.get_weather()
		temp = w.get_temperature('fahrenheit')
	except (RuntimeError, TypeError, NameError):
		print "Caught Exception...whatever.."
	curr_temp = temp['temp']
	#print curr_temp
	humidity = w.get_humidity()
	#print humidity
	post_weather(curr_temp,humidity)
	#print colored(curr_temp, 'blue')
	time.sleep(600)
