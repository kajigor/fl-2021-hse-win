from antlr4 import *
from plangLexer import plangLexer
from plangVisitor import plangVisitor
from plangParser import plangParser
import sys
from pprint import pprint


def main():
	sample = 1
	file = open('./programs/program%s.p' % sample, 'r')
	program = file.read().strip()
	file.close()

	# lexer = plangLexer(StdinStream())
	lexer = plangLexer(InputStream(program))
	stream = CommonTokenStream(lexer)
	parser = plangParser(stream)
	tree = parser.start()
	#tree = parser.start()
	#out = EvalVisitor().visit(tree)

	#file = open('./outputs/output%s.result' % sample, 'w')
	#file.write('' if parser is None else parser)
	#file.close()
	# print(out)


if __name__ == '__main__':
	# antlr4 -Dlanguage=Python3 -visitor plang.g4
	main()
