#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import io


def programFromFile(filename):
	try:
		file = open(filename, 'r')
		try:
			return file.read().strip()
		finally:
			file.close()
	except:
		print('Bad file argument')
		exit(1)


def grabOutstreams(function, out=False, err=False):
	if out:
		out_stream = io.StringIO('')
		sys.stderr = out_stream
	if err:
		err_stream = io.StringIO('')
		sys.stderr = err_stream
	yield function()
	if out:
		yield out_stream.getvalue()
		out_stream.close()
		sys.stdout = sys.__stdout__
	if err:
		yield err_stream.getvalue().strip()
		err_stream.close()
		sys.stderr = sys.__stderr__
