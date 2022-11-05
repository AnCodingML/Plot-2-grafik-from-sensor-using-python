//setting pin sensor jarak
const int trigPin = A3;
const int echoPin = A2;

const int trigPin1 = A0;
const int echoPin1 = A1;



void setup() {
  Serial.begin(9600);
  pinMode(trigPin, OUTPUT);
  pinMode(trigPin1, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(echoPin1, INPUT);
}


void loop(){
  long duration, cm;
  long duration1, cm1;

  pinMode(trigPin, OUTPUT);
  
  digitalWrite(trigPin, LOW);
     
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  
  delayMicroseconds(5);
  digitalWrite(trigPin, LOW);
  

  pinMode(echoPin, INPUT);
  
  duration = pulseIn(echoPin, HIGH);

  pinMode(trigPin1, OUTPUT);
  digitalWrite(trigPin1, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin1, HIGH);
  delayMicroseconds(5);
  digitalWrite(trigPin1, LOW);
  pinMode(echoPin1, INPUT);
  duration1 = pulseIn(echoPin1, HIGH);

  
  cm = microsecondsToCentimeters(duration);
  cm1 = microsecondsToCentimeters(duration1);

  Serial.println(cm);


  Serial.println(cm1);
  


  delay(100);

  
  
}
long microsecondsToCentimeters(long microseconds){
  return microseconds/29/2;
}
