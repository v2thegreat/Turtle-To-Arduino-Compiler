from .commands import intCommandsFull, intCommandsShort, nonValueCommands, arduinoCode
from .sourceCode import sourcecode
from os import mkdir

class turtleCommandsClass():

    def __init__(self, turtleCode=''):
        """
        A python class to compile turtle code and convert it to arduino code
        """
        self.turtleCode=turtleCode.lower() #Converting the entire code to lowercase so that it can be formatted
        self.__formatCommands()            #Converting the commands to work better


    def __formatCommands(self) -> None:
        """
        A function to format the turtle commands
        """
        l=self.turtleCode.split() #Getting individual words
        self.turtleCommandsLst=[] #Creating a list to save commands
        for x in enumerate(l):

            turtleCommandsClass.__checkTurtleSyntax(x[1]) #Checking each items format and raising errors when they're incorrect
            if turtleCommandsClass.__isIntTurtleCommand(x[1]):
                self.turtleCommandsLst.append('{0} {1}'.format(x[1], l[x[0]+1]))
            if turtleCommandsClass.__isNonValueCommand(x[1]):
                self.turtleCommandsLst.append(x[1])

            #continuing if the item is an integer
            if x[1].isdigit() or x[1].isdecimal():
                continue


    @staticmethod
    def __isNonValueCommand(cmd) -> bool:
        """
        checking if a command is a non-value command
        """
        return cmd in nonValueCommands

    @staticmethod
    def __isIntTurtleCommand(cmd) -> bool:
        """
        checking if a command is either a short form or a regular int command
        """
         
        ch1 = turtleCommandsClass.__isShortLengthIntTurtleCommand(cmd) 
        ch2 = turtleCommandsClass.__isFullLengthIntTurtleCommand(cmd)
        return ch1 or ch2

    @staticmethod
    def __isFullLengthIntTurtleCommand(cmd) -> bool:
        """
        checking if a command is long command
        """
        return cmd in intCommandsFull

    @staticmethod
    def __isShortLengthIntTurtleCommand(cmd) -> bool:
        """
        checking if a command is short command
        """
        return cmd in intCommandsShort

    @staticmethod
    def __checkTurtleSyntax(cmd) -> None:
        """
        function to check the turtle syntax
        """
        ch1 = turtleCommandsClass.__isIntTurtleCommand(cmd) #cmd in intCommandsShort
        ch3 = turtleCommandsClass.__isNonValueCommand(cmd) #cmd in nonValueCommands
        ch4 = cmd.isdigit() or cmd.isdecimal()
        if not (ch1 or ch3 or ch4):
            raise SyntaxError('Invalid Command: {0} not understood'.format(cmd))

    @property
    def arduino_mainloop(self) -> str:
        """
        a property to get mainloop code
        """
        code=''
        for x in self.turtleCommandsLst:
            isIn_intCommandsFull=x.split()[0] in intCommandsFull
            isIn_intCommandsShort=x.split()[0] in intCommandsShort
            isIn_nonValueCommands=x.split()[0] in nonValueCommands

            if isIn_intCommandsFull or isIn_intCommandsShort:
                code += arduinoCode[x.split()[0]] + '({0});\n\t'.format(x.split()[1])

            if isIn_nonValueCommands:
                code += arduinoCode[x.split()[0]]+'();\n\t'

        return code[:-2]

    @property
    def arduinocode(self) -> str:
        """
        a property to get the arduno code
        """
        arduinoSourceCode = sourcecode
        arduinoLoopCode = self.arduino_mainloop
        arduinoSourceCode = arduinoSourceCode.replace("//1650--TENNIS", arduinoLoopCode)
        return arduinoSourceCode

    def save_arduino_code(self, fileName='Output.ino'):
        """
        function to save the arduino code into a file
        """
        folder = fileName.split('.')[0]
        #mkdir(folder)
        try:
        	mkdir(folder)
        except FileExistsError:
        	pass
        open("\\".join([folder,fileName]),'w').write(self.arduinocode)

if __name__ == '__main__':
    s='fd 5 rt 15 ' 		#This is a test command
    t=turtleCommandsClass(turtleCode=s).save_arduino_code()