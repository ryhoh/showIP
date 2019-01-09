# -*- coding: utf-8 -*-

# show IPaddress by using Adafruit's Library

import Adafruit_CharLCD as LCD
import netifaces

# GPIO mapping
lcd_rs = 2
lcd_en = 3
lcd_d4 = 4
lcd_d5 = 14
lcd_d6 = 15
lcd_d7 = 17
lcd_backlight = 18	# not connected

# LCD parameters
lcd_columns = 16
lcd_rows = 2

# initialize
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

# print
lcd.message('Raspberry Pi 2B\n')
lcd.message(netifaces.ifaddresses("eth0")[netifaces.AF_INET][0]['addr'])

#lcd.message('test')


