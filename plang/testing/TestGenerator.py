#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


class TestGenerator:
	def __init__(self, seed=1337):
		self.seed = seed
		random.seed(seed)

	def generateCorrectProgram(self):
		out = []
		out = '?'
		return ''

	def generateIncorrectProgram(self):
		return ''
