#!/usr/bin/env bash

antlr4 -Dlanguage=Python3 -visitor plang.g4 -o vendor
