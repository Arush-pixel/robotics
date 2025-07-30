const int HallSensor = A0;
const int LED = 13;
const int Buzzer = 8;

int baseline = 0;

void setup() {
  pinMode(LED, OUTPUT);
  pinMode(Buzzer, OUTPUT);
  Serial.begin(9600);

  // 🔍 Take baseline reading
  baseline = analogRead(HallSensor);
  Serial.print("Baseline: ");
  Serial.println(baseline);
}

void loop() {
  int sensorValue = analogRead(HallSensor);
  Serial.println(sensorValue);

  // Trigger only if the value drops well below baseline
  if (sensorValue < baseline - 30) {  // Adjust margin as needed
    digitalWrite(LED, HIGH);
    tone(Buzzer, 1000);
  } else {
    digitalWrite(LED, LOW);
    noTone(Buzzer);
  }

  delay(100);
}
