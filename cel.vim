" Vim syntax file
" Language: Celestia Star Catalogs

if exists("b:current_syntax")
  finish
endif

let b:current_syntax = "cel"
syn keyword celBlockCmd RA Dec SpectralType Mass Distance AbsMag
syn match celNumber '\d\+'
syn match celNumber '[-+]\d\+'
syn match celNumber '[-+]\d\+\.\d*'
syn match celNumber '\d\+\.\d*'

syn match celString '"*"'

syn region celString start='"' end='"' contained fold

syn region celDescBlock start="{" end="}" fold transparent contains=celNumber,celBlockCmd,celString

hi num ctermfg=DarkRed
hi num ctermbg=Blue

hi string ctermfg=LightGreen
hi string ctermbg=Magenta

hi def link celBlockCmd    Statement
hi def link celNumber	   num
hi def link celString      string
