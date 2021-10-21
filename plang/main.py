#!/usr/bin/env python3

from antlr4 import *
from plangLexer import plangLexer
from plangParser import plangParser

from kernel import iocontrol
from kernel.parser import Parser

import re
import sys

def main():
	if len(sys.argv) < 2:
		print('Wrong number of arguments', file=sys.stderr)
		exit(1)
	filename = sys.argv[1]
	program = iocontrol.programFromFile(filename)

	lexer = plangLexer(InputStream(program))
	stream = CommonTokenStream(lexer)
	parser = plangParser(stream)

	tree, errors_raw = iocontrol.grabOutstreams(parser.start, err=True)

	if len(errors_raw) == 0:
		out = tree.toStringTree().replace(r'\n', '\n')
	else:
		def explainer(issue):
			return ''

		def issuePointer(line, left, right=None):
			right = left if right is None else right
			return line + '\n' + ' ' * left + '^' * (right - left + 1)

		program_lines = program.strip().splitlines()
		errors = errors_raw.strip().splitlines()
		error_messages = []
		for i, error_raw in zip(errors):
			line, column, error_content = map(lambda i, x: x if i == 2 else int(x) - 1, re.findall('^line (\d+):(\d+) (.+)', error_raw)[0])
			error_messages.append('Error at %s:%i:%i error: ' % (program_lines[line], line + 1, column + 1) + explainer(error_content) + '\n' + issuePointer(program_lines[line], column))
		out = '\n'.join(error_messages)

	try:
		output = open(filename + '.out', 'w')
		try:
			output.write(out + '\n')
		finally:
			output.close()
	except:
		print(out)


if __name__ == '__main__':
	main()
