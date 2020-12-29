import string
from scanner import Scanner
from parser import Parser
from semanticAnalyser import SemanticAnalyser
from codeGenerator import CodeGenerator
import time




class Compiler:
	def __init__(self, fileName):
		self.symbolTable = {}
		self.scanner = Scanner()
		self.parser = Parser()
		self.semanticAnalyser = SemanticAnalyser(self.symbolTable)
		self.codeGenerator = CodeGenerator()
		charStream = open(fileName, "r").read()

		tks = self.scanner.scan(charStream)
		parseTree = self.parser.parse(tks)
		ast = self.parser.generateAST(parseTree)
		
		ast = self.semanticAnalyser.analyse(ast)

		code = self.codeGenerator.generateDC(ast)

		with open("test.txt", "w") as f:
			f.write(code)


if __name__ == "__main__":
	s = time.time()
	# self.symbolTable[stmt[1][2]][0]
	c = Compiler("test.ac")
	print(time.time() - s)
