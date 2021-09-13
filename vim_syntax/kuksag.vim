let b:current_syntax = "kuksag"

" Integer with - + or nothing in front
syn match Number '\d\+j'
syn match Number '[-+]\d\+j'

" Floating point number with decimal no E or e
syn match Number '[-+]\d\+\.\d*j'

" Floating point like number with E and no decimal point (+,-)
syn match Number '[-+]\=\d[[:digit:]]*[eE][\-+]\=\d\+j'
syn match Number '\d[[:digit:]]*[eE][\-+]\=\d\+j'

" Floating point like number with E and decimal point (+,-)
syn match Number '[-+]\=\d[[:digit:]]*\.\d*[eE][\-+]\=\d\+j'
syn match Number '\d[[:digit:]]*\.\d*[eE][\-+]\=\d\+j'

hi def link Number Type
