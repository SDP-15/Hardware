



#define fsrPin0 A0// the FSR and 10K pulldown are connected to a0
#define fsrPin1 A1
#define fsrPin2 A2

#define fsrPin3 A3
#define fsrPin4 A4
#define fsrPin5 A5


// #define fsrPin6 A6
// #define fsrPin7 A7
#include<SoftwareSerial.h>
/*create a object*/
SoftwareSerial bt(2,3); /*(Rx,Tx)*/




void setup() {
  bt.begin(9600);
  Serial.begin(9600);
    }


void loop(void) {
  if(bt.available())
  {
    Serial.write(bt.read());  
  }
  if (Serial.available())
  {
    bt.write(Serial.read());
  }
  int back_top_left = analogRead(fsrPin0);  
 
  Serial.print("reading0 = ");
  Serial.print(back_top_left);     // print the raw analog reading
 
  if (back_top_left < 50) {
    Serial.println(" - No pressure");
  } else if (back_top_left < 500) {
    Serial.println(" - Light touch");
  } else if (back_top_left < 700) {
    Serial.println(" - Light squeeze");
  } else if (back_top_left < 900) {
    Serial.println(" - Medium squeeze");
  } else {
    Serial.println(" - Big squeeze");
  }
  
  
  int back_top_right    = analogRead(fsrPin1);  
 
  Serial.print("reading1 = ");
  Serial.print(back_top_right);     // print the raw analog reading
 
  if (back_top_right < 50) {
    Serial.println(" - No pressure");
  } else if (back_top_right < 500) {
    Serial.println(" - Light touch");
  } else if (back_top_right < 700) {
    Serial.println(" - Light squeeze");
  } else if (back_top_right < 900) {
    Serial.println(" - Medium squeeze");
  } else {
    Serial.println(" - Big squeeze");
  }
  int bottom_middle    = analogRead(fsrPin2);  
 
  Serial.print("reading2 = ");
  Serial.print(bottom_middle);     // print the raw analog reading
 
  if (bottom_middle < 50) {
    Serial.println(" - No pressure");
  } else if (bottom_middle < 500) {
    Serial.println(" - Light touch");
  } else if (bottom_middle < 700) {
    Serial.println(" - Light squeeze");
  } else if (bottom_middle < 900) {
    Serial.println(" - Medium squeeze");
  } else {
    Serial.println(" - Big squeeze");
  }
  int seat_back_middle    = analogRead(fsrPin3);  
 
  Serial.print("reading3 = ");
  Serial.print(seat_back_middle);     // print the raw analog reading
 
  if (seat_back_middle < 50) {
    Serial.println(" - No pressure");
  } else if (seat_back_middle < 500) {
    Serial.println(" - Light touch");
  } else if (seat_back_middle < 700) {
    Serial.println(" - Light squeeze");
  } else if (seat_back_middle < 900) {
    Serial.println(" - Medium squeeze");
  } else {
    Serial.println(" - Big squeeze");
  }
  int seat_front_left    = analogRead(fsrPin4);  
 
  Serial.print("reading4 = ");
  Serial.print(seat_front_left);     // print the raw analog reading
 
  if (seat_front_left < 50) {
    Serial.println(" - No pressure");
  } else if (seat_front_left < 500) {
    Serial.println(" - Light touch");
  } else if (seat_front_left < 700) {
    Serial.println(" - Light squeeze");
  } else if (seat_front_left < 900) {
    Serial.println(" - Medium squeeze");
  } else {
    Serial.println(" - Big squeeze");
  }
  int seat_front_right    = analogRead(fsrPin5);  
 
  Serial.print("reading5 = ");
  Serial.print(seat_front_right);     // print the raw analog reading
 
  if (seat_front_right < 50) {
    Serial.println(" - No pressure");
  } else if (seat_front_right < 500) {
    Serial.println(" - Light touch");
  } else if (seat_front_right < 700) {
    Serial.println(" - Light squeeze");
  } else if (seat_front_right < 900) {
    Serial.println(" - Medium squeeze");
  } else {
    Serial.println(" - Big squeeze");
  }
  
}
