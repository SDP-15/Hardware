

#define fsrPin0 A0// the FSR and 10K pulldown are connected to a0
#define fsrPin1 A1
#define fsrPin2 A2

#define fsrPin3 A3
#define fsrPin4 A4
#define fsrPin5 A5


// #define fsrPin6 A6
// #define fsrPin7 A7




void setup() {
  Serial.begin(9600);
    }


void loop(void) {
  int back_top_left = analogRead(fsrPin0);  
 
  Serial.print("back top left = ");
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
 
  Serial.print("back top right = ");
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
 
  Serial.print("bottom middle = ");
  Serial.print(bottom_middle);     // print the raw analog reading
 
  if (bottom_middle < 50) {
    Serial.println(" - No pressure");
  } else if (bottom_middlebottom_middlebottom_middle < 500) {
    Serial.println(" - Light touch");
  } else if (bottom_middlebottom_middle < 700) {
    Serial.println(" - Light squeeze");
  } else if (bottom_middle < 900) {
    Serial.println(" - Medium squeeze");
  } else {
    Serial.println(" - Big squeeze");
  }
  int seat_back_middle    = analogRead(fsrPin3);  
 
  Serial.print("seat back middle = ");
  Serial.print(fsrReading3);     // print the raw analog reading
 
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
 
  Serial.print("seat front left = ");
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
 
  Serial.print("seat front right = ");
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
//   int fsrReading6   = analogRead(fsrPin6);  
 
//   Serial.print("Analog reading6 = ");
//   Serial.print(fsrReading6);     // print the raw analog reading
 
//   if (fsrReading6 < 50) {
//     Serial.println(" - No pressure");
//   } else if (fsrReading6 < 500) {
//     Serial.println(" - Light touch");
//   } else if (fsrReading6 < 700) {
//     Serial.println(" - Light squeeze");
//   } else if (fsrReading6 < 900) {
//     Serial.println(" - Medium squeeze");
//   } else {
//     Serial.println(" - Big squeeze");
//   }
//   int fsrReading7    = analogRead(fsrPin7);  
 
//   Serial.print("Analog reading7 = ");
//   Serial.print(fsrReading7);     // print the raw analog reading
 
//   if (fsrReading7 < 50) {
//     Serial.println(" - No pressure");
//   } else if (fsrReading7 < 500) {
//     Serial.println(" - Light touch");
//   } else if (fsrReading7 < 700) {
//     Serial.println(" - Light squeeze");
//   } else if (fsrReading7 < 900) {
//     Serial.println(" - Medium squeeze");
//   } else {
//     Serial.println(" - Big squeeze");
//   }
//  int fsrReading9    = analogRead(fsrPin9);  
// 
//  Serial.print("Analog reading9 = ");
//  Serial.print(fsrReading9);     // print the raw analog reading
// 
//  if (fsrReading9 < 10) {
//    Serial.println(" - No pressure");
//  } else if (fsrReading9 < 500) {
//    Serial.println(" - Light touch");
//  } else if (fsrReading9 < 700) {
//    Serial.println(" - Light squeeze");
//  } else if (fsrReading9  < 900) {
//    Serial.println(" - Medium squeeze");
//  } else {
//    Serial.println(" - Big squeeze");
//  }
  delay(50);
}
