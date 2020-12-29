import string

class Scanner:
	def __init__(self):
		return

	def scan(self, charStream):

		tokens = []

		charStreamLen = len(charStream)
		i = 0

		lineNumber = 1
		while i < charStreamLen:

			currChar = charStream[i]

			if currChar in [" ", "\t", "\n"]:
				if currChar == "\n":
					lineNumber += 1
				

			elif currChar in string.digits:
				numberChars = ""
				
				while currChar in string.digits + ".":
					
					numberChars += currChar


					i += 1
					if i == charStreamLen:
						break
					else:
						currChar = charStream[i]
				
				i -= 1
				currChar = charStream[i]
				
				if "." in numberChars:
					tokens.append(("FNUM", numberChars))
				else:
					tokens.append(("INUM", numberChars))

			elif currChar == "f":
				tokens.append(("FLOATDCL", "FLOATDCL"))
			elif currChar == "i":
				tokens.append(("INTDCL", "INTDCL"))
			elif currChar == "p":
				tokens.append(("PRINT", "PRINT"))

			elif currChar in string.ascii_lowercase:
				tokens.append(("ID", currChar))

			elif currChar == "=":
				tokens.append(("ASSIGN", "ASSIGN"))

			elif currChar == "+":
				tokens.append(("PLUS", "PLUS"))

			elif currChar == "-":
				tokens.append(("MINUS", "MINUS"))

			else:
				print("Scanner error: unrecognised token '" + currChar + "' on line " + str(lineNumber))
				quit()

			i += 1

			if i == charStreamLen:
				tokens.append(('$', '$'))
				break

		return tokens