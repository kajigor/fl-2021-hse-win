#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from plang.kernel.Parser import Parser
from TestGenerator import TestGenerator
from Counter import Counter


class Tester:
	def __init__(self, seed=1337):
		self.generator = TestGenerator(seed)

	def saveLog(self, dirname, program, out):
		Counter.inc()
		directory = './logs/' + dirname + '/' + str(Counter.value()) + '/'
		os.mkdir(directory)
		path = directory + 'program' + str(Counter.value()) + '.p'
		with open(path + '.p', 'w') as file:
			file.write(program)
		with open(path + '.p.out', 'w') as file:
			file.write(out)

	def saveTestResult(self, program, correctness, result, out):
		if correctness and result:
			self.saveLog('correct', program, out)

	def doTest(self, program, correctness):
		parser = Parser(program)
		self.saveTestResult(program, correctness, parser.parse(stderr=False, saveErrors=True), parser.getResult())

	def doTests(self, repeats):
		pass
