
/* 
 *  Mesure de la résistance d'une CTN et calcul de la température 
 *  à partir de la relation simplifiée de Steinhart-Hart
 */ 

// Déclaration des variables pour la mesure de la résistance
float Vcc = 5.0;    // Tension d'alimentation
float R1 = 10000;   // Résistance du pont diviseur de tension
float U;            // Tension CTN en volt
float R_mes;        // Résistance CTN en ohm

// Déclaration des variables pour la calcul de la température
float T0 = 25;      // Température de référence (25°C)
float R0 = 10500;   // Resistance R0 à T0 = 25°C
float beta = 3290;  // Coefficient de temperature en K
float inverse;      // Inverse de la temperature en K-1
float T_K;          // Temperature en K
float T;            // Temperature en °C


void setup() {
  Serial.begin(9600);  // Paramétrage du port série
}

void loop() {
 U = analogRead(A0)*Vcc/1023;                      // Lecture de la tension en V
 R_mes = R1*U/(Vcc-U);                             // Calcul de la résistance mesurée
 Serial.print("R = ");                             // Affichage
 Serial.print(R_mes);                              // Affichage
 Serial.println(" Ohm");                           // Affichage + retour à la ligne
 
 inverse = 1/beta * log(R_mes/R0) + 1/(T0+273.15); // Calcul de l'inverse de la temperature
 T_K = 1/inverse;                                  // Calcul de la température en Kelvin
 T = T_K - 273.15;                                 // Caclul de la température en °C
 Serial.print("T = ");                             // Affichage
 Serial.print(T);                                  // Affichage
 Serial.println("°C");                             // Affichage + retour à la ligne
 delay(1000);                                      // Pause
}
