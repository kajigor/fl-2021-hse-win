#!/usr/bin/env bash

cd ./vendor/
antlr4 -Dlanguage=Python3 -visitor plang.g4
