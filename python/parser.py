

class Parser:
	def __init__(self):
		return

	def parseError(self, code):
		print("Parse error: " + code)
		quit()

	def parse(self, tokenStream):

		return self.program(tokenStream)

	def program(self, tokenStream):
		return ("PROGRAM", self.declares(tokenStream), self.statements(tokenStream), self.match(tokenStream.pop(0), "$"))

	def statements(self, tokenStream):

		headToken = tokenStream[0]
		if headToken[0] == "ID" or headToken[0] == "PRINT":
			return ("STATEMENTS", self.statement(tokenStream), self.statements(tokenStream))
		elif headToken[0] == "$":
			return
		else:
			self.parseError("Grammar error in STATEMENTS")

	def match(self, token, t):

		if token[0] != t:
			self.parseError("A " + str(token) + " should be a " + t)
		else:
			return token


	def statement(self, tokenStream):

		headToken = tokenStream.pop(0)

		if headToken[0] == "ID":
			
			return ("STATEMENT", headToken, self.match(tokenStream.pop(0), "ASSIGN"), self.value(tokenStream), self.expr(tokenStream))


		elif headToken[0] == "PRINT":

			return ("STATEMENT", headToken, self.match(tokenStream.pop(0), "ID"))


	def value(self, tokenStream):

		headToken = tokenStream.pop(0)

		if headToken[0] in ["ID", "FNUM", "INUM"]:
			return headToken
		else:
			self.parseError(str(headToken) + " can't be interpreted as a value")

	def expr(self, tokenStream):

		if tokenStream[0][0] in ["PLUS", "MINUS"]:
			return ("EXPRESSION", tokenStream.pop(0), self.value(tokenStream), self.expr(tokenStream))
		else:
			return

	def declares(self, tokenStream):
		headToken = tokenStream[0]
		if headToken[0] == "FLOATDCL" or headToken[0] == "INTDCL":
			return ("DECLARES", self.declare(tokenStream), self.declares(tokenStream))
		else:
			return

	def declare(self, tokenStream):

		return ("DECLARE", tokenStream.pop(0), self.match(tokenStream.pop(0), "ID"))


	def generateAST(self, parseTree):

		root = parseTree[0]

		decls = parseTree[1]

		stmts = parseTree[2]

		return ("PROGRAM", self.collapseDeclares(decls), self.collapseStatements(stmts))


	def collapseDeclares(self, declaresTree):
		root = declaresTree[1]

		restOfDecs = declaresTree[2]

		if restOfDecs == None:
			return [(root[1][0], root[2][1])]
		else:
			return [(root[1][0], root[2][1])] + self.collapseDeclares(restOfDecs)

	def collapseStatements(self, stmtsTree):
		root = stmtsTree[1]

		restOfStmts = stmtsTree[2]

		nRoot = ()

		if root[1][0] == "ID":
			nRoot = ("ASSIGN", root[1], self.collapseExpr(root[4:], root[3]))
		elif root[1][0] == "PRINT":
			nRoot = ("PRINT", root[2])

		if restOfStmts == None:
			return [nRoot]
		else:

			return [nRoot] + self.collapseStatements(restOfStmts)

	def collapseExpr(self, exprTree, leftTerm):

		if exprTree[0] == None:
			return leftTerm
		elif exprTree[0][0] == "EXPRESSION":
			if exprTree[0][1][0] in ["MINUS", "PLUS"]:

				return (exprTree[0][1][0], leftTerm, self.collapseExpr(exprTree[0][3:], exprTree[0][2]))

			else:
				return leftTerm

