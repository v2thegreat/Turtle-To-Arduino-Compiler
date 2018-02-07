from commands import intCommandsFull, intCommandsShort, nonValueCommands, arduinoCode
import sourceCode

class turtleCommandsClass():

	def __init__(self, turtleCode=''):
		self.turtleCode=turtleCode.lower() #Converting the entire code to lowercase
		self.__formatCommands()		#Converting the commands to work better


	def __formatCommands(self):
		l=self.turtleCode.split() #Getting individual words
		self.turtleCommandsLst=[] #Creating a list to save commands
		for x in enumerate(l):
			self.__checkTurtleSyntax(x[1]) #Checking each items format and raising errors when they're incorrect

			#Checking where each item belongs and how to run it
			
			#Checking if the item belongs to int commands list (if it was one above or below)
			if x[1] in intCommandsFull or x[1] in intCommandsShort:
				self.turtleCommandsLst.append('{0} {1}'.format(x[1], l[x[0]+1]))

			#Same thing here
			if x[1] in nonValueCommands:
				self.turtleCommandsLst.append(x[1])

			#continuing if the item is an interger
			if x[1].isdigit() or x[1].isdecimal():
				continue


	def __checkTurtleSyntax(self, command):
		#Checking if command belongs in intCommandsShort
		ch1 = command in intCommandsShort

		#Checking if command belongs in intCommandsFull
		ch2 = command in intCommandsFull

		#Checking if command belongs in nonValueCommands
		ch3 = command in nonValueCommands

		#Checking if the command is actually an integer
		ch4 = command.isdigit() or command.isdecimal()

		#If any of these conditions are true, and raises if none of them work
		if (ch1 or ch2 or ch3 or ch4):
			return None
		else:
			raise SyntaxError('Invalid Command: {0} not understood'.format(command))


	#Method for converting mainloop code to C++ arduino Code
	def getArduinoLoopCode(self):
		code=''
		for x in self.turtleCommandsLst:

			#Assigning Boolean Values to check how they work
			isIn_intCommandsFull=x.split()[0] in intCommandsFull
			isIn_intCommandsShort=x.split()[0] in intCommandsShort
			isIn_nonValueCommands=x.split()[0] in nonValueCommands

			if isIn_intCommandsFull or isIn_intCommandsShort:
				code += arduinoCode[x.split()[0]] + '({0});\n\t'.format(x.split()[1])

			if isIn_nonValueCommands:
				code += arduinoCode[x.split()[0]]+'();\n\t'

		return code[:-2]


	def getArduinoCode(self):
		arduinoSourceCode = sourceCode.getArduinoSourceCode
		arduinoLoopCode = self.getArduinoLoopCode()
		arduinoSourceCode = arduinoSourceCode.replace("//1650--TENNIS", arduinoLoopCode)
		return arduinoSourceCode


	def saveArduinoCode(self, fileName='Output Arduino Code.ino'):
		open(fileName,'w').write(self.getArduinoCode())


	def saveChangesToSourceCode(self, modifiedSourceCode):
		Warning('This has not been tested yet')
		Warning('''Ensure that the lines: '//1650--TENNIS' is present in the comments
				That line is used as a replacement placeholder for easy formatting''')

		if '//1650--TENNIS' not in modifiedSourceCode:
			raise ValueError("Command: //1650--TENNIS not found")

		data=open(modifiedSourceCode, 'r').read()
		pickle.dump(data, open("arduinoSourceCode--To Mod.txt",'wb'))


def main():
	s='fd 5 rt 9'				#input('Enter the Turtle Command')
	t=turtleCommandsClass(turtleCode=s).saveArduinoCode()

if __name__ == '__main__':
	main()