#!/usr/bin/env bash

res_file="$1"
>"${res_file}.out"
python3 parser.py "$res_file"

g++ -o hopcroft hopcroft.cpp
./hopcroft "${res_file}.out"
rm hopcroft
