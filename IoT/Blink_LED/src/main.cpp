//--------------------
// Title: Blink_LED
//--------------------
// Program Detail:
//--------------------
// Purpose: Continuously blinks an LED at a constant speed based on delay_speed_normal variable. If user enters "A" then speed of 
//          ON/OFF cycle is increased to delay_speed_fast variable. If user enters "B" then speed of ON/OFF cycle is decreased
//          to delay_speed_slow variable. User can also enter "reset" to go back to original speed operation.
// Inputs: Terminal
// Outputs: Terminal, GPIO2(LED)
// Date: Sept. 23, 2023 - 1:45PM
// Compiler: Arduino IDE 2.2.1
// Author: Daniel Rebich
// Versions:
//      V1 - Original Iteration

//--------------------
// File Dependencies: NONE
//--------------------
#include <Arduino.h>
//--------------------
// Main Program
//--------------------
const int D2 = 2;
int delay_speed_normal = 1000;
int delay_speed_slow = 2000;
int delay_speed_fast = 100;
int delay_amt = delay_speed_normal;

void setup() {
  Serial.begin(9600);
  pinMode(D2, OUTPUT);
  digitalWrite(D2,LOW);
}

void loop() {
  digitalWrite(D2,HIGH);
  delay(delay_amt);
  Serial.println("LED is ON");

  digitalWrite(D2,LOW);
  delay(delay_amt);
  Serial.println("LED is OFF");  
 
  if(Serial.available() > 0){
    String tempVar = Serial.readString();
    tempVar.trim();

    if(tempVar == "A"){
      delay_amt = delay_speed_fast;
    }else if(tempVar == "B"){
      delay_amt = delay_speed_slow;
    }else if(tempVar == "reset"){
      delay_amt = delay_speed_normal;
    }else {
      Serial.println("Input Not Accepted!");
    }
  }
}
