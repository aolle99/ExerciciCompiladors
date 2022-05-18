from Stack import Stack

if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
    from .ExprVisitor import ExprVisitor
else:
    from ExprParser import ExprParser
    from ExprVisitor import ExprVisitor


class EvalVisitor(ExprVisitor):
    def __init__(self):
        self.variables = Stack()
        self.functions = {}

    def visitRoot(self, ctx):
        l = list(ctx.getChildren())
        self.visit(l[0])

    def visitBloc(self, ctx):
        l = list(ctx.getChildren())
        for pos in range(len(l)):
            self.visit(l[pos])
            if "return" in self.variables.peek():
                return

    """
    EXPRESSIONS
    """

    def visitMultDivExpr(self, ctx):
        l = list(ctx.getChildren())
        if l[1].getSymbol().type == ExprParser.MULT:
            return self.visit(l[0]) * self.visit(l[2])
        elif l[1].getSymbol().type == ExprParser.DIV:
            return self.visit(l[0]) / self.visit(l[2])
        return 0

    def visitTypesExpr(self, ctx):
        l = list(ctx.getChildren())
        if l[0].getSymbol().type == ExprParser.VAR:
            return int(self.variables.peek()[l[0].getText()])
        else:
            return int(l[0].getText())

    def visitMesMenExpr(self, ctx):
        l = list(ctx.getChildren())
        if l[1].getSymbol().type == ExprParser.MES:
            return self.visit(l[0]) + self.visit(l[2])
        elif l[1].getSymbol().type == ExprParser.MENUS:
            return self.visit(l[0]) - self.visit(l[2])
        return 0

    def visitPowExpr(self, ctx):
        l = list(ctx.getChildren())
        if l[1].getSymbol().type == ExprParser.POW:
            return self.visit(l[0]) ** self.visit(l[2])
        return 0

    """INSTRUCCIONS"""

    def visitVarAssigInstr(self, ctx):
        l = list(ctx.getChildren())

        value = self.visit(l[2])
        self.variables.peek()[l[0].getText()] = value

    def visitWriteInstr(self, ctx):
        l = list(ctx.getChildren())

        print(self.visit(l[1]))

    def visitIfInstr(self, ctx):
        l = list(ctx.getChildren())

        if self.visit(l[1]):
            self.visit(l[3])

    def visitWhileInstr(self, ctx):
        l = list(ctx.getChildren())

        while self.visit(l[1]):
            self.visit(l[3])

    def visitFunctionInstr(self, ctx):
        l = list(ctx.getChildren())

        func_name = l[1].getText()
        i = 3
        params = []
        while l[i].getText() != ')':
            params.append(l[i].getText())
            i += 1

        bloc = l[i + 1]
        self.functions[func_name] = [params, bloc]

    def visitMainInstr(self, ctx: ExprParser.MainInstrContext):
        l = list(ctx.getChildren())
        self.visit(l[1])

    def visitCallInstr(self, ctx):
        l = list(ctx.getChildren())
        func_name = l[0].getText()
        function = self.functions[func_name]
        if function == None:
            raise Exception("La funció no existeix")
        i = 2
        params = []
        while l[i].getText() != ')':
            params.append(self.visit(l[i]))
            i += 1

        if len(params) != len(function[0]):
            raise Exception("Nombre de parametres incorrectes")
        self.variables.push()
        for i in range(len(params)):
            self.variables.peek()[function[0][i]] = params[i]
        self.visit(function[1])
        ret = self.variables.peek()["return"]
        self.variables.pop()
        return ret

    def visitReturnInstr(self, ctx):
        l = list(ctx.getChildren())

        self.variables.peek()["return"] = self.visit(l[1])

    def visitComparator(self, ctx):
        l = list(ctx.getChildren())
        expr1 = l[0]
        comp = l[1]
        expr2 = l[2]

        if comp.getSymbol().type == ExprParser.EQUAL: return self.visit(expr1) == self.visit(expr2)
        if comp.getSymbol().type == ExprParser.DIFF: return self.visit(expr1) != self.visit(expr2)
        if comp.getSymbol().type == ExprParser.GREATER_EQUAL: return self.visit(expr1) >= self.visit(expr2)
        if comp.getSymbol().type == ExprParser.LESS_EQUAL: return self.visit(expr1) <= self.visit(expr2)
        if comp.getSymbol().type == ExprParser.GREATER: return self.visit(expr1) > self.visit(expr2)
        if comp.getSymbol().type == ExprParser.LESS: return self.visit(expr1) < self.visit(expr2)

        return False

    def visitParam(self, ctx):
        l = list(ctx.getChildren())
        return self.visit(l[0])
