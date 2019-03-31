#include <Stepper.h>
#include <Math.h>

Stepper horizontal = Stepper(64, 3, 5, 4, 6);
Stepper vertical = Stepper(64, 10, 12, 11, 13);

int sH = 0, sV = 0, x, y;
double thetaX, thetaY;
String in;

double pi = 3.141592653589793238462643383279502884197169399375105820974944592307826;

void setup()
{
  Serial.begin(9600);

  pinMode(11, OUTPUT);

  Serial.setTimeout(10);
  
  for (int i = 3; i <= 13; i++)
  {
    pinMode(i, OUTPUT);
  }

  horizontal.setSpeed(500);
  vertical.setSpeed(500);

  digitalWrite(8, HIGH);
}

void loop()
{ 
  if (Serial.available() > 0)
  {
    in = Serial.readString();
  }

  x = parseDataX(in);
  y = parseDataY(in);

  thetaX = atan(((x - 60) * 0.15385) / 56);
  thetaY = atan(((y - 410) * 0.15385) / 56);

  horizontal.step(( -1 * (thetaX * 350)) - sH);
  sH += ( -1 * (thetaX * 350)) - sH;
  
  delay(1);
}

int parseDataX(String data)
{
  data.remove(data.indexOf("Y"));
  data.remove(data.indexOf("X"), 1);

  return data.toInt();
}

int parseDataY(String data)
{
  data.remove(0, data.indexOf("Y") + 1);
  
  return data.toInt();
}
