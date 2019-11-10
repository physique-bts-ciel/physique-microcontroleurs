Mesurer la célérité d'un son (première générale)
================================================

.. topic:: Programme de première générale 2019 - Enseignement de spécialité.

   Exploiter la relation entre la durée de propagation, la distance parcourue par une perturbation et la célérité, notamment pour localiser une source d’onde. Déterminer, par exemple à l’aide d’un microcontrôleur ou d’un smartphone, une distance ou la célérité d’une onde.



Principe
--------

Module HC-SR04
~~~~~~~~~~~~~~

Les modules du type  HC-SR04 sont des émetteurs-récepteurs ultrasonores fonctionnant par réflexion. Ils sont utilisés généralement dans des applications  comme télémètre.

.. figure:: Images/Ultrason_HC-SR04-Photo.png
   :width: 292
   :height: 162
   :scale: 70 %
   :alt: Montage ultrason - Arduino
   :align: center
   
   Module HC-SR04

Fonctionnement
~~~~~~~~~~~~~~
* Le module est alimenté entre ``GND`` et ``Vcc`` (généralement 5 V ou 3,3 V sur certains modules).
* Le déclenchement d'une mesure (émission d'une salve) se fait par une brève impulsion (> 10 µs) sur l'entrée ``trig``.
* La durée que prend l'onde pour aller de l'émetteur au récepteur est celle de l'impulsion renvoyée sur la sortie ``echo``. 

Chronogrammes
~~~~~~~~~~~~~

.. figure:: Images/Ultrason_HC-SR04_Chrono.png
   :width: 960
   :height: 720
   :scale: 70 %
   :alt: Chronogrammes HC-SR04
   :align: center
   
   Mesures réalisées à l'oscilloscope sur un module HC-SR04 (5 V)


Dans cet exemple, le calcul de la célérité du son donne 352 m/s.

Montage
-------


.. image:: Images/Ultrason_HC-SR04-Montage.png
   :width: 761
   :height: 445
   :scale: 50 %
   :alt: Montage ultrason - Arduino
   :align: center

Programme
---------

.. code:: arduino

   /*
    * Mesurer vitesse son
    */

   #define pinTrig 8       // Trig sur broche 8
   #define pinEcho 9       // Echo sur broche 9

   float distance = 0.3;   // Distance en module et réflecteur
   long dureeEcho;         // Durée mesurée
   float vitesse ;         // Vitesse obtenue


   void setup() {
     pinMode(pinTrig,OUTPUT);      // Broche Trig en sortie
     digitalWrite(pinEcho,LOW);    // Sortie Trig à l état bas
     pinMode(pinEcho,INPUT);       // Broche Echo en entrée
     Serial.begin(9600);           // Paramétrage du port série
   }

   void loop() {
     digitalWrite(pinTrig,HIGH);            // Début impulsion de declenchement
     delayMicroseconds(10);                 // Attendre 10 microseconde
     digitalWrite(pinTrig,LOW);             // Fin impulsion (Etat bas)
     dureeEcho = pulseIn(pinEcho,HIGH);     // Mesure de la durée de l impulsion sur Echo
     vitesse = 2*distance/dureeEcho * 1E6;  // Calcul de la vitesse
     Serial.print("Durée (s) = ");          // Affichage sur port série
     Serial.println(dureeEcho);
     Serial.print("Vitesse (m/s) = ");
     Serial.println(vitesse);
     delay(1000);                           // Attendre 1s
   }

A retenir
---------

Les modules du type HC-SR04 délivre une **impulsion à l'état haut** dont la durée est égale au temps que prend le son pour partir de l'émetteur puis revenir au récepteur.

Dans le programme la fonction ``pulseIn(pin,HIGH)`` est chargée de la **mesure de cette durée**.

Aller plus loin
---------------

Pour améliorer la précision, il est possible de réaliser plusieurs mesures et d'en faire une moyenne ou même de tracer un histogramme de ces mesures !

.. code:: arduino

   /*
    * Exporter plusieurs mesures de la vitesse du son
    * au format CSV pour exploitation par tableur ou
    * logiciels spécialisés (Regressi, Latis, ...)
    */

   #define pinTrig 8       // Trig sur broche 8
   #define pinEcho 9       // Echo sur broche 9

   float distance = 0.297; // Distance en module et réflecteur
   long dureeEcho;         // Durée mesurée
   int vitesse ;           // Vitesse obtenue
   int n=1;

   void setup() {
     pinMode(pinTrig,OUTPUT);     // Broche Trig en sortie
     digitalWrite(pinEcho,LOW);   // Sortie Trig à l état bas
     pinMode(pinEcho,INPUT);      // Broche Echo en entrée
     Serial.begin(9600);          // Paramétrage du port série
     Serial.println("n;v");       // Entête du fichier CSV
   }

   void loop() {
     if (n<=20) {
     digitalWrite(pinTrig,HIGH);                 // Début impulsion de déclenchement
     delayMicroseconds(10);                      // Attendre 10 microseconde
     digitalWrite(pinTrig,LOW);                  // Fin impulsion (Etat bas)
     dureeEcho = pulseIn(pinEcho,HIGH);          // Mesure de la durée de l impulsion sur Echo
     vitesse = round(2*distance/dureeEcho*1E6);  // Calcul de la vitesse
     Serial.print(n);                            // Début d écriture d une ligne de mesure
     Serial.print(";");
     Serial.println(vitesse);
     delay(100);                                 // Attendre 1s
     n++;
     }
   }

.. figure:: Images/ultrason_histogramme_moniteur_serie.png
   :width: 911
   :height: 423
   :scale: 70 %
   :alt:
   :align: center
   
   Mesures au format CSV obtenues dans le moniteur série


.. figure:: Images/ultrason_histogramme.png
   :width: 640
   :height: 480
   :scale: 70 %
   :alt:
   :align: center
   
   Histogramme des mesures tracé à l'aide du module ``matplolib`` de Python


