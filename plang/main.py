#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from kernel.args_handle import argsHandle
from kernel import iocontrol
from kernel.Parser import Parser


def main():
	_, filename, key_args = argsHandle(1, ('silent-errors', 'silent-result', 'nofile'))

	with Parser(iocontrol.programFromFile(filename)) as parser:
		parser.parse()
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

	if not 'silent-result' in key_args:
		print(out)


if __name__ == '__main__':
	main()
