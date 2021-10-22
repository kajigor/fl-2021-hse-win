#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from plang.kernel.args_handle import argsHandle
from Tester import Tester


def main():
	_, n_tests = argsHandle(1)

	tester = Tester()

	tester.doTests(n_tests)


if __name__ == '__main__':
	main()
