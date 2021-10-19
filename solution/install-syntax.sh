#!/usr/bin/env bash

mkdir "$HOME/.vim/syntax/" 2> /dev/null
cp highlighting.vim "$HOME/.vim/syntax/dka.vim"
cp code-formatter.py "$HOME/.vim/syntax/code-formatter.py"

mkdir "$HOME/.vim/ftdetect/" 2> /dev/null
cp newfiletype.vim "$HOME/.vim/ftdetect/dka.vim"

{
  printf "inoremap [      []<Left>\n";
  printf "inoremap [[     [\n";
  printf "inoremap []     []\n";
  printf "inoremap (      ()<Left>\n";
  printf "inoremap ((     (\n";
  printf "inoremap ()     ()\n";
  printf "inoremap {      {}<Left>\n";
  printf "inoremap {{     {\n";
  printf "inoremap {}     {}\n";
  printf "\ninoremap <C-M-l> :!python3 \$HOME/.vim/syntax/code-formatter.py %%<CR><l><CR>\n";
} >> "$HOME/.vimrc"
