#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.kernel.args_handle import argsHandle
from src.testing.Tester import Tester
from src.testing.Generator import Generator


def main():
	_, n_tests = argsHandle(1)

	# TODO: отчёт о текущем состоянии в консольку
	Tester.doTests([(Generator.program(), True) for _ in range(int(n_tests))])


if __name__ == '__main__':
	main()
