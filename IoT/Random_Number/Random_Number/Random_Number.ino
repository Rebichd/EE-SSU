//--------------------
// Title: Random_Number
//--------------------
// Program Detail:
//--------------------
// Purpose: Continuously generates random intger numbers between 0-100 every 5 seconds. 
//          Displays the numbers in the terminal
// Inputs: NONE
// Outputs: Terminal, Serial Plotter
// Date: Sept. 23, 2023 - 11:19AM
// Compiler: Arduino IDE 2.2.1
// Author: Daniel Rebich
// Versions:
//      V1 - Original Iteration

//--------------------
// File Dependencies: NONE
//--------------------

//--------------------
// Main Program
//--------------------
void setup() {
  Serial.begin(9600);
  randomSeed(analogRead(0));
}

void loop() {
  int randNumber = random(101);
  Serial.println(randNumber);
  delay(5000);
}
