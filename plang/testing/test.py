#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from plang.kernel.args_handle import argsHandle
from TestGenerator import TestGenerator


def main():
	_, n_tests = argsHandle(1)

	generator = TestGenerator()


if __name__ == '__main__':
	main()
