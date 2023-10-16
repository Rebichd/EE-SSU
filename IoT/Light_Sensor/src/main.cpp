//--------------------
// Title: Light_Sensor
//--------------------
// Program Detail:
//--------------------
// Purpose: 
//          Monitors light intensity levels in Lux. If the Lux<"luxThreshold" then the active buzzer activates. If the Lux>="luxThreshold"
//          the the color RGB LED will change from white to red as the brigthness increases. Lux level is displayed on the terminal screen. 
//          If the user enters "B" then the buzzer will be activated for ~5 seconds to act as a system test.
// Inputs: Terminal, AN0(light sensor)
// Outputs: Terminal, GPIO 0,1,2(RGB LED), GPIO 3(Active Buzzer)
// Date: Sept. 30, 2023 - 6:20PM
// Compiler: VS Studio IDE 1.82.2 , PlatformIO core 6.1.11
// Author: Daniel Rebich
// Versions:
//      V1 - Original Iteration

//--------------------
// File Dependencies: NONE
//--------------------
#include <Arduino.h>
#include <math.h>
//--------------------
// Main Program
//--------------------

//Function Declartions:
int ADCtoLuxConversion(int);
int ADCtoRGBconversion(float);

//Pin Variable Names:
const int redPin = D0;
const int grnPin = D1;
const int bluPin = D2;
const int buzzer = D3;

float readValue = 0; //Value obtained from ADC
float luxValue = 0;

float indoorLightingLevel = 1000; //This assumes the level of light in side a typical room is 1000 Lux
float maxLightLevel = 3000; //this is taken from the lab assignment parametes of being the max avlue to measure
float minLightLevel = 0; //this assumes complete darkness
float luxThreshold = 50; //this is the value which if vbelow will sound the buzzer

float maxADCvalue = 1024;
float minADCvalue = 16;

void setup() {
  Serial.begin(9600);

  //RGB LED and Buzzer Setup
  pinMode(redPin, OUTPUT);
  pinMode(grnPin, OUTPUT);
  pinMode(bluPin, OUTPUT);
  pinMode(buzzer, OUTPUT);
  analogWrite(redPin, 255);
  analogWrite(grnPin, 255);
  analogWrite(bluPin, 255);
  digitalWrite(buzzer, LOW);
}

void loop() {
  readValue = analogRead(A0);
  float voltage = readValue * (3.3/1024) * 1000;

  //turns read value into Lux value
  luxValue = ADCtoLuxConversion(voltage);

  //Prints Lux value to terminal
  Serial.print("The value of the sensor is: "); 
  Serial.print(luxValue);
  Serial.println(" Lux");

  //Change lighting accordingly for light levels(white for low, red for high, gradient)
  analogWrite(grnPin, ADCtoRGBconversion(luxValue));
  analogWrite(bluPin, ADCtoRGBconversion(luxValue));

  //Call a funciton to check whether the light sensor input is below a certain threshold
  if(luxValue < luxThreshold){
    digitalWrite(buzzer, HIGH);//sound buzzer
    analogWrite(grnPin, 255);
    analogWrite(bluPin, 255);
    analogWrite(redPin, 255);
  }
  else{
    digitalWrite(buzzer, LOW);//turn off buzzer
  }

  //look for the user input
  //if User endter "B" then the buzzer needs to sound for 5 seconds
  if(Serial.available() > 0){
    String tempVar = Serial.readString();
    tempVar.trim();

    if(tempVar == "B"){
      Serial.println("Starting System Test!!!");
      digitalWrite(buzzer, HIGH);//sound buzzer for 5 seconds
      delay(5000); //5 second delay
      digitalWrite(buzzer, LOW); //turn buzzer off
      Serial.println("Test Complete!!!");
    }else {
      Serial.println("Input Not Accepted!");
    }
  }

  //1 sec delay before repeat
  delay(1000);
}

int ADCtoLuxConversion(int readValue){
  int convertedValue = 0;
  convertedValue = 2.75 * readValue - 6054;
  if(convertedValue < 0){
    return 0;
  }
  return convertedValue;
}

int ADCtoRGBconversion(float ADCvalue){
  //RGB scale goes from 0 to 255
  //old value - old min / old max - old min     *     new max - new min     + new min
  float RGBvalue = (255 - 0) * ((ADCvalue - 0)/(3021 - 0)) + 0;
  RGBvalue = 255 - RGBvalue;
 
  return RGBvalue;
}
