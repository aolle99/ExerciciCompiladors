import sys
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
#from TreeVisitor import TreeVisitor
from EvalVisitor import EvalVisitor
input_stream = FileStream(sys.argv[1], encoding='utf-8')
lexer = ExprLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = ExprParser(token_stream)
tree = parser.root() 
#visitor = TreeVisitor()
#visitor.visit(tree)

eval = EvalVisitor()
result = eval.visit(tree)
