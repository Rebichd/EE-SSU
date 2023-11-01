#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <ArduinoJson.h>  // must be installed 
#include <WiFiClientSecure.h>
#include "sendRequest.h"

//Function Declartions:
void grabTime();
void pushToSite();


const char* ssid     = "Verizon-SM-G960U-97FC";//"DARE";
const char* password = "lhik780*";//"rebichmotherfucker";

//This is for getting the time
String TimeURL = "https://timeapi.io/api/Time/current/zone?timeZone=America/Los_Angeles";
DynamicJsonDocument doc(1024);

//This is the URL parameters that will be used to push sensor data to website
String myURL     = "https://danielrebich.000webhostapp.com/data.php"; //this is the first part of the full URL to be sent
String dataNodeTemp   = "?nodeID=node_1&nodeTemp="; // specifies that we refering to node_1 and sending temp (temp value not here currently)
u_int8_t tempValue = 0; //sets up tempValue as an unsigned 8 bit int
String dataHumi = "&nodeHumi="; //specifies the next part of the URL that will refers to the humidity
u_int8_t flameValue = 0; //sets up humiValue as an unsigned 8 bit int
String dataTime   = "&nodeTime=";//2022-10-25T20:44:11.4055468"; //this is the final segment of the string // this will be swapped out with the actual time

//Define button and sensors variable names
int pushButton = D1;
int tempSensor = A0;
int flameSensor = D0;
float tempInDegrees = 0;
String mytime;

void setup() {
  Serial.begin(9600); //set baud rate to use serial monitor
  delay(10); // just a short delay
  Serial.println("");
  
  // (A) Start connecting to the WiFI
  Serial.println("Connecting to WiFi"); 
  WiFi.begin(ssid, password); // Connection to WiFi Starts until status()=WL_CONNECTED
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(100);
    Serial.print("."); // waiting to get connected
  }

  // Details of the connection
  connectionDetails();

  //Setup for pins of sensors and button
  pinMode(pushButton, INPUT); //Sets pushButton(D1) as an input pin that will be used for switch
  pinMode(tempSensor, INPUT); //Set tempSensor(A0) as an input pin for analog temp sensor
  pinMode(flameSensor, INPUT); //Set flameSensor(D0) as an input pin for digital flame sensor
}

void loop() {
  //Read button and sensor values
  int buttonState = digitalRead(pushButton);
  flameValue = digitalRead(flameSensor);
  tempValue = analogRead(tempSensor);

  tempValue = tempValue * (3.3 / 1023)*10; //to convert the analog readings of the ADC to degress

  if(buttonState){
    Serial.println("Button has been pressed");//for testing 
    Serial.print("The read Temp is: "); Serial.println(tempInDegrees);
    Serial.print("The read Flame is: "); Serial.println(flameValue);
    grabTime(); //This is the function is to GET time from timeapi.io
    pushToSite(); //This is the function to push the data with timestamp to my database

    delay(30000); //30 second delay between REQUEST to servers
    Serial.println("I have made it past the grabTime and putToSite function calls");
  }
  
}

void grabTime(){
  if (WiFi.status() == WL_CONNECTED){
    WiFiClientSecure client;
    client.setInsecure();
    HTTPClient https;

    String fullUrl = TimeURL; // preparing the full URL
    Serial.println("Requesting: --> " + fullUrl);

    if (https.begin(client, fullUrl)) { // start the connection 1=started / 0=failed
      
      int httpCode = https.GET(); // choose GET or POST method
      //int httpCode = https.POST(fullUrl); // need to include URL
     
      Serial.println("Response code <--: " + String(httpCode)); // print response code: e.g.,:200
      
      Serial.println(https.getString());// for testing purposes

      if (httpCode > 0) {
        Serial.println(https.getString()); // this is the content of the get request received
        deserializeJson(doc,https.getString()); // deserialize the JSON file
        /*--- Sample Response ----
        {"year":2022,"month":10,"day":25,"hour":20,"minute":44,"seconds":11,"milliSeconds":405,
        "dateTime":"2022-10-25T20:44:11.4055468","date":"10/25/2022","time":"20:44",
        "timeZone":"America/Los_Angeles","dayOfWeek":"Tuesday","dstActive":true}
        ------------------------ */
        deserializeJson(doc,https.getString()); // deserialize the JSON format into keys and values
        String temp = doc["dateTime"]; // get the value associated with the dataTime key         //i added the second equal sign when forcing the string declaration to global
        mytime = temp;
        Serial.println(temp); // soomething like 2022-10-25T21:03:44.1790514
      }

      https.end(); // end of request
    
    } else {
        Serial.printf("[HTTPS] Unable to connect\n");
    }
  }  
}

void pushToSite(){
  if (WiFi.status() == WL_CONNECTED){
    WiFiClientSecure client;
    client.setInsecure();
    HTTPClient https;

    String fullUrl = myURL + dataNodeTemp + tempValue + dataHumi + flameValue + dataTime + mytime; // preparing the full URL
    Serial.println("Requesting: --> " + fullUrl);
    if (https.begin(client, fullUrl)) { // start the connection 1=started / 0=failed
      int httpCode = https.GET(); // choose GET or POST method
      //int httpCode = https.POST(fullUrl); // need to include URL
      
      Serial.println("Response code <--: " + String(httpCode)); // print response code: e.g.,:200
      if (httpCode > 0) {
        //Serial.println(https.getString()); // this is the content of the get request received
      }
    https.end(); // end of request
    }else{
      Serial.printf("[HTTPS] Unable to connect\n");
    }
  }
}
