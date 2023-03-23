





#define fsrPin0 A0// the FSR and 10K pulldown are connected to a0
#define fsrPin1 A1
#define fsrPin2 A2

#define fsrPin3 A3
#define fsrPin4 A4
#define fsrPin5 A5



#include<SoftwareSerial.h>

/*create a object*/
SoftwareSerial bt(10,11); /*(Rx,Tx)*/




void setup() {
//   /
  pinMode(10,INPUT);
  pinMode(11,OUTPUT);
  bt.begin(9600);
  Serial.begin(9600);

    }


void loop(void) {
  
  int back_top_left = analogRead(fsrPin0);  
 
  bt.print("reading0 = ");
  bt.print(back_top_left);     // print the raw analog reading
 
  if (back_top_left < 50) {
    bt.println(" - No pressure");
  } else if (back_top_left < 500) {
    bt.println(" - Light touch");
  } else if (back_top_left < 700) {
    bt.println(" - Light squeeze");
  } else if (back_top_left < 900) {
    bt.println(" - Medium squeeze");
  } else {
    bt.println(" - Big squeeze");
  }
  
  
  int back_top_right    = analogRead(fsrPin1);  
 
  bt.print("reading1 = ");
  bt.print(back_top_right);     // print the raw analog reading
 
  if (back_top_right < 50) {
    bt.println(" - No pressure");
  } else if (back_top_right < 500) {
    bt.println(" - Light touch");
  } else if (back_top_right < 700) {
    bt.println(" - Light squeeze");
  } else if (back_top_right < 900) {
    bt.println(" - Medium squeeze");
  } else {
    bt.println(" - Big squeeze");
  }
  int bottom_middle    = analogRead(fsrPin2);  
 
  bt.print("reading2 = ");
  bt.print(bottom_middle);     // print the raw analog reading
 
  if (bottom_middle < 50) {
    bt.println(" - No pressure");
  } else if (bottom_middle < 500) {
    bt.println(" - Light touch");
  } else if (bottom_middle < 700) {
    bt.println(" - Light squeeze");
  } else if (bottom_middle < 900) {
    bt.println(" - Medium squeeze");
  } else {
    bt.println(" - Big squeeze");
  }
  int seat_back_middle    = analogRead(fsrPin3);  
 
  bt.print("reading3 = ");
  bt.print(seat_back_middle);     // print the raw analog reading
 
  if (seat_back_middle < 50) {
    bt.println(" - No pressure");
  } else if (seat_back_middle < 500) {
    bt.println(" - Light touch");
  } else if (seat_back_middle < 700) {
    bt.println(" - Light squeeze");
  } else if (seat_back_middle < 900) {
    bt.println(" - Medium squeeze");
  } else {
    bt.println(" - Big squeeze");
  }
  int seat_front_left    = analogRead(fsrPin4);  
 
  bt.print("reading4 = ");
  bt.print(seat_front_left);     // print the raw analog reading
 
  if (seat_front_left < 50) {
    bt.println(" - No pressure");
  } else if (seat_front_left < 500) {
    bt.println(" - Light touch");
  } else if (seat_front_left < 700) {
    bt.println(" - Light squeeze");
  } else if (seat_front_left < 900) {
    bt.println(" - Medium squeeze");
  } else {
    bt.println(" - Big squeeze");
  }
  int seat_front_right    = analogRead(fsrPin5);  
 
  bt.print("reading5 = ");
  bt.print(seat_front_right);     // print the raw analog reading
 
  if (seat_front_right < 50) {
    bt.println(" - No pressure");
  } else if (seat_front_right < 500) {
    bt.println(" - Light touch");
  } else if (seat_front_right < 700) {
    bt.println(" - Light squeeze");
  } else if (seat_front_right < 900) {
    bt.println(" - Medium squeeze");
  } else {
    bt.println(" - Big squeeze");
  }
  delay(1000);

}
