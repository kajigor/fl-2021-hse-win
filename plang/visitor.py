from antlr4 import *
from plangLexer import plangLexer
from plangVisitor import plangVisitor
from plangParser import plangParser
import sys
from pprint import pprint

import codecs
import sys


class EvalVisitor(plangVisitor):
	def visitOpExpr(self, context):
		left = self.visit(context.left)
		right = self.visit(context.right)

		print('lr:', left, right)

		print('op:', context.op.text)
		operator = context.op.text[0]
		if operator == ',':
			val = left & right
		elif operator == ';':
			val = left | right
		else:
			raise ValueError("Unknown operatorL " + operator)
		print("visitOpExpr", operator, left, right, val)
		return val

	def visitStart(self, context):
		print("visitStart", context.getText())
		return self.visit(context.start())

	def visitAtomExpr(self, context):
		print("visitAtomExpr", int(context.getText()))
		return int(context.getText())

	def visitParentExpr(self, context):
		print("visitParenExpr", context.getText())
		return self.visit(context.expr())


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
	out = EvalVisitor().visit(tree)
	file = open('./outputs/output%s.result', 'w')
	file.write(out)
	file.close()
	# print(answer)


if __name__ == '__main__':
	# antlr4 -Dlanguage=Python3 -visitor plang.g4
	main()
