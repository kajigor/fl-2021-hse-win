let b:current_syntax = "my_syntax"

" match integer
syn match Number "[+-]\?\d\+"

" match float
syn match Number "[-+]\*\d\+\.\d*"
syn match Number "[-+]\*\d\*\.\d+"

" match 'terminal' keyword 
syn keyword Statement terminal

hi def link Number Constant
hi def link Statement Statement
