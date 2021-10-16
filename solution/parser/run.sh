# !/bin/bash

python3 parser_yacc.py input.txt
dot -Tpng input.txt.out > output.png
