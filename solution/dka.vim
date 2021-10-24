let b:current_syntax = "dka"

" match numbers
syn match Number "[+-]\?\d\+"
syn match Number "[+-]\?\d\+\.\d\*"

" match states and alphabet symbols
syn match Symbol "[a-zA-Z_][a-zA-Z0-9_]*"

" match keywords
syn keyword Keyword states alpha initial accepting trans

hi def link Number Number
hi def link Symbol Type
hi def link Keyword Statement
