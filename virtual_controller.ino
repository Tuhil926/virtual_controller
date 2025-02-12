void setup() {
    Serial.begin(115200);
    pinMode(3, INPUT);
    pinMode(5, INPUT);
    pinMode(6, INPUT);
    pinMode(9, INPUT);
}

int GetPWM(int pin){
  unsigned long highTime = pulseIn(pin, HIGH, 50000UL);  // 50 millisecond timeout
  if (highTime == 0)
    return 1500;
  return highTime;
}

void loop() {
    int val4 = GetPWM(3);
    int val3 = GetPWM(5);
    int val2 = GetPWM(6);
    int val1 = GetPWM(9);
    
    Serial.print(String(val1) + " ");
    Serial.print(String(val2) + " ");
    Serial.print(String(val3) + " ");
    Serial.print(String(val4) + "\n");
}
