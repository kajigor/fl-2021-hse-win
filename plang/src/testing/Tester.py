#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time

from plang.src.kernel.Parser import Parser
from plang.src.testing.Generator import Generator


class Tester:
	def __init__(self, seed=1337):
		self.generator = Generator.setSeed(seed)

	def saveTestLog(self, test_id, dirname, program, out):
		directory = './src/testing/logs/' + dirname + '/' + str(test_id) + '/'
		os.mkdir(directory)
		path = directory + 'program' + str(test_id) + '.p'
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
		test_id = hex(int(str(time.time()).replace('.', '')))[2:]
		parser = Parser(program)
		situation = self.getTestResultName(correctness, parser.parse(stderr=False, saveErrors=True))
		self.saveTestLog(test_id, situation, program, parser.getResult())
		return situation

	def doTests(self, tests):
		for program, correctness in tests:
			self.doTest(program, correctness)
