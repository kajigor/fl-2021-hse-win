#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re

from antlr4 import *
from plang.vendor.plangLexer import plangLexer
from plang.vendor.plangParser import plangParser

from plang.kernel import iocontrol


class Parser:
	def __init__(self, program):
		self.program = program
		self.correct = None

	def analyzeErrors(self, errors_raw, error_stream=sys.stderr):
		def explainer(issue):
			return ''

		def issuePointer(line, left, right=None):
			right = left if right is None else right
			return line + '\n' + ' ' * left + '^' * (right - left + 1)

		program_lines = self.program.strip().splitlines()
		errors = errors_raw.strip().splitlines()
		for i, error_raw in zip(errors):
			line, column, error_content = map(lambda i, x: x if i == 2 else int(x) - 1, re.findall('^line (\d+):(\d+) (.+)', error_raw)[0])
			error_message = 'Error at %s:%i:%i error: ' % (program_lines[line], line + 1, column + 1) + explainer(error_content) + \
							'\n' + issuePointer(program_lines[line], column)
			yield error_message
			if not error_stream is None:
				print(error_message, file=error_stream)

	def errorsReport(self):
		if hasattr(self, 'errors'):
			return '\n'.join(self.errors)
		raise Exception('Errors were not saving.')

	def parse(self, stderr=True, saveErrors=True):
		self.lexer = plangLexer(InputStream(self.program))
		self.stream = CommonTokenStream(self.lexer)
		self.parser = plangParser(self.stream)

		self.tree, errors_raw = iocontrol.grabOutstreams(self.parser.start, err=True)

		if len(errors_raw) == 0:
			self.correct = True
			return True

		analyze = lambda: self.analyzeErrors(errors_raw, sys.stderr if stderr else None)
		if saveErrors:
			self.errors = list(analyze())
		else:
			analyze()
		self.correct = False
		return False

	def getStringTree(self, storeTree=True):
		if storeTree:
			if not hasattr(self, 'stringTree'):
				self.stringTree = self.tree.toStringTree().replace(r'\n', '\n')
			else:
				return self.stringTree
		return self.stringTree

	def getResult(self):
		if self.correct is None:
			raise Exception("Parsing has not been done yet.")
		return self.getStringTree() if self.correct == True else self.errorsReport()
