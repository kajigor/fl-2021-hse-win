#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
from random import randint as rand


class TestGenerator:
	alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
	lower = 'abcdefghijklmnopqrstuvwxyz'
	upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	digits = '0123456789'

	@staticmethod
	def setSeed(self, seed=1337):
		random.seed(seed)

	@staticmethod
	def getRandom(a):
		return a[rand(0, len(a) - 1)]

	@staticmethod
	def randomLower():
		return TestGenerator.getRandom(TestGenerator.lower)

	@staticmethod
	def randomUpper():
		return TestGenerator.getRandom(TestGenerator.upper)

	@staticmethod
	def randomSym():
		return TestGenerator.getRandom(TestGenerator.alpha)

	@staticmethod
	def repeat(symGenerator, n):
		return ''.join([symGenerator() for _ in range(n)])

	@staticmethod
	def string(n):
		return TestGenerator.repeat(TestGenerator.randomSym, n)

	@staticmethod
	def identificator(l = 1, r = 5):
		return TestGenerator.randomLower() + TestGenerator.string(rand(l - 1, r - 1))

	@staticmethod
	def generateAtom():
		return ''

	@staticmethod
	def generateProgram():
		out = []
		out = '?'
		return ''

	@staticmethod
	def generateIncorrectProgram():
		return ''
