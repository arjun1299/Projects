#include <Servo.h>

#include <Wire.h>


#define sensor A1 // Sharp IR 

#define max_angle 180 //depends what angle it is rotating
Servo s;
int pos=0;
void setup() {
  Serial.begin(9600); // start the serial port
  s.attach(7);
}

void loop() {
  
  // 5v
  if(pos>=max_angle)
  {  pos=0;
      s.write(pos);
      delay(1000);
  } 
  
  s.write(pos);
  float volts = analogRead(sensor)*float(5)/1024;  // value from sensor * (5/1024)  
  float distance = 25.95*pow(volts, -1); // worked out from datasheet graph
  delay(50); // slow down serial port

  pos+=1;

  Serial.println(distance);
  
}
