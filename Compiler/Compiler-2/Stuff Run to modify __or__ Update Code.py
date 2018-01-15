Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> f=open
>>> from os import chdir; chdir(r'D:\Ali Stuff\Coding Things\Hexbot\Compiler\Code'); import pickle; pickle.dump(['forward', 'left', 'right', 'setx', 'sety','setxy', 'setheading', 'arc'], open('intCommandsFull','wb'))
>>> from os import chdir; chdir(r'D:\Ali Stuff\Coding Things\Hexbot\Compiler\Code'); import pickle; pickle.dump(['forward', 'left', 'right', 'setx', 'sety','setxy', 'setheading', 'arc'], open('intCommandsFull.txt','wb'))
>>> pickle.dump(['fd', 'lt','rt', 'seth'], open('intCommandsShort.txt','wb'))
>>> pickle.dump(['penup', 'pendown','hideturtle','showturtle','home'], open('nonValueCommands.txt','wb'))
>>> pickle.dump({
					'forward':'forward', 'fd':'forward',
					'right':'rightTurn', 'rt':'rightTurn',
					'left':'leftTurn', 'lt': 'leftTurn',
					'pendown':'pendown',
					'penup' : 'penup',
					'hideturtle':'hideturtle',
					'showturtle':'showturtle',
					}, open('nonValueCommands.txt','wb'))
>>> pickle.dump({
					'forward':'forward', 'fd':'forward',
					'right':'rightTurn', 'rt':'rightTurn',
					'left':'leftTurn', 'lt': 'leftTurn',
					'pendown':'pendown',
					'penup' : 'penup',
					'hideturtle':'hideturtle',
					'showturtle':'showturtle',
					}, open('arduinoCode.txt','wb'))
>>> pickle.dump(['penup', 'pendown','hideturtle','showturtle','home'], open('nonValueCommands.txt','wb'))
>>> s='''void setup()
{
	MovePin=2;
	TurnPin=3;
	PenLEDPin=4;
	VisibilityPin=5;

	DistanceDelay=1;
	TurnDelay=1;

	pinMode(MovePin, OUTPUT);
	pinMode(TurnPin, OUTPUT);
}

void loop()
{
	//1650--TENNIS
}

void secondsDelay(int s)
{
	delay(1000*s);
	resetBug();
}

void penup()
{
	digitalWrite(PenLEDPin, LOW);
}

void pendown()
{
	digitalWrite(PenLEDPin, HIGH);
}

void showTurtle()
{
	digitalWrite(VisibilityPin, HIGH);
}

void hideTurtle()
{
	digitalWrite(VisibilityPin, LOW);
}

void forward(int distance)
{
	digitalWrite(MovePin, HIGH);
	secondsDelay(DistanceDelay*distance)
	digitalWrite(MovePin, LOW);
}

void leftTurn(int angle)
{
	digitalWrite(TurnPin, HIGH);
	secondsDelay(TurnDelay*angle)
	digitalWrite(TurnPin, LOW);
}

void rightTurn(int angle)
{
	angle=360-angle;
	leftTurn(angle);
}

void turnOnly()
{
	digitalWrite(MovePin, HIGH);
	digitalWrite(TurnPin, LOW);
}

void moveOnly()
{
	digitalWrite(MovePin, LOW);
	digitalWrite(TurnPin,HIGH);
}

void resetBug()
{
	digitalWrite(MovePin, LOW);
	digitalWrite(TurnPin, LOW);
}'''
>>> pickle.dump(s, open('arduinoSourceCode--To Mod.txt','wb'))
>>> arduinoCode = pickle.load(open('arduinoSourceCode--To Mod.txt','rb'))
>>> arduinoCode
'void setup()\n{\n\tMovePin=2;\n\tTurnPin=3;\n\tPenLEDPin=4;\n\tVisibilityPin=5;\n\n\tDistanceDelay=1;\n\tTurnDelay=1;\n\n\tpinMode(MovePin, OUTPUT);\n\tpinMode(TurnPin, OUTPUT);\n}\n\nvoid loop()\n{\n\t//1650--TENNIS\n}\n\nvoid secondsDelay(int s)\n{\n\tdelay(1000*s);\n\tresetBug();\n}\n\nvoid penup()\n{\n\tdigitalWrite(PenLEDPin, LOW);\n}\n\nvoid pendown()\n{\n\tdigitalWrite(PenLEDPin, HIGH);\n}\n\nvoid showTurtle()\n{\n\tdigitalWrite(VisibilityPin, HIGH);\n}\n\nvoid hideTurtle()\n{\n\tdigitalWrite(VisibilityPin, LOW);\n}\n\nvoid forward(int distance)\n{\n\tdigitalWrite(MovePin, HIGH);\n\tsecondsDelay(DistanceDelay*distance)\n\tdigitalWrite(MovePin, LOW);\n}\n\nvoid leftTurn(int angle)\n{\n\tdigitalWrite(TurnPin, HIGH);\n\tsecondsDelay(TurnDelay*angle)\n\tdigitalWrite(TurnPin, LOW);\n}\n\nvoid rightTurn(int angle)\n{\n\tangle=360-angle;\n\tleftTurn(angle);\n}\n\nvoid turnOnly()\n{\n\tdigitalWrite(MovePin, HIGH);\n\tdigitalWrite(TurnPin, LOW);\n}\n\nvoid moveOnly()\n{\n\tdigitalWrite(MovePin, LOW);\n\tdigitalWrite(TurnPin,HIGH);\n}\n\nvoid resetBug()\n{\n\tdigitalWrite(MovePin, LOW);\n\tdigitalWrite(TurnPin, LOW);\n}'
>>> arduinoCode.replace('//1650--TENNIS',self.getArduinoLoopCode())
		return arduinoCode
	
SyntaxError: multiple statements found while compiling a single statement
>>> arduinoCode.replace('//1650--TENNIS',self.getArduinoLoopCode())
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    arduinoCode.replace('//1650--TENNIS',self.getArduinoLoopCode())
NameError: name 'self' is not defined
>>> s='te'
>>> s.replace('te','4')
'4'
\
>>> 
