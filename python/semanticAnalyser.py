
class SemanticAnalyser:
	def __init__(self, symbolTable):
		self.symbolTable = symbolTable

	def analyse(self, ast):

		self.populateSymbolTable(ast[1])

		self.visitTypes(ast[2])

		ast = (ast[0], ast[1], self.visitConsistency(ast[2]))

		return ast



	def semanticError(self, code):
		print("Semantic error: " + code)
		quit()

	def populateSymbolTable(self, decls):

		for i in decls:
			if i[1] not in self.symbolTable:
				if i[0] == "FLOATDCL":
					self.symbolTable[i[1]] = ["FNUM", False]
				elif i[0] == "INTDCL":
					self.symbolTable[i[1]] = ["INUM", False]
			else:
				self.semanticError("Symbol " + str(i) + " declared twice")

	def visitConsistency(self, stmts):
		for i in range(len(stmts)):
			a, _ = self.checkConsistency(stmts[i])
			stmts[i] = a
			

		return stmts

	def checkConsistency(self, stmt):


		if stmt[0] == "ASSIGN":
			leftType = self.symbolTable[stmt[1][1]][0]

			rightStmt, rightType = self.checkConsistency(stmt[2])



			if (leftType == "INUM" and rightType == "FNUM"):
				self.semanticError("Cannot convert type float to int")
			elif (leftType == "FNUM" and rightType == "INUM"):
				return ("ASSIGN", stmt[1], ("TOFLOAT", rightStmt)), "FNUM"
			else:
				if leftType == "INUM":
					return ("ASSIGN", stmt[1], rightStmt), leftType
				else:
					return ("ASSIGN", stmt[1], rightStmt), leftType

		elif stmt[0] == "ID":
			return stmt, self.symbolTable[stmt[1]][0]

		elif stmt[0] == "FNUM":
			return stmt, "FNUM"
		elif stmt[0] == "INUM":
			return stmt, "INUM"

		elif stmt[0] in ["PLUS", "MINUS"]:
			leftStmt, leftType = self.checkConsistency(stmt[1])

			rightStmt, rightType = self.checkConsistency(stmt[2])

			if (leftType == "FNUM" and rightType == "INUM"):
				return (stmt[0], leftStmt, ("TOFLOAT", rightStmt)), "FNUM"
			elif (leftType == "INUM" and rightType == "FNUM"):
				return (stmt[0], ("TOFLOAT", leftStmt), rightStmt), "FNUM"
			else:
				return stmt, leftType

		else:
			return stmt, None


	def visitTypes(self, stmts):

		for stmt in stmts:
			self.checkTypes(stmt)


	def checkTypes(self, stmt):
		if stmt[0] == "PRINT":
			if stmt[1][1] not in self.symbolTable:
				self.semanticError("Symbol " + str(stmt) + " has been used before declaration")
			elif not self.symbolTable[stmt[1][1]][1]:
				self.semanticError("Symbol " + str(stmt) + " has been used before assignment")
		elif stmt[0] in ["PLUS", "MINUS"]:
			if stmt[1][0] == "ID":
				if stmt[1][1] not in self.symbolTable:
					self.semanticError("Symbol " + str(stmt) + " has been used before declaration")
				elif not self.symbolTable[stmt[1][1]][1]:
					self.semanticError("Symbol " + str(stmt) + " has been used before assignment")
			self.checkTypes(stmt[2])
			self.checkTypes(stmt[1])
		elif stmt[0] == "ID":
			if stmt[1] not in self.symbolTable:
					self.semanticError("Symbol " + str(stmt) + " has been used before declaration")
			elif not self.symbolTable[stmt[1]][1]:
					self.semanticError("Symbol " + str(stmt) + " has been used before assignment")
		elif stmt[0] == "ASSIGN":
			if stmt[1][1] not in self.symbolTable:
				self.semanticError("Symbol " + str(stmt) + " has been used before declaration")
			elif not self.symbolTable[stmt[1][1]][1]:
				self.symbolTable[stmt[1][1]][1] = True
			self.checkTypes(stmt[2])
