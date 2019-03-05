#include "Cell.h"
#include "Maze.h"

//const int buttonPin = 2;

//int buttonState = 0;
//String searchType = "center";
Maze OUMaze;
unsigned char total = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  //pinMode(buttonPin, INPUT);
  //OUMaze.initializePerimiter();
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.print("Loops = ");
  Serial.print(total, DEC);
  Serial.print("\n");
  ++total;
}
