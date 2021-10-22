#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Counter:
	counter_file = 'counter'
	counter = -1

	@staticmethod
	def value():
		if Counter.counter != -1:
			return Counter.counter
		try:
			file = open(Counter.counter_file, 'r')
			try:
				Counter.counter = int(file.read().strip())
			finally:
				file.close()
			return Counter.counter
		finally:
			file.close()

	@staticmethod
	def set(x):
		try:
			file = open(Counter.counter_file, 'w')
			try:
				file.write(str(x))
			finally:
				file.close()
			Counter.counter = x
			yield Counter.counter
		finally:
			file.close()

	@staticmethod
	def inc():
		yield Counter.set(Counter.value() + 1)

	@staticmethod
	def dec():
		yield Counter.set(Counter.value() - 1)
