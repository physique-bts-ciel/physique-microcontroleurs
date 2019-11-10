Mesurer une tension (CAN)
=========================



Principe
--------

La mesure d'une tension par un microcontrôleur est réalisée en interne par un **convertisseur analogique-numérique**.

Ce type de conversion est importante en sciences physique. Elle permet par exemple d'obtenir la mesure d'une grandeur physique provenant d'un **capteur**.

Arduino UNO dispose de **6 entrées analogiques** disponibles sur les broches A0 à A5. Par défaut, la tension en entrée doit-être comprise entre 0 V et 5 V (Vref). La résolution de la conversion est de 10 bits.


.. image:: images/05_arduino_entrees_analogiques.png
   :width: 500
   :height: 400
   :scale: 70 %
   :alt:
   :align: center


   
.. warning::
   Le tension appliquée sur les entrées analogiques doivent être **strictement comprise entre 0 V et 5 V** sous peine de détruire le microcontrôleur.

Montage
-------

Un pont diviseur de tension branché entre la masse (``GND``) et la tension d'alimentation (``5V``) délivre une tension réglable sur l'entrée ``A0``.

.. figure:: images/05_arduino_uno_can_potentiometre.png
   :width: 667
   :height: 669
   :scale: 50 %
   :alt:
   :align: center
   
   Montage potentiométrique

Programme
---------

Le programme suivant lit la tension sur l'entrée ``A0`` et affiche sa valeur dans le moniteur série du logiciel Arduino.

.. code:: arduino

   /*
     Lecture de l'entrée analogique A0 sur le port série.
   */

   int valAnalog;    // Entier compris entre 0 et 1023 (10bits)
   float tension;    // La tension calculée est un nombre à virgule

   void setup() {
     Serial.begin(9600);   // Paramétrage port série
   }

   void loop() {
     valAnalog = analogRead(A0);     // Lecture valeur sur A0
     tension = valAnalog*5.0/1023;   // Calcul de la tension
     Serial.print("Valeur A0 = ");
     Serial.println(valeurA0);       // Affichage valeur A0
     Serial.print("Tension = ");
     Serial.println(tension);        // Affichage de la tension
     delay(1000);                    // temporisation de 1 s
   }




* La fonction ``analogRead(A0)`` retourne un entier sur 10 bits compris entre 0 (pour 0V) et 1023 (pour 5V).

* L'expression ``valAnalog*5.0/1023`` calcule la valeur de la tension en volt.

A retenir
---------

===================== =======================================
Instruction           Description
===================== =======================================
``analogRead(A0)``    Retourne un entier entre 0 et 1023 proportionnel à la tension appliquée
===================== =======================================

Applications
------------

* Interface avec un circuit comportant un capteur.
* Mesure d'une position (potentiomètre).
