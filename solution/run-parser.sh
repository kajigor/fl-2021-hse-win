#!/usr/bin/env bash

if [[ "$#" -ne 2 ]]; then
  echo "Illegal number of parameters"
  exit 1
fi

CUR_DIR=$PWD
cd /usr/local/lib
sudo curl -Os "https://www.antlr.org/download/antlr-4.9-complete.jar"

cd "$CUR_DIR"
export CLASSPATH=".:/usr/local/lib/antlr-4.9-complete.jar:$CLASSPATH"
alias antlr4='java -Xmx500M -cp "/usr/local/lib/antlr-4.9-complete.jar:$CLASSPATH" org.antlr.v4.Tool'
# alias grun='java -Xmx500M -cp "/usr/local/lib/antlr-4.9-complete.jar:$CLASSPATH" org.antlr.v4.gui.TestRig'
shopt -s expand_aliases
source ~/.bashrc

antlr4 -Dlanguage=Python3 -visitor DKA.g4
python3 visitor.py "$1" > "$2" 2> /dev/null
