#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time

from ..kernel.Parser import Parser


class Tester:
	@staticmethod
	def saveTestLog(test_id, dirname, program, out):
		parent = './src/testing/logs/' + dirname + '/'
		try:
			os.mkdir(parent)
		except:
			pass
		directory = parent + str(test_id) + '/'
		os.mkdir(directory)
		path = directory + 'program' + str(test_id) + '.p'

		with open(path, 'w') as file:
			file.write(program)

		with open(path + '.out', 'w') as file:
			file.write(out)

	@staticmethod
	def getTestResultName(correctness, result):
		if correctness and result:
			return 'correct'
		elif correctness and not result:
			return 'false-incorrect'
		elif not correctness and result:
			return 'false-correct'
		return 'incorrect'

	@staticmethod
	def doTest(program, correctness):
		test_id = hex(int(str(time.time()).replace('.', '')))[2:]
		parser = Parser(program)
		situation = Tester.getTestResultName(correctness, parser.parse(stderr=False, saveErrors=True))
		Tester.saveTestLog(test_id, situation, program, parser.getResult())
		return situation

	@staticmethod
	def doTests(tests):
		for program, correctness in tests:
			Tester.doTest(program, correctness)
