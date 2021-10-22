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
	def newlines(n):
		return '\n' * n

	@staticmethod
	def identificator(n):
		return Generator.randomLower() + Generator.word(n - 1)

	@staticmethod
	def variable(n):
		return Generator.randomUpper() + Generator.word(n - 1)

	@staticmethod
	def argument():
		r = rand(1, 4)
		if r == 1:
			return ' ' + Generator.variable(rand(1, 5))
		elif r == 2:
			return ' (' + Generator.variable(rand(1, 5)) + ')'
		elif r == 3:
			return ' (' + Generator.atom() + ')'
		else:
			return ' ' + Generator.identificator(rand(1, 5))

	@staticmethod
	def atom():
		return Generator.identificator(rand(1, 5)) + Generator.repeat(Generator.argument, rand(0, 4))

	@staticmethod
	def string():
		return Generator.atom() + (' :-' + Generator.goal() if rand(0, 1) == 1 else '.') + Generator.newlines(rand(1, 3))

	# Очень глубоко в рекурсию уходить, конечно, не хочется. Это нужно как-то ограничивать.
	@staticmethod
	def arithmetic(depth=0):
		if depth == 5:
			r = 1
		else:
			r = rand(1, 4)
		if r == 1:
			return Generator.atom()
		elif r == 2:
			return '(' + Generator.arithmetic(depth + 1) + ')'
		elif r == 3:
			return Generator.arithmetic(depth + 1) + '; ' + Generator.arithmetic(depth + 1)
		return Generator.arithmetic(depth + 1) + ', ' + Generator.arithmetic(depth + 1)

	@staticmethod
	def goal():
		return ' ' + Generator.arithmetic() + '.'

	@staticmethod
	def relationship():
		return Generator.repeat(Generator.string, rand(1, 5))

	@staticmethod
	def program():
		return Generator.repeat(Generator.relationship, rand(0, 5)) + '?' + Generator.goal() + Generator.newlines(rand(0, 4))

	@staticmethod
	def incorrectProgram():
		return ''
