#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
