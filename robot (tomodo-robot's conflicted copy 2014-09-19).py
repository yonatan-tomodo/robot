#!/usr/bin/python
import sys
import struct
from time import sleep

import serial


class Bot(object):
	"""
	it's a bot
	"""

	STOP = [128, 131, 145, 0, 0, 0, 0]
	
	HARD_RIGHT = []
	HARD_LEFT = []
	
	LEFT =  [128, 131, 145, 0, 64, 255, 64]
	RIGHT = [128, 131, 145, 255, 64, 0, 64]
	
	FORWARD =      [128, 131, 145, 0, 64, 0, 64]
	FAST_FORWARD = [128, 131, 145, 127, 255, 127, 255]

	BACKWARD = [128, 131, 145, 255, 64, 255, 64]
	FAST_BACKWARD = [128, 131, 145, 128, 255, 128, 255]

	TURN_LED = [128, 132, 139, 2, 0, 0]
	SING  = [128, 132, 140, 0, 4, 62, 12, 66, 12, 69, 12, 74, 36, 141, 0]


	def __init__(self):
				
		for i in range(3):
			try:
				self.serial = serial.Serial('/dev/ttyUSB' + str(i), baudrate=57600)
			except:
				continue
			break


		dir_self = dir(self)
		dir_self = filter(lambda att: not att.startswith('_'), dir_self)
		actions = filter(lambda att: att.isupper(),dir_self)

		for action in actions:
			self.__setattr__(actions.lower(), lambda : self.execute(self.__getattribute__(action)))
	
	def forward(self):
		self._execute(self.FORWARD)

	def stop(self):
		self._execute(self.STOP)

	def left(self):
		pass

	def right(self):
		pass

	def turn_led(self):
		self._execute(self.TURN_LED)

	def define_song(self):
		self._execute(self.DEFINE_SONG)

	def sing(self):
		self._execute(self.SING)

	def full_mod(self):
		self._execute(self.FULL_MOD)

	def _execute(self, command):	
		number_args = len(command)
		bs = "B" * number_args
		command = [bs] + command	
		command = struct.pack(*command)
		self.serial.write(command)

if __name__ == '__main__':
	
	bot =  Bot()
	try:
		action = sys.argv[1]
	except:
		action = None

	bot.sing()
	bot.turn_led()
	bot.forward()
	sleep(1)
	bot.sing()
	bot.turn_led()
	sleep(1)
	bot.stop()
		
	if action == 'forward':
		bot.forward()
	if action == 'stop':
		bot.stop()
	elif action == 'left':
		bot.left()
	elif action == 'right':
		bot.right()

	
