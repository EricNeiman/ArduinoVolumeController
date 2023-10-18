#include <Arduino.h>

int p_p0 = 0;
int print_p0 = 0;
int p_p1 = 0;
int print_p1 = 0;
int p_p2 = 0;
int print_p2 = 0;
int p_clk = 0;
int p_sw = 0;
int p_t0 = 0;
int p_t1 = 0;
int p_t2 = 0;
int p_s1 = 0;
int p_s2 = 0;
int p_s3 = 0;
int p_s5 = 0;
int p_s6 = 0;
int p_s7 = 0;
int p_s8 = 0;

void setup() {
  Serial.begin(9600);
  pinMode(2, INPUT_PULLUP);
  pinMode(3, INPUT_PULLUP);
  pinMode(4, INPUT_PULLUP);
  pinMode(5, INPUT_PULLUP);
  pinMode(6, INPUT_PULLUP);
  pinMode(7, INPUT_PULLUP);
  pinMode(8, INPUT_PULLUP);
  pinMode(9, INPUT_PULLUP);
  pinMode(10, INPUT_PULLUP);
  pinMode(11, INPUT_PULLUP);
  pinMode(12, INPUT_PULLUP);
  pinMode(A3, INPUT_PULLUP);
  pinMode(A4, INPUT_PULLUP);
  pinMode(A5, INPUT_PULLUP);
}

void loop() {
  potentiometers();
  rotaryEncoders();
  toggleSwitches();
  buttons();
}

void potentiometers() {
  int p0 = 1024 - analogRead(A0);
  if (p0 != p_p0) {
    p_p0 = p0;
    if (p0 > (print_p0 + 3) || p0 < (print_p0 - 3) || p0 >= 1021 || p0 <= 3) {
      print_p0 = p0;
      Serial.println("p 0 " + String(p0));
    }
  }

  int p1 = 1024 - analogRead(A1);
  if (p1 != p_p1) {
    p_p1 = p1;
    if (p1 > (print_p1 + 3) || p1 < (print_p1 - 3) || p1 >= 1021 || p0 <= 3) {
      print_p1 = p1;
      Serial.println("p 1 " + String(p1));
    }
  }

  int p2 = 1024 - analogRead(A2);
  if (p2 != p_p2) {
    p_p2 = p2;
    if (p2 > (print_p2 + 3) || p2 < (print_p2 - 3) || p2 >= 1021 || p0 <= 3) {
      print_p2 = p2;
      Serial.println("p 2 " + String(p2));
    }
  }
}

void rotaryEncoders() {
  int clk = digitalRead(A3);
  int dt = digitalRead(A4);
  if (clk != p_clk) {
    if (clk == dt) {
      Serial.println("re 0 clockwise");
    } else {
      Serial.println("re 0 counterclockwise");
    }
    p_clk = clk;
  }
}

void toggleSwitches() {
  int t0 = !digitalRead(9);
  if (t0 != p_t0) {
    p_t0 = t0;
    Serial.println("t 0 " + String(p_t0));
  }

  int t1 = !digitalRead(10);
  if (t1 != p_t1) {
    p_t1 = t1;
    Serial.println("t 1 " + String(p_t1));
  }

  int t2 = !digitalRead(11);
  if (t2 != p_t2) {
    p_t2 = t2;
    Serial.println("t 2 " + String(p_t2));
  }
}

void buttons() {
int s1 = !digitalRead(6);
  if (s1 != p_s1) {
    p_s1 = s1;
    Serial.println("s 1 " + String(p_s1));
  }

int s2 = !digitalRead(7);
  if (s2 != p_s2) {
    p_s2 = s2;
    Serial.println("s 2 " + String(p_s2));
  }

int s3 = !digitalRead(8);
  if (s3 != p_s3) {
    p_s3 = s3;
    Serial.println("s 3 " + String(p_s3));
  }

int sw = !digitalRead(A5);
  if (sw != p_sw) {
    p_sw = sw;
    Serial.println("s 4 " + String(p_sw));
  }

int s5 = !digitalRead(2);
  if (s5 != p_s5) {
    p_s5 = s5;
    Serial.println("s 5 " + String(p_s5));
  }

int s6 = !digitalRead(3);
  if (s6 != p_s6) {
    p_s6 = s6;
    Serial.println("s 6 " + String(p_s6));
  }

int s7 = !digitalRead(4);
  if (s7 != p_s7) {
    p_s7 = s7;
    Serial.println("s 7 " + String(p_s7));
  }

int s8 = !digitalRead(5);
  if (s8 != p_s8) {
    p_s8 = s8;
    Serial.println("s 8 " + String(p_s8));
  }
}