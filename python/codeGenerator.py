
class CodeGenerator:
	def __init__(self):
		pass

	def generateDC(self, ast):

		if ast[0] == "PROGRAM":
			ret = []
			[ret.append(self.generateDC(x)) for x in ast[1]]
			[ret.append(self.generateDC(x)) for x in ast[2]]
			
			return "\n".join(sum(ret,[]))
		elif ast[0] == "ASSIGN":
			return self.generateDC(ast[2]) + ["s" + ast[1][1], "0 k"]
		elif ast[0] == "PLUS":
			return self.generateDC(ast[1]) + self.generateDC(ast[2]) + ["+"]
		elif ast[0] == "MINUS":
			return self.generateDC(ast[1]) + self.generateDC(ast[2]) + ["-"]
		elif ast[0] == "ID":
			return ["l" + ast[1]]
		elif ast[0] == "TOFLOAT":
			return self.generateDC(ast[1]) + ["5 k"]
		elif ast[0] == "PRINT":
			return self.generateDC(ast[1]) + ["p", "si"]
		elif ast[0] == "FNUM":
			return [ast[1]]
		elif ast[0] == "INUM":
			return [ast[1]]
		elif ast[0] == "FLOATDCL":
			return ["5 k", "0.0", "s" + ast[1]]
		elif ast[0] == "INTDCL":
			return ["0 k", "0", "s" + ast[1]]
		else:
			print(ast)