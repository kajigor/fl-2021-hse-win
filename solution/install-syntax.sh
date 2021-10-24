#!/usr/bin/env bash

mkdir "$HOME/.vim/syntax/" 2> /dev/null
cp dka.vim "$HOME/.vim/syntax/dka.vim"
cp code-formatter.py "$HOME/.vim/syntax/code-formatter.py"

{
  printf "noremap [      []<Left>\n";
  printf "noremap [[     [\n";
  printf "noremap []     []\n";
  printf "noremap (      ()<Left>\n";
  printf "noremap ((     (\n";
  printf "noremap ()     ()\n";
  printf "noremap {      {}<Left>\n";
  printf "noremap {{     {\n";
  printf "noremap {}     {}\n";
  printf "\n";
  printf "noremap <C-l> :silent execute \"!(python3 \$HOME/.vim/syntax/code-formatter.py %% 2> /dev/null)\"<CR>\n";
  printf "\n";
  printf "au BufRead,BufNewFile *.dka set filetype=dka\n";
  printf "\n";
} >> "$HOME/.vimrc"
