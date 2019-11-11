Mesurer la célérité d'un son (première générale)
================================================

.. topic:: Programme de première générale 2019 - Enseignement de spécialité.

   Exploiter la relation entre la durée de propagation, la distance parcourue par une perturbation et la célérité, notamment pour localiser une source d’onde. Déterminer, par exemple à l’aide d’un microcontrôleur ou d’un smartphone, une distance ou la célérité d’une onde.



Présentation du module HC-SR04
------------------------------

Les modules du type  HC-SR04 sont des émetteurs-récepteurs ultrasonores fonctionnant par réflexion. Ils sont utilisés généralement dans des applications comme télémètre (< 5 m).

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

Modification du module
~~~~~~~~~~~~~~~~~~~~~~

Tel qu'il est vendu, ce module n'a peu d'intérêt en sciences physiques car les signaux électriques sur l'émetteur et le récepteur ne sont pas accessibles.
Il est possible de résoudre ce problème en y soudant deux connecteurs supplémentaires (voir photo ci-dessous) et de visualiser ces deux signaux à l'oscilloscope ou avec une interface d'acquisition.

.. image:: Images/Ultrason_HC-SR04-modifie-soudures.png
   :width: 700
   :height: 500
   :scale: 50 %
   :alt:
   :align: center

Mesure de la célérité du son
----------------------------

Principe
~~~~~~~~

Montage
~~~~~~~

.. figure:: Images/Ultrason_HC-SR04-Montage-Oscillo.png
   :width: 837
   :height: 434
   :scale: 50 %
   :alt: Montage ultrason - Arduino
   :align: center

   Montage avec oscilloscope ou interface d'acquisition

.. figure:: Images/Ultrason_HC-SR04-Module_arduino_sysam.png
   :width: 900
   :height: 600
   :scale: 50 %
   :alt:
   :align: center

   Acquisition avec interface Sysam SP5

.. figure:: Images/Ultrason_HC-SR04-modifie.png
   :width: 900
   :height: 900
   :scale: 50 %
   :alt:
   :align: center

   Branchement du module HC-SR04 modifié



Programme
~~~~~~~~~

.. code-block:: arduino

   /*
    * Pilotage du module ultrason avec mesure de durée
    */

   #define pinTrig 8       // Trig sur broche 8
   #define pinEcho 9       // Echo sur broche 9

   long dureeEcho;         // Durée de l'Echo

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
     dureeEcho = pulseIn(pinEcho,HIGH);     // Mesure de la durée de l'impulsion sur Echo
     Serial.print("Durée (µs) = ");          // Affichage sur port série
     Serial.println(dureeEcho);
     delay(1000);                           // Attendre 1s
   }



Résultats
~~~~~~~~~

La mesure de durée est donnée par le microcontrôleur et/ou mesurée sur les chronogrammes.

.. figure:: Images/Ultrasons_Latis.png
   :width: 932
   :height: 857
   :scale: 50 %
   :alt:
   :align: center

   Mesures obtenues dans Latis avec Sysam SP5


.. figure:: Images/Ultrasons_scope_60cm.png
   :width: 900
   :height: 600
   :scale: 50 %
   :alt:
   :align: center

   Mesures à l'oscilloscope pour une distance de 30 cm

.. note::

   La fonction ``+Width`` de l'oscilloscope mesure en temps réel la durée de l'impulsion sur la broche ``Echo``.

Par exemple, pour une distance de 30 cm, la mesure de la célérité du son est :

.. math::

   c = \dfrac{2 \times d}{\Delta t} = \dfrac{2 \times 300}{1,73} \approx 347\,m\cdot s^{-1}

Application : réalisation d'un télémètre
----------------------------------------

Principe
~~~~~~~~

Connaissant la célérité du son, la distance par rapport à un obstacle est calculée par le microcontrôleur à l'aide de la relation suivante :

.. math::

   d = \dfrac{c \times \Delta t}{2}

L'affichage de la distance peut se faire sur un afficheur ou dans le moniteur série de l'ordinadeur.

Montage
~~~~~~~

.. figure:: Images/Ultrason_HC-SR04-Montage.png
   :width: 720
   :height: 429
   :scale: 50 %
   :alt: Montage ultrason - Arduino
   :align: center

   Montage télémètre

Programme
~~~~~~~~~

Le programme est le même. Il suffit juste ajouter le calcul de la distance.

Avec le moniteur série :

.. code-block:: arduino

   /*
   * Application : télémétre
   */

   #define pinTrig 8       // Trig sur broche 8
   #define pinEcho 9       // Echo sur broche 9

   float distance;         // Distance en module et réflecteur
   long dureeEcho;         // Durée mesurée
   float vitesse = 345 ;   // Vitesse obtenue


   void setup() {
   pinMode(pinTrig,OUTPUT);      // Broche Trig en sortie
   digitalWrite(pinEcho,LOW);    // Sortie Trig à l état bas
   pinMode(pinEcho,INPUT);       // Broche Echo en entrée
   Serial.begin(9600);           // Paramétrage du port série
   }

   void loop() {
   digitalWrite(pinTrig,HIGH);                   // Début impulsion de déclenchement
   delayMicroseconds(10);                        // Attendre 10 microseconde
   digitalWrite(pinTrig,LOW);                    // Fin impulsion (Etat bas)
   dureeEcho = pulseIn(pinEcho,HIGH);            // Mesure de la durée de l'impulsion sur Echo
   distance = 100*(vitesse*dureeEcho*1E-6)/2;    // Calcul de la distance
   Serial.print("Durée (s) = ");                 // Affichage sur port série
   Serial.println(dureeEcho);
   Serial.print("Distance (cm) = ");
   Serial.println(distance);
   delay(1000);                                   // Attendre 1s
   }

Avec un écran LCD 2x16 :

.. code-block:: arduino

    /*
     * Application : télémétre sur écran LCD 2x16
     */
   #include <LiquidCrystal.h>        // Importation de la librairie LiquidCrystal
   #define pinTrig 8       // Trig sur broche 8
   #define pinEcho 9       // Echo sur broche 9

   LiquidCrystal lcd(12, 11, 5, 4, 3, 2);  // Brochage de l'afficheur

   float distance;         // Distance en module et réflecteur
   long dureeEcho;         // Durée mesurée
   float vitesse = 345 ;   // Vitesse obtenue


   void setup() {
    pinMode(pinTrig,OUTPUT);      // Broche Trig en sortie
    digitalWrite(pinEcho,LOW);    // Sortie Trig à l état bas
    pinMode(pinEcho,INPUT);       // Broche Echo en entrée
    lcd.begin(16, 2);               // fixe le nombre de colonnes et de lignes de l afficheur
   }

   void loop() {
    digitalWrite(pinTrig,HIGH);                   // Début impulsion de déclenchement
    delayMicroseconds(10);                        // Attendre 10 microseconde
    digitalWrite(pinTrig,LOW);                    // Fin impulsion (Etat bas)
    dureeEcho = pulseIn(pinEcho,HIGH);            // Mesure de la durée de l'impulsion sur Echo
    distance = (vitesse*dureeEcho*1E-6)/2;    // Calcul de la distance
    lcd.setCursor(0,0);                           // place le curseur au début de la ligne 0
    lcd.print("Distance en m");                  // Affiche la légende
    lcd.setCursor(0,1);                           // place le curseur au début de la ligne 1
    lcd.print(distance);                          // Affiche la valeur de la distance
    delay(1000);                                  // Attendre 1s
   }

.. figure:: Images/Ultrason_HC-SR04_Educaduino_LCD.png
   :width: 850
   :height: 550
   :scale: 50 %
   :alt: Montage ultrason - Arduino
   :align: center

   Télémètre sur Educaduino-Lab LCD

A retenir
---------

* Le module HC-SR04 fournit un **signal Echo pour la mesure automatique de la durée** de propagation du son.

* La fonction ``pulseIn(pin,HIGH)`` **mesure cette durée**.


