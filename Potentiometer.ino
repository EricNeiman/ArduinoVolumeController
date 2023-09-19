float v1 = 0.0;
float v2 = 0.0;
float v3 = 0.0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  pinMode(11, INPUT_PULLUP);
  pinMode(12, INPUT_PULLUP);
  pinMode(13, INPUT_PULLUP);
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
}

void loop() {
  String s = switches();
  String p = potentiometers();
  Serial.println(s + "|" + p);
  // Serial.println("-------");
  delay(100);
}

String switches() {
  int left = leftSwitch();
  int middle = middleSwitch();
  int right = rightSwitch();
  String l = String(left);
  String m = String(middle);
  String r = String(right);
  String val = l + " " + m + " " + r;
  return val;
}

int leftSwitch() {
  digitalWrite(4, HIGH);
  int val = digitalRead(13);
  // Serial.println(val);
  return val;
}

int middleSwitch() {
  digitalWrite(3, HIGH);
  int val = digitalRead(12);
  // Serial.println(val);
  return val;
}

int rightSwitch() {
  digitalWrite(2, HIGH);
  int val = digitalRead(11);
  // Serial.println(val);
  return val;
}

String potentiometers() {
  float left = leftPot();
  float middle = middlePot();
  float right = rightPot();
  String l = String(left);
  String m = String(middle);
  String r = String(right);
  String val = l + " " + m + " " + r;
  return val;
}

float leftPot() {
  digitalWrite(7, HIGH);
  int sensorValue1 = analogRead(A3);
  float v1 = sensorValue1 * (5.0 / 1023.0);
  // Serial.print("1: ");
  // Serial.println(v1);
  return v1;
}

float middlePot() {
  digitalWrite(6, HIGH);
  int sensorValue1 = analogRead(A4);
  float v1 = sensorValue1 * (5.0 / 1023.0);
  // Serial.print("1: ");
  // Serial.println(v1);
  return v1;
}

float rightPot() {
  digitalWrite(5, HIGH);
  int sensorValue1 = analogRead(A5);
  float v1 = sensorValue1 * (5.0 / 1023.0);
  // Serial.print("1: ");
  // Serial.println(v1);
  return v1;
}

