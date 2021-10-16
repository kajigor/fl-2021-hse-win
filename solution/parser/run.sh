# !/bin/bash

python3 parser_yacc.py
dot -Tpng output.dot > output.png
