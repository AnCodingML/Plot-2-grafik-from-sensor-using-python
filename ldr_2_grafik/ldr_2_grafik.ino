int son = A0;
int sun = A1;
int LDR1 = 0;
int LDR2 = 0;

void setup() 
{
  Serial.begin(9600);
  pinMode(son, INPUT);
  pinMode(sun, INPUT);
}

void loop()
{
  LDR1 = analogRead(son);
  Serial.println(LDR1);
  delay(500);

  LDR2 = analogRead(sun);
  Serial.println(LDR2);
  delay(500);
}
