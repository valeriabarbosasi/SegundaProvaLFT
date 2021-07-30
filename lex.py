import ply.lex as lex


# List of token names.   This is always required
tokens = (
 'AND',
 'OR',
 'NOR',
 'NOT',
 'IMPLIES',
 'EQUIVALENT',
 'NAND',
 'XOR',
 'LPAREN',
 'RPAREN',
 'TRUE',
 'FALSE',)

# Regular expression rules for simple tokens

t_AND = r'&&'
t_OR = r'\|\|'
t_NOR = r'\!\|'
t_NOT = r'\!'
t_IMPLIES = r'->'
t_EQUIVALENT = r'=='
t_NAND = r'\!\&'
t_XOR = r'\|'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_TRUE = r'true'
t_FALSE = r'false'

def t_NUMBER(t):
   r'\d+'
   t.value = int(t.value)
   return t

# Error handling rule
def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)

t_ignore = ' \t'

def t_newline(t):    
  r'\n+'    
  t.lexer.lineno += len(t.value)

# Build the lexer
lexer = lex.lex()

# Test it out
data = '''( ) -> true false || <-> !&
!| ! | && =='''

# Give the lexer some input
lexer.input(data)
