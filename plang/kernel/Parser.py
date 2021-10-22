#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re

from antlr4 import *
from plang.vendor.plangLexer import plangLexer
from plang.vendor.plangParser import plangParser

from plang.kernel import iocontrol


class Parser:
	class ErrorsWereNotSaved(Exception):
		pass

	def __init__(self, program):
		self.program = program

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
		raise Parser.ErrorsWereNotSaved

	def parse(self, stderr=True, saveErrors=True):
		self.lexer = plangLexer(InputStream(self.program))
		self.stream = CommonTokenStream(self.lexer)
		self.parser = plangParser(self.stream)

		self.tree, errors_raw = iocontrol.grabOutstreams(self.parser.start, err=True)

		if len(errors_raw) == 0:
			return True

		analyze = lambda: self.analyzeErrors(errors_raw, sys.stderr if stderr else None)
		if saveErrors:
			self.errors = list(analyze())
		else:
			analyze()
		return False

	def getStringTree(self, storeTree=True):
		if storeTree:
			if not hasattr(self, 'stringTree'):
				self.stringTree = self.tree.toStringTree().replace(r'\n', '\n')
			else:
				return self.stringTree
		return self.stringTree
