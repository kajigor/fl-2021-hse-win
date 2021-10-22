#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from plang.src.kernel.args_handle import argsHandle
from plang.src.testing.Tester import Tester
from plang.src.testing.Generator import Generator


def main():
	_, n_tests = argsHandle(1)

	tester = Tester()
	tester.doTests([(Generator.program(), True) for _ in range(int(n_tests))])


if __name__ == '__main__':
	main()
