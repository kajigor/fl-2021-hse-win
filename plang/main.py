#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from kernel.argsHandle import argsHandle
from kernel import iocontrol
from kernel.parser import Parser


def main():
	_, filename, key_args = argsHandle(2, ('silent-errors', 'silent-result', 'nofile'))

	with Parser(iocontrol.programFromFile(filename)) as parser:
		out = parser.getStringTree() if parser.parse('silent-errors' in key_args) else parser.errorsReport()

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
