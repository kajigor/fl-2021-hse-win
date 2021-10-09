let b:current_syntax = "dfa"

syn match S 's: .*'
hi S ctermfg=Red

syn match W 'w: .*'
hi W ctermfg=Green

syn match N 'n: .*'
hi N ctermfg=Magenta

syn match T 't: .*'
hi T ctermfg=Blue
