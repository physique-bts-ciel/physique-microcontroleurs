.. |kohm| replace:: :math:`{k\Omega}`
.. |ohm| replace:: :math:`{\Omega}`

====================================
Allumer une LED (sorties numériques)
====================================

Principe
========

Les entrées/sorties numériques de la carte Arduino UNO sont accessibles sur les broches 0 à 13.

.. figure:: images/arduino_uno_sorties_numeriques.png
   :width: 450
   :height: 400
   :scale: 60 %
   :alt:
   :align: center

   Entrées/sorties numériques

.. warning::

   Une sortie numérique ne peut délivrer que 40 mA au maximum (200 mA pour l'ensemble des sorties). Au delà de cette valeur, la carte peut-être détériorée !


Montage
=======

Une LED en série avec une résistance est connectée entre la broche 11 et la masse (GND).

.. figure:: images/arduino_LED_PWM.png
   :width: 536
   :height: 423
   :scale: 60 %
   :alt:
   :align: center

   Branchement d'une LED sur la broche 11

La formule suivante donne le calcul de la résistance en fonction du courant nominal et de la couleur de la LED :

.. math::

   R = \dfrac{V_{CC}-V_S}{I}

* :math:`V_{CC}` est la tension d'alimentation (5 V) ;
* :math:`V_S \approx 2 V` est la tension de seuil de la LED (dépend de la couleur) ;
* :math:`I` est l'intensité du courant généralement de l'ordre de 20 mA.

Une valeur de résistance de 220 |ohm| donne un bon compromis.

Programme en langage Arduino (C/C++)
====================================

.. code-block:: arduino

   int pinLED = 11;             // LED connectée sur broche 11

   void setup() {
     pinMode(pinLED, OUTPUT);   // Broche LED paramétrée en sortie
   }

   void loop() {
     digitalWrite(pinLED,0);    // LED éteinte
     delay(1000);               // Attendre 1000 ms = 1s
     digitalWrite(pinLED,1);    // LED allumée
     delay(1000);               // Attendre 1000 ms = 1s
   }

Dans la fonction ``setup()`` :

* ``pinMode(LED,OUTPUT)`` paramètre la broche ``LED`` en sortie (``OUPUT``).

Dans la fonction ``loop()`` :

* ``digitalWrite(LED,LOW)`` fixe un niveau logique 0 (``LOW``) sur la broche ``LED``.
* ``digitalWrite(LED,HIGH)`` fixe un niveau logique 1 (``HIGH``) sur la broche ``LED``.



Applications
============

* Commande d'un actionneur (LED, relais, ...) en tout ou rien.
* Communication numérique.


