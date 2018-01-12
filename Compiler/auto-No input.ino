void setup()
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
	secondsDelay(1);
	//1650--TENNIS
	secondsDelay(1);
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
}