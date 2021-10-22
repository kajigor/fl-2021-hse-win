#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from plang.kernel.Parser import Parser
from Generator import Generator
from Counter import Counter


class Tester:
	def __init__(self, seed=1337):
		self.generator = Generator.setSeed(seed)

	def saveTestLog(self, dirname, program, out):
		Counter.inc()
		directory = './logs/' + dirname + '/' + str(Counter.value()) + '/'
		os.mkdir(directory)
		path = directory + 'program' + str(Counter.value()) + '.p'
		with open(path, 'w') as file:
			file.write(program)
		with open(path + '.out', 'w') as file:
			file.write(out)

	def getTestResultName(self, correctness, result):
		if correctness and result:
			return 'correct'
		elif correctness and not result:
			return 'false-incorrect'
		elif not correctness and result:
			return 'false-correct'
		return 'incorrect'

	def doTest(self, program, correctness):
		parser = Parser(program)
		situation = self.getTestResultName(correctness, parser.parse(stderr=False, saveErrors=True))
		self.saveTestLog(situation, program, parser.getResult())
		return situation

	def doTests(self, tests):
		for program, correctness in tests:
			self.doTest(program, correctness)
