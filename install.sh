#!/usr/bin/env bash
mkdir ~/.vim/syntax
mv my_syntax.vim ~/.vim/syntax/my_syntax.vim
vim example.txt
: set syntax=my_syntax
