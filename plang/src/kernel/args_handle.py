#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def argsHandle(positionals=1, keys=None):
	if positionals < 0:
		raise Exception
	args = list(map(str.strip, sys.argv))
	if len(args) < positionals + 1:
		print('Not enough arguments.', file=sys.stderr)
		exit(1)
	for i in range(positionals + 1):
		yield args[i]
	if keys is None:
		return
	if len(args) == positionals + 1:
		yield set()
	else:
		yield set(keys) & set(map(lambda key: key[len(key) - str(reversed(key)).find('-') + 1:], args[positionals:]))
