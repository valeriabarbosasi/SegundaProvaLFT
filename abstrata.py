from abc import abstractmethod
from abc import ABCMeta

class Exp(metaclass=ABCMeta):
 @abstractmethod
 def accept(self, Visitor):
  pass

#################################
#CONCRETA
#################################
class ExpImplies(Exp):
 def __init__(self, exp, exp1):
  self.exp = exp
  self.exp1 = exp1
def accept(self, Visitor):
 Visitor.visitExpImplies(self)

class ExpEquivalent(Exp):
 def __init__(self, exp, exp1):
  self.exp = exp
  self.exp1 = exp1
 def accept(self, Visitor):
  Visitor.visitExpEquivalent(self) 

class Exp_Exp1(Exp):
 def __init__(self, exp1):
  self.exp1 = exp1
 def accept(self, Visitor):
  Visitor.visitExp_Exp1(self)

class Exp1Or(Exp):
 def __init__(self, exp1, exp2):
  self.exp1 = exp1
  self.exp2 = exp2
 def accept(self, Visitor):
  Visitor.visitExp1Or(self)

class Exp1Nor(Exp):
 def __init__(self, exp1, exp2):
  self.exp1 = exp1
  self.exp2 = exp2
 def accept(self, Visitor):
  Visitor.visitExp1Nor(self)

class Exp1_Exp2(Exp):
 def __init__(self, exp2):
  self.exp2 = exp2
 def accept(self, Visitor):
  Visitor.visitExp_Exp2(self)

class Exp2Xor(Exp):
 def __init__(self, exp2, exp3):
  self.exp2 = exp2
  self.exp3 = exp3
 def accept(self, Visitor):
  Visitor.visitExp2Xor(self)

class Exp2_Exp3(Exp):
 def __init__(self, exp3):
  self.exp3 = exp3
 def accept(self, Visitor):
  Visitor.visitExp2_Exp3(self)

class Exp3And(Exp):
 def __init__(self, exp3, exp4):
  self.exp3 = exp3
  self.exp4 = exp4
 def accept(self, Visitor):
  Visitor.visitExp3And(self)

class Exp3Nand(Exp):
 def __init__(self, exp3, exp4):
  self.exp3 = exp3
  self.exp4 = exp4
 def accept(self, Visitor):
  Visitor.visitExp3Nand(self) 

class Exp3_Exp4(Exp):
 def __init__(self, exp4):
  self.exp4 = exp4
 def accept(self, Visitor):
  Visitor.visitExp3_Exp4(self)

class Exp4Not(Exp):
 def __init__(self, exp4):
  self.exp4 = exp4
 def accept(self, Visitor):
  Visitor.visitExp4Not(self)

class Exp4_Exp5(Exp):
 def __init__(self, exp5):
  self.exp5 = exp5
 def accept(self, Visitor):
  Visitor.visitExp4_Exp5(self)

class Exp5Parentesis(Exp):
 def __init__(self, exp5):
  self.exp5 = exp5
 def accept(self, Visitor):
  Visitor.visitExp5Parentesis(self)

class Exp5True(Exp):
 def accept(self, Visitor):
  Visitor.visitExp5True(self)

class Exp5False(Exp):
 def accept(self, Visitor):
  Visitor.visitExp5False(self)


class Visitor():

 def visitExpImplies(self, expImplies):
  expImplies.exp1.accept(self)
  print ('->')
  expImplies.exp2.accept(self)

 def visitExpEquivalent(self, expEquivalent):
  expEquivalent.exp1.accept(self)
  print ('==')
  expEquivalent.exp2.accept(self)

  def visitExp3Nand(self, exp3Nand):
   exp3Nand.exp1.accept(self)
   print ('!&')
   exp3Nand.exp2.accept(self)

  def visitExp1Or(self, exp1Or):
   exp1Or.exp1.accept(self)
   print ('||')
   exp1Or.exp2.accept(self) 

  def visitExp1Nor(self, exp1Nor):
   exp1Nor.exp1.accept(self)
   print ('!|')
   exp1Nor.exp2.accept(self)

  def visitExp3And(self, exp3And):
   exp3And.exp1.accept(self)
   print ('&&')
   exp3And.exp2.accept(self)

  def visitExp2Xor(self, exp2Xor):
   exp2Xor.exp1.accept(self)
   print ('|')
   exp2Xor.exp2.accept(self)

  def visitExp4Not(self, exp4Not):
   print ('!')
   Exp4Not.exp2.accept(self)
  
  def visitExp5Parentesis(self, exp5Parentesis):
   print ('(')
   exp5Parentesis.exp2.accept(self)
   print (')')

  def visitExp5True(self, exp5True):
   print ('True') 

  def visitExp5False(self, exp5False):
   print ('False')