int previousS1 = 0;
int previousS2 = 0;
int previousS3 = 0;

int previousClk1 = 0;
int previousDt1 = 0;
int previousSw1 = 0;

int previousClk2 = 0;
int previousDt2 = 0;
int previousSw2 = 0;

int previousClk3 = 0;
int previousDt3 = 0;
int previousSw3 = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(A0, INPUT_PULLUP);
  pinMode(A1, INPUT_PULLUP);
  pinMode(A2, INPUT_PULLUP);

  pinMode(10, INPUT_PULLUP);
  pinMode(9, INPUT_PULLUP);
  pinMode(8, INPUT_PULLUP);
  pinMode(7, INPUT_PULLUP);
  pinMode(6, INPUT_PULLUP);
  pinMode(5, INPUT_PULLUP);
  pinMode(4, INPUT_PULLUP);
  pinMode(3, INPUT_PULLUP);
  pinMode(2, INPUT_PULLUP);
}

void loop() {
  // put your main code here, to run repeatedly:
  int s1 = !digitalRead(A0);
  int s2 = !digitalRead(A1);
  int s3 = !digitalRead(A2);
  int clk1 = digitalRead(10);
  int dt1 = digitalRead(9);
  int sw1 = digitalRead(8);
  int clk2 = digitalRead(7);
  int dt2 = digitalRead(6);
  int sw2 = digitalRead(5);
  int clk3 = digitalRead(4);
  int dt3 = digitalRead(3);
  int sw3 = digitalRead(2);

  if (
    previousS1 != s1 ||
    previousS2 != s2 ||
    previousS3 != s3 ||
    previousClk1 != clk1 ||
    previousDt1 != dt1 ||
    previousSw1 != sw1 ||
    previousClk2 != clk2 ||
    previousDt2 != dt2 ||
    previousSw2 != sw2 ||
    previousClk3 != clk3 ||
    previousDt3 != dt3 ||
    previousSw3 != sw3
  ) {
    previousS1 = s1;
    previousS2 = s2;
    previousS3 = s3;
    previousClk1 = clk1;
    previousDt1 = dt1;
    previousSw1 = sw1;
    previousClk2 = clk2;
    previousDt2 = dt2;
    previousSw2 = sw2;
    previousClk3 = clk3;
    previousDt3 = dt3;
    previousSw3 = sw3;
    String s = "S 1:" + String(s1) + " " + String(s2) + " " + String(s3);
    String r1 = "RE 1:" + String(clk1) + " " + String(dt1) + " " + String(sw1);
    String r2 = "RE 2:" + String(clk2) + " " + String(dt2) + " " + String(sw2);
    String r3 = "RE 3:" + String(clk3) + " " + String(dt3) + " " + String(sw3);

    Serial.println(s + " | " + r1 + " | " + r2 + " | " + r3);
  }
}
