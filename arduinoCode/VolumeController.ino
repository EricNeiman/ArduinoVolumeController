float previousP1 = 0.0;
float previousP2 = 0.0;
float previousP3 = 0.0;

int previousS1 = 0;
int previousS2 = 0;
int previousS3 = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  pinMode(7, INPUT_PULLUP);
  pinMode(6, INPUT_PULLUP);
  pinMode(5, INPUT_PULLUP);
}

float getVoltage(float analogValue) {
  return analogValue * (5.0 / 1023.0);
}

void loop() {
  // put your main code here, to run repeatedly:
  float p1 = getVoltage(analogRead(A0));
  float p2 = getVoltage(analogRead(A1));
  float p3 = getVoltage(analogRead(A2));

  int s1 = digitalRead(7);
  int s2 = digitalRead(6);
  int s3 = digitalRead(5);

  if (
    p1 != previousP1 ||
    p2 != previousP2 ||
    p3 != previousP3 ||
    s1 != previousS1 ||
    s2 != previousS2 ||
    s3 != previousS3
  ) {
    previousP1 = p1;
    previousP2 = p2;
    previousP3 = p3;
    previousS1 = s1;
    previousS2 = s2;
    previousS3 = s3;
    Serial.println(String(previousS1) + " " + String(previousS2) + " " + String(previousS3) + "|" + String(previousP1) + " " + String(previousP2) + " " + String(previousP3));
  }
}
