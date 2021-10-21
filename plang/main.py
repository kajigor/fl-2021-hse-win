#!/usr/bin/env python3

from antlr4 import *
from plangLexer import plangLexer
from plangParser import plangParser
import re
import sys
import io


def main():
	global tree, program
	if len(sys.argv) < 2:
		print('Wrong number of arguments', file=sys.stderr)
		exit(1)
	filename = sys.argv[1]
	try:
		file = open(filename, 'r')
		try:
			program = file.read().strip()
		finally:
			file.close()
	except:
		print('Bad file argument', file=sys.stderr)
		exit(1)

	lexer = plangLexer(InputStream(program))
	stream = CommonTokenStream(lexer)
	parser = plangParser(stream)

	error_stream = io.StringIO('')
	backup = sys.stderr
	sys.stderr = error_stream
	tree = parser.start()
	errors_raw = error_stream.getvalue().strip()
	sys.stderr = backup
	error_stream.close()

	if len(errors_raw) == 0:
		out = tree.toStringTree().replace(r'\n', '\n')
	else:
		def explainer(issue):
			return ''
		def issuePointer(line, left, right=None):
			right = left if right is None else right
			return line + '\n' + ' ' * left + '^' * (right - left + 1)
		program_lines = program.strip().splitlines()
		errors = errors_raw.splitlines()
		error_messages = []
		for i, error_raw in zip(errors):
			line, column, error_content = re.findall('^line (\d+):(\d+) (.+)', error_raw)[0]
			error_messages.append('Error at %:%:% error: ' + explainer(error_content) + '\n' + issuePointer(program_lines[line - 1], column - 1))
		out = '\n'.join(error_messages)

	try:
		output = open(filename + '.out', 'w')
		try:
			output.write(out + '\n')
		finally:
			output.close()
	except IOError:
		print(out)


if __name__ == '__main__':
	main()
