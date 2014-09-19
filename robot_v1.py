#!/usr/bin/python
import sys
import struct
from time import sleep

import serial

def two_secons(func):
	def _decorator(self, *args, **kwargs):
		self.sing()
		func(self, *args, **kwargs)
		sleep(2)
		self.stop()
	return _decorator


class Bot(object):
	"""
	it's a bot
	"""

	STOP = [128, 131, 145, 0, 0, 0, 0]
	
	HARD_LEFT = [128, 131, 145, 127, 255, 128, 255]
	HARD_RIGHT = [128, 131, 145, 128, 255, 127, 255]
	
	LEFT =  [128, 131, 145, 0, 64, 255, 64]
	RIGHT = [128, 131, 145, 255, 64, 0, 64]
	
	FORWARD =      [128, 131, 145, 0, 64, 0, 64]
	FAST_FORWARD = [128, 131, 145, 127, 255, 127, 255]

	BACKWARD = [128, 131, 145, 255, 64, 255, 64]
	FAST_BACKWARD = [128, 131, 145, 128, 255, 128, 255]

	TURN_LED = [128, 132, 139, 2, 0, 0]
	SING  = [128, 132, 140, 0, 4, 62, 12, 66, 12, 69, 12, 74, 36, 141, 0]


	def __init__(self):
				
		print 'init'
		for i in range(10):
			try:
				self.serial = serial.Serial('/dev/ttyUSB' + str(i), baudrate=57600)
			except Exception as exp:
				print exp
				print 'except %s' % i
				continue
			break


		# dir_self = dir(self)
		# dir_self = filter(lambda att: not att.startswith('_'), dir_self)
		# actions = filter(lambda att: att.isupper(), dir_self)

		# for action in actions:

		# 	def baa():
		# 		self._execute(self.__getattribute__(action))
		# 	self.__setattr__(action.lower(), baa)

	def tearDown(self):
        	self.serial.close()

	@two_secons	
	def forward(self):
		self._execute(self.FORWARD)

	@two_secons
	def backward(self):
		self._execute(self.BACKWARD)

	@two_secons
	def fast_forward(self):
		self._execute(self.FAST_FORWARD)

	@two_secons
	def fast_backward(self):
		self._execute(self.FAST_BACKWARD)

	@two_secons
	def left(self):
		self._execute(self.LEFT)

	@two_secons
	def right(self):
		self._execute(self.RIGHT)

	@two_secons
	def hard_left(self):
		self._execute(self.HARD_LEFT)

	@two_secons
	def hard_right(self):
		self._execute(self.HARD_RIGHT)

	def turn_led(self):
		self._execute(self.TURN_LED)

	def stop(self):
		self._execute(self.STOP)

	
	def sing(self):
		self._execute(self.SING)

	def _execute(self, command):
		number_args = len(command)
		bs = "B" * number_args
		command = [bs] + command	
		command = struct.pack(*command)
		self.serial.write(command)


if __name__ == '__main__':
	print "creating the Bot"
	try:
		bot =  Bot()
	except e:
		print "Error creating Bot: " + e
	print "Bot Created"
	try:	
		action = sys.argv[1]
	except:
		action = None

	if action == 'forward':
		bot.forward()
	if action == 'backward':
		bot.backward()
	if action == 'fast_forward':
		bot.fast_forward()
	if action == 'fast_backward':
		bot.fast_backward()
	elif action == 'left':
		bot.left()
	elif action == 'right':
		bot.right()
	elif action == 'hard_left':
		bot.hard_left()
	elif action == 'hard_right':
		bot.hard_right()
	if action == 'stop':
		bot.stop()
	elif action == 'sing':
		bot.sing()
	print "Closing serial port"
	bot.tearDown()
	print "Port closed"

