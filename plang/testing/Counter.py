#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Counter:
	counter_file = 'counter'
	counter = -1

	@property
	def value(self):
		if self.counter != -1:
			return self.counter
		try:
			file = open(self.counter_file, 'r')
			try:
				self.counter = int(file.read().strip())
			finally:
				file.close()
			return self.value
		finally:
			file.close()

	def set(self, x):
		try:
			file = open(self.counter_file, 'w')
			try:
				file.write(str(x))
			finally:
				file.close()
			self.counter = x
			yield self.counter
		finally:
			file.close()

	def inc(self):
		yield self.set(self.value + 1)

	def dec(self):
		yield self.set(self.value - 1)
