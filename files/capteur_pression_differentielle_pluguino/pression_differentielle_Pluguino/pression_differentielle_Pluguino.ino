/*
 * Capteur de pression différentielle Plug'Uino
 * 0 - 50 hPa -> 0,5 - 4,5 V (capteur XGZP6857A005KPG)
 * David THERINCOURT - 2025
 */

void setup() {
  Serial.begin(9600);          // Initialisation du port série
}

void loop() {
  int N = analogRead(A0);       // Lecture sur A0
  float u = N * (5.0 / 1023.0); // Calcul de la tension en volt
  float P = 1250*(u-0.5);       // Calcul de la pression en Pa
  Serial.print("U = ");         // Affichage
  Serial.print(u);              // ...
  Serial.print(" V \t");        // ...
  Serial.print(P);              // ...
  Serial.println(" Pa");        // ...
  delay(1000);                  // Temporisation
}
