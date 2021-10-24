#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.kernel.args_handle import argsHandle
from src.kernel import iocontrol
from src.kernel.Parser import Parser


def main():
	_, filename, key_args = argsHandle(1, ('silent-errors', 'silent-result', 'nofile'))

	parser = Parser(iocontrol.programFromFile(filename))
	result = parser.parse(not 'silent-errors' in key_args)
	out = parser.getResult()

	if not 'nofile' in key_args:
		try:
			output = open(filename + '.out', 'w')
			try:
				output.write(out + '\n')
			finally:
				output.close()
		finally:
			output.close()

	if not 'silent-result' in key_args and result:
		print(out)


if __name__ == '__main__':
	main()
