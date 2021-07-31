import ply.yacc as yacc
import numbers
from lex import *

def p_exp(p):
  '''exp : exp IMPLIES exp1
  | exp EQUIVALENT exp1
  | exp1 '''
  if(len(p)==2):
   p[0] = p[1]
  elif (p[2] == '=='):
    
    if((p[1] == 'true') and (p[3] == 'true')):
      p[0] = 'true'
    elif((p[1] == 'false') and (p[3] == 'false')):
      p[0] = 'true'
    else:
      p[0] = 'false'
  else:
    if((p[1] == 'true') and (p[3] == 'false')):
      p[0] = 'false'
    else:
      p[0] = 'true'

def p_exp1(p):
  '''exp1 : exp1 OR exp2
  | exp1 NOR exp2
  | exp2 '''

def p_exp2(p):
  '''exp2 : exp2 XOR exp3
  | exp3 ''' 

def p_exp3(p):
  '''exp3 : exp3 AND exp4
  | exp3 NAND exp4 
  | exp4 '''  

def p_exp4(p):
  '''exp4 : NOT exp4
  | exp5 ''' 

def p_exp5(p):
  '''exp5 : LPAREN exp RPAREN
  | TRUE
  | FALSE ''' 

 
def p_error(p):
  print('Error') 
  
parser = yacc.yacc()
while True:
 try:
     s = input('calc > ')
 except EOFError:
     break
 if not s: continue
 result = parser.parse(s)
 print(result)