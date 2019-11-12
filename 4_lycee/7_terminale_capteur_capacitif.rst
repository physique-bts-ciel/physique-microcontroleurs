Capteur capacitif (terminale générale)
======================================

.. topic:: Programme de terminale générale 2019 - Enseignement de spécialité.

   Expliquer le principe de fonctionnement de quelques capteurs capacitifs. Étudier la réponse d’un dispositif modélisé par un dipôle RC. **Déterminer le temps caractéristique d'un dipôle RC** à l’aide d’un microcontrôleur, d’une carte d’acquisition ou d’un oscilloscope.

Principe
--------

Sur la réponse d'un circuit RC à un échelon de tension de 0 V à :math:`V_{cc}`, le temps caractéristique :math:`\tau` est la durée que prend cette réponse pour atteindre 63% de sa valeur finale :math:`V_{cc}`.

Il suffit donc de mesurer, à l'aide du timer du microcontrôleur, la durée que prend la tension aux bornes du condensateur pour passer de :math:`0` à :math:`0,63 \times V_{cc}`.


Montage
-------

.. image:: Images/RC_Montage_Charge.png
   :width: 917
   :height: 510
   :scale: 50 %
   :alt:
   :align: center

* La broche digitale ``8`` charge ou décharge le condensateur à travers la résistance.
* ``A0`` mesure la tension aux bornes du condensateur.

Données :

.. math::

   R = 1\,M\Omega \qquad C=22\,nF

Programme
---------

.. code-block:: arduino

   /*
    *  Mesure de constante de temps d un circuit RC
    */

   #define pinE 8

   int N = 0;
   unsigned long t0;
   unsigned long t1;
   unsigned long Dt;
   float C;


   void setup() {
     Serial.begin(9600);
     Serial.println("Start");
     pinMode(pinE,OUTPUT);      // Broche digitale en sortie

     digitalWrite(pinE,LOW);    // Décharge condensateur avant mesure
     delay(1000);               // pendant 1 s

     digitalWrite(pinE,HIGH);   // Début charge condensateur
     t0 = micros();             // Mesure instant initial

     while (N<646) {            // Boucle tant que tension inférieure à seuil (0,632*1023=646)
       N=analogRead(A0);        // Lecture tension condensateur
     }

     t1 = micros();             // Mesure instant où seuil atteint
     Dt = t1 - t0;              // Calcul de tau

     Serial.print(Dt);          // Début affichage
     Serial.println(" µs");
     digitalWrite(pinE,LOW);    // Début décharge condensateur
   }

   void loop() {
     // Boucle sans fin pas utilisée ici !
   }

A retenir
---------

La fonction ``micros()`` renvoie la durée en µs (< 70 min) depuis que la carte Arduino a été mise sous tension.
La précision est de 4 µs !

Application : mesure d'une capacité
-----------------------------------

.. code-block:: arduino

   /*
    *  Mesure de la capacité d un circuit RC
    */

   #define pinE 8

   int N = 0;
   unsigned long t0;
   unsigned long t1;
   unsigned long Dt;
   float C;


   void setup() {
     Serial.begin(9600);
     Serial.println("Start");
     pinMode(pinE,OUTPUT);      // Broche digitale en sortie

     digitalWrite(pinE,LOW);    // Décharge condensateur avant mesure
     delay(1000);               // pendant 1 s

     digitalWrite(pinE,HIGH);   // Début charge condensateur
     t0 = micros();             // Mesure instant initial

     while (N<646) {            // Boucle tant que tension inférieure à seuil (0,632*1023=646)
       N=analogRead(A0);        // Lecture tension condensateur
     }

     t1 = micros();             // Mesure instant où seuil atteint
     Dt = t1 - t0;              // Calcul de tau
     C = Dt/1000.0;             // Calcul de C connaissant R

     Serial.print(C);           // Début affichage
     Serial.println(" nF");     // Fin affichage
     digitalWrite(pinE,LOW);    // Début décharge condensateur
   }

   void loop() {
     // Boucle sans fin pas utilisée ici !
   }
