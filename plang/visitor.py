from antlr4 import *
from plangLexer import plangLexer
from plangVisitor import plangVisitor
from plangParser import plangParser
import sys
from pprint import pprint

import codecs
import sys


'''class EvalVisitor(plangVisitor):
	def visitStart(self, context):
		# print("visitStart", context.getText())
		return self.visit(context.program())

	def visitString(self, context):
		print("visitString", context.getText())


	def visitOpExpr(self, context):
		left = self.visit(context.left)
		right = self.visit(context.right)
		print(left, right)
		print('Test:', context.op.text)

		op = context.op.text[0]
		operator = op[0]
		if operator == ',':
			out = left & right
		elif operator == ';':
			out = left | right
		else:
			raise ValueError("Unknown operator " + op)
		print("visitOpExpr", operator, left, right, out)
		return out

	def visitAtomExpr(self, context):
		print("visitAtomExpr", int(context.getText()))
		return int(context.getText())

	def visitParenExpr(self, context):
		print("visitParenExpr", context.getText())
		return self.visit(context.expr())'''



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
