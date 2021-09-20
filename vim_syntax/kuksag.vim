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

syn keyword Keywords False      await      else       import     pass
syn keyword Keywords None       break      except     in         raise
syn keyword Keywords True       class      finally    is         return
syn keyword Keywords and        continue   for        lambda     try
syn keyword Keywords as         def        from       nonlocal   while
syn keyword Keywords assert     del        global     not        with
syn keyword Keywords async      elif       if         or         yield

syn match Comments '#.*'
syn match Strings '\'.*\''

hi def link Number Type
hi def link Keywords Constant
hi def link Comments Comment
hi def link Strings Todo
