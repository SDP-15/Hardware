

#define fsrPin0 A0// the FSR and 10K pulldown are connected to a0
#define fsrPin1 A1
#define fsrPin2 A2

#define fsrPin3 A3
#define fsrPin4 A4
#define fsrPin5 A5


#define fsrPin6 A6
#define fsrPin7 A7




void setup() {
  Serial.begin(9600);
    }


void loop(void) {
  int fsrReading0 = analogRead(fsrPin0);  
 
  Serial.print("Analog reading0 = ");
  Serial.print(fsrReading0);     // print the raw analog reading
 
  if (fsrReading0 < 50) {
    Serial.println(" - No pressure");
  } else if (fsrReading0 < 500) {
    Serial.println(" - Light touch");
  } else if (fsrReading0 < 700) {
    Serial.println(" - Light squeeze");
  } else if (fsrReading0 < 900) {
    Serial.println(" - Medium squeeze");
  } else {
    Serial.println(" - Big squeeze");
  }
  
  
  int fsrReading1    = analogRead(fsrPin1);  
 
  Serial.print("Analog reading1 = ");
  Serial.print(fsrReading1);     // print the raw analog reading
 
  if (fsrReading1 < 50) {
    Serial.println(" - No pressure");
  } else if (fsrReading1 < 500) {
    Serial.println(" - Light touch");
  } else if (fsrReading1 < 700) {
    Serial.println(" - Light squeeze");
  } else if (fsrReading1 < 900) {
    Serial.println(" - Medium squeeze");
  } else {
    Serial.println(" - Big squeeze");
  }
  int fsrReading2    = analogRead(fsrPin2);  
 
  Serial.print("Analog reading2 = ");
  Serial.print(fsrReading2);     // print the raw analog reading
 
  if (fsrReading2 < 50) {
    Serial.println(" - No pressure");
  } else if (fsrReading2 < 500) {
    Serial.println(" - Light touch");
  } else if (fsrReading2 < 700) {
    Serial.println(" - Light squeeze");
  } else if (fsrReading2 < 900) {
    Serial.println(" - Medium squeeze");
  } else {
    Serial.println(" - Big squeeze");
  }
  int fsrReading3    = analogRead(fsrPin3);  
 
  Serial.print("Analog reading3 = ");
  Serial.print(fsrReading3);     // print the raw analog reading
 
  if (fsrReading3 < 50) {
    Serial.println(" - No pressure");
  } else if (fsrReading3 < 500) {
    Serial.println(" - Light touch");
  } else if (fsrReading3 < 700) {
    Serial.println(" - Light squeeze");
  } else if (fsrReading3 < 900) {
    Serial.println(" - Medium squeeze");
  } else {
    Serial.println(" - Big squeeze");
  }
  int fsrReading4    = analogRead(fsrPin4);  
 
  Serial.print("Analog reading4 = ");
  Serial.print(fsrReading4);     // print the raw analog reading
 
  if (fsrReading4 < 50) {
    Serial.println(" - No pressure");
  } else if (fsrReading4 < 500) {
    Serial.println(" - Light touch");
  } else if (fsrReading4 < 700) {
    Serial.println(" - Light squeeze");
  } else if (fsrReading4 < 900) {
    Serial.println(" - Medium squeeze");
  } else {
    Serial.println(" - Big squeeze");
  }
  int fsrReading5    = analogRead(fsrPin5);  
 
  Serial.print("Analog reading5 = ");
  Serial.print(fsrReading5);     // print the raw analog reading
 
  if (fsrReading5 < 50) {
    Serial.println(" - No pressure");
  } else if (fsrReading5 < 500) {
    Serial.println(" - Light touch");
  } else if (fsrReading5 < 700) {
    Serial.println(" - Light squeeze");
  } else if (fsrReading5 < 900) {
    Serial.println(" - Medium squeeze");
  } else {
    Serial.println(" - Big squeeze");
  }
  int fsrReading6   = analogRead(fsrPin6);  
 
  Serial.print("Analog reading6 = ");
  Serial.print(fsrReading6);     // print the raw analog reading
 
  if (fsrReading6 < 50) {
    Serial.println(" - No pressure");
  } else if (fsrReading6 < 500) {
    Serial.println(" - Light touch");
  } else if (fsrReading6 < 700) {
    Serial.println(" - Light squeeze");
  } else if (fsrReading6 < 900) {
    Serial.println(" - Medium squeeze");
  } else {
    Serial.println(" - Big squeeze");
  }
  int fsrReading7    = analogRead(fsrPin7);  
 
  Serial.print("Analog reading7 = ");
  Serial.print(fsrReading7);     // print the raw analog reading
 
  if (fsrReading7 < 50) {
    Serial.println(" - No pressure");
  } else if (fsrReading7 < 500) {
    Serial.println(" - Light touch");
  } else if (fsrReading7 < 700) {
    Serial.println(" - Light squeeze");
  } else if (fsrReading7 < 900) {
    Serial.println(" - Medium squeeze");
  } else {
    Serial.println(" - Big squeeze");
  }
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
