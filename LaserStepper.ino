#include <Stepper.h>
#include <Math.h>

Stepper horizontal = Stepper(64, 3, 5, 4, 6);
Stepper vertical = Stepper(64, 10, 12, 11, 13);

int sH = 0, sV = 0, x, y;
String in;

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

  horizontal.step(10);
}

void loop()
{ 
  if (Serial.available() > 0)
  {
    in = Serial.readString();
  }

  x = parseDataX(in);
  y = parseDataY(in);
  
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
