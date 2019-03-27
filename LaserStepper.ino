#include <Stepper.h>

Stepper horizontal = Stepper(64, 3, 5, 4, 6);
Stepper vertical = Stepper(64, 10, 12, 11, 13);

char in, pos;
int sH = 0, sV = 0;

void TopLeft();
void TopRight();
void BottomLeft();
void BottomRight();
void Center();

void setup()
{
  Serial.begin(9600);

  pinMode(11, OUTPUT);
  
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

    in = Serial.read();
    
    if (in == 'q')
    {
      if (pos != 'q')
        TopLeft();
    }
    else if (in == 'p')
    {
      if (pos != 'p')
        TopRight();
    }
    else if (in == 'z')
    {
      //BottomLeft();
    }
    else if (in == 'm')
    {
      //BottomRight();
    }
  }
  delay(1);
}

void TopLeft()
{
  if (sH < 100)
  {
    for (;sH <= 100; sH += 1)
    {
      horizontal.step(1);
    }
  }

  if (sH > 100)
  {
    for (;sH >= 100; sH -= 1)
    {
      horizontal.step(-1);
    } 
  }

  if (sV < 100)
  {
    for (;sV <= 100; sV += 1)
    {
      vertical.step(1);
    } 
  }

  if (sV > 100)
  {
    for (;sV >= 100; sV -= 1)
    {
      vertical.step(-1);
    } 
  }

  pos = 'q';
  
}

void TopRight()
{
  if (sH > -100)
  {
    for (;sH >= -100; sH -= 1)
    {
      horizontal.step(-1);
    }
  }

  if (sH < -100)
  {
    for (;sH <= -100; sH += 1)
    {
      horizontal.step(1);
    } 
  }

  if (sV < 100)
  {
    for (;sV <= 100; sV += 1)
    {
      vertical.step(1);
    } 
  }

  if (sV > 100)
  {
    for (;sV >= 100; sV -= 1)
    {
      vertical.step(-1);
    } 
  }

  pos = 'p';
  
}

void BottomLeft()
{
  if (sH > -100)
  {
    for (;sH >= -100; sH -= 1)
    {
      horizontal.step(-1);
    }
  }

  if (sH < -100)
  {
    for (;sH <= -100; sH += 1)
    {
      horizontal.step(1);
    } 
  }

  if (sV < 100)
  {
    for (;sV <= 100; sV += 1)
    {
      vertical.step(1);
    } 
  }

  if (sV > 100)
  {
    for (;sV >= 100; sV -= 1)
    {
      vertical.step(-1);
    } 

  pos = 'p'; 
}
