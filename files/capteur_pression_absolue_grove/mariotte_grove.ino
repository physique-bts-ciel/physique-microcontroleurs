/*
 * Mesure d'une pression absolue
 * Capteur Grove MPX5700AP (15 kPa à 700 kPa) branché sur la broche A0
 * David THERINCOURT - 2025
 */

float tension ;    // Tension mesurée (V)
float pression ;   // Pression mesurée (kPa)

void setup() {
  Serial.begin(9600); // Initialisation du port série
}

void loop() {
  tension = analogRead(A0)*5.0/1023 ;    // Lecture de la tension sur A0 en volt
  pression = 152*(tension-0.2) + 15 ;    // Calcul de la pression en kPa
  Serial.print("U = ");                  // Affichage dans le moniteur série
  Serial.print(tension);                 // Affichage de la tension
  Serial.print(" V  =>  ");              // ...
  Serial.print("P = ");                  // ...
  Serial.print(pression, 0);             // Affichage de la pression arrondie
  Serial.println(" kPa");                // Fin affichage
  delay(1000);                           // Temporisation
}
