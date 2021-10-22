#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
from random import randint as rand


class Generator:
	alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
	lower = 'abcdefghijklmnopqrstuvwxyz'
	upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	digits = '0123456789'

	@staticmethod
	def setSeed(seed=1337):
		random.seed(seed)

	@staticmethod
	def getRandom(a):
		return a[rand(0, len(a) - 1)]

	@staticmethod
	def randomLower():
		return Generator.getRandom(Generator.lower)

	@staticmethod
	def randomUpper():
		return Generator.getRandom(Generator.upper)

	@staticmethod
	def randomSym():
		return Generator.getRandom(Generator.alpha)

	@staticmethod
	def repeat(tokenGenerator, n):
		return ''.join([tokenGenerator() for _ in range(n)])

	@staticmethod
	def word(n):
		return Generator.repeat(Generator.randomSym, n)

	#########

	@staticmethod
	def newlines(l=1, r=3):
		return '\n' * rand(l, r)

	@staticmethod
	def identificator(l=1, r=5):
		return Generator.randomLower() + Generator.word(rand(l - 1, r - 1))

	@staticmethod
	def variable(l=1, r=5):
		return Generator.randomUpper() + Generator.word(rand(l - 1, r - 1))

	@staticmethod
	def argument():
		r = rand(1, 4)
		if r == 1:
			return ' ' + Generator.variable()
		elif r == 2:
			return ' (' + Generator.variable() + ')'
		elif r == 3:
			return ' (' + Generator.atom() + ')'
		else:
			return ' ' + Generator.identificator()

	@staticmethod
	def atom():
		return Generator.identificator() + Generator.repeat(Generator.argument, rand(0, 4))

	@staticmethod
	def string():
		return Generator.atom() + (' :-' + Generator.goal() if rand(0, 1) == 1 else '.') + Generator.newlines()

	# Очень глубоко в рекурсию уходить, конечно, не хочется. Это нужно как-то ограничивать.
	@staticmethod
	def arithmetic():
		r = rand(1, 4)
		if r == 1:
			return Generator.atom()
		elif r == 2:
			return '(' + Generator.arithmetic() + ')'
		elif r == 3:
			return Generator.arithmetic() + '; ' + Generator.arithmetic()
		return Generator.arithmetic() + ', ' + Generator.arithmetic()

	@staticmethod
	def goal():
		return ' ' + Generator.arithmetic() + '.'

	@staticmethod
	def relationship():
		return Generator.repeat(Generator.string, rand(1, 5))

	@staticmethod
	def program():
		return Generator.repeat(Generator.relationship, rand(0, 5)) + '?' + Generator.goal() + Generator.newlines(0, 4)

	@staticmethod
	def incorrectProgram():
		return ''
