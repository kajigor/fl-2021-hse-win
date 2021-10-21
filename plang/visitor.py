from antlr4 import *
from plangLexer import plangLexer
from plangVisitor import plangVisitor
from plangParser import plangParser
import sys
from pprint import pprint

import codecs
import sys


class EvalVisitor(plangVisitor):
	def visitStart(self, context):
		# print("visitStart", context.getText())
		return self.visit(context.program())

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
		print("visitOpExpr", operator, left, right, val)
		return out

	def visitStart(self, ctx):
		print("visitStart", ctx.getText())
		return self.visit(ctx.expr())

	def visitAtomExpr(self, ctx):
		print("visitAtomExpr", int(ctx.getText()))
		return int(ctx.getText())

	def visitParenExpr(self, ctx):
		print("visitParenExpr", ctx.getText())
		return self.visit(ctx.expr())



def main():
	sample = 3
	file = open('./programs/program%s.p' % sample, 'r')
	program = file.read().strip()
	file.close()

	# lexer = plangLexer(StdinStream())
	lexer = plangLexer(InputStream(program))
	stream = CommonTokenStream(lexer)
	parser = plangParser(stream)
	tree = parser.start()
	out = EvalVisitor().visit(tree)

	file = open('./outputs/output%s.result' % sample, 'w')
	file.write('' if out is None else out)
	file.close()
	# print(out)


if __name__ == '__main__':
	# antlr4 -Dlanguage=Python3 -visitor plang.g4
	main()
