/* 
 *  Mesure de la résistance d'une CTN
 */

// Déclaration des variables pour la mesure de la résistance
float Vcc = 5.0;    // Tension d'alimentation
float R1 = 10000;   // Résistance du pont diviseur de tension
float U;            // Tension de la CTN en volt
float R_mes;        // Résistance mesurée de le CTN en Ohm



void setup() {
  Serial.begin(9600);  // Paramétrage du port série
}

void loop() {
  U = analogRead(A0)*Vcc/1023;   // Lecture tension en V
  R_mes = R1*U/(Vcc-U);          // Calcul de la résistance
  Serial.print("R = ");          // Affichage
  Serial.print(R_mes);           // Affichage
  Serial.println(" Ohm");         // Affichage + sout de ligne
  delay(1000);                   // Temporisation de 1s
}
