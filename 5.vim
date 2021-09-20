let b:current_syntax = "5"

syn keyword Keyword for if while else break continue const do switch case return public private protected using namespace
syn keyword Type int signed unsigned float double long char auto void struct class
syn keyword Constant nullptr true false

syn match Constant '[+-]\?\(\d\+\.\?\d*\|\.\d\+\)'
syn match PreProc '^#.*'

syn match String '".*"'

hi String ctermfg=Red
