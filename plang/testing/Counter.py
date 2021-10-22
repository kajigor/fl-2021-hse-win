#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Counter:
	counter_file = 'counter'

	@staticmethod
	def value():
		with open(Counter.counter_file, 'r') as file:
			return int(file.read().strip())

	@staticmethod
	def set(x):
		with open(Counter.counter_file, 'w') as file:
			file.write(str(x))
		return x

	@staticmethod
	def inc():
		return Counter.set(Counter.value() + 1)

	@staticmethod
	def dec():
		return Counter.set(Counter.value() - 1)
