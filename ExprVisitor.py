# Generated from Expr.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#root.
    def visitRoot(self, ctx:ExprParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#bloc.
    def visitBloc(self, ctx:ExprParser.BlocContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#VarAssigInstr.
    def visitVarAssigInstr(self, ctx:ExprParser.VarAssigInstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#WriteInstr.
    def visitWriteInstr(self, ctx:ExprParser.WriteInstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#IfInstr.
    def visitIfInstr(self, ctx:ExprParser.IfInstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#WhileInstr.
    def visitWhileInstr(self, ctx:ExprParser.WhileInstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#FunctionInstr.
    def visitFunctionInstr(self, ctx:ExprParser.FunctionInstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#MainInstr.
    def visitMainInstr(self, ctx:ExprParser.MainInstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#ReturnInstr.
    def visitReturnInstr(self, ctx:ExprParser.ReturnInstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#MultDivExpr.
    def visitMultDivExpr(self, ctx:ExprParser.MultDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#CallInstr.
    def visitCallInstr(self, ctx:ExprParser.CallInstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#TypesExpr.
    def visitTypesExpr(self, ctx:ExprParser.TypesExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#MesMenExpr.
    def visitMesMenExpr(self, ctx:ExprParser.MesMenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#PowExpr.
    def visitPowExpr(self, ctx:ExprParser.PowExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#comparator.
    def visitComparator(self, ctx:ExprParser.ComparatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#param.
    def visitParam(self, ctx:ExprParser.ParamContext):
        return self.visitChildren(ctx)



del ExprParser