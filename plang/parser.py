#!/usr/bin/env python3

from antlr4 import *
from plangLexer import plangLexer
from plangParser import plangParser
import sys


def main():
	program = ''
	try:
		filename = sys.argv[1]
		file = open(filename, 'r')
		program = file.read()
		file.close()
	except:
		print('Bad file argument', file=sys.stderr)
		exit(1)

	lexer = plangLexer(InputStream(program))
	stream = CommonTokenStream(lexer)
	parser = plangParser(stream)
	tree = parser.start()

if __name__ == '__main__':
	main()
