#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def argsHandle(positionals=2, keys=None):
	if positionals < 1:
		raise Exception
	args = list(map(str.strip, sys.argv))
	if len(args) < positionals:
		print('Not enough arguments.', file=sys.stderr)
		exit(1)
	for i in range(positionals):
		yield args[i]
	if len(args) == positionals or keys is None:
		return
	yield set(keys) & set(map(lambda key: key[len(key) - str(reversed(key)).find('-') + 1:], args[positionals - 1:]))
