from lex import *
import parser

for tok in lexer:   
  print(tok.type, tok.value, tok.lineno, tok.lexpos)

#parser.parse()