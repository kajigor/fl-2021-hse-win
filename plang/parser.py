#!/usr/bin/env python3

from antlr4 import *
from plangLexer import plangLexer
from plangParser import plangParser
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
		program = file.read()
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
	errors = error_stream.getvalue().strip()
	sys.stderr = backup
	error_stream.close()

	if len(errors) == 0:
		out = tree.toStringTree().replace('\\n', '\n')
	else:
		out = errors

	try:
		output = open(filename + '.out', 'w')
	except:
		print(out)
	else:
		output.write(out)
		output.close()


if __name__ == '__main__':
	main()
