.. |kohm| replace:: :math:`{k\Omega}`
.. |ohm| replace:: :math:`{\Omega}`

Allumer une LED (sorties numériques)
====================================

Principe
--------

Les entrées/sorties numériques de la carte Arduino UNO sont accessibles sur les broches 0 à 13.

.. image:: images/01_arduino_uno_sorties_numeriques.png
   :width: 450
   :height: 400
   :scale: 60 %
   :alt:
   :align: center

.. warning::

   Une sortie numérique ne peut délivrer que 40 mA au maximum (200 mA pour l'ensemble des sorties). Au delà de cette valeur, la carte peut-être détériorée !


Montage
-------

Une LED en série avec une résistance est connectée entre la broche 11 et la masse (GND).

.. image:: images/Arduino_LED_PWM.png
   :width: 536
   :height: 423
   :scale: 60 %
   :alt:
   :align: center

La formule suivante donne le calcul de la résistance en fonction du courant nominal et de la couleur de la LED :

.. math::

   R = \dfrac{V_{CC}-V_S}{I}

* :math:`V_{CC}` est la tension d'alimentation (5 V) ;
* :math:`V_S \approx 2 V` est la tension de seuil de la LED (dépend de la couleur) ;
* :math:`I` est l'intensité du courant généralement de l'ordre de 20 mA.

Une valeur de 220 |ohm| est un bon compromis.

Programme
---------

.. code:: arduino

   int LED = 11;             // LED connectée sur broche 11

   void setup() {
     pinMode(LED, OUTPUT);   // Broche LED paramétrée en sortie
   }

   void loop() {
     digitalWrite(LED,0);    // LED éteinte
     delay(1000);            // Attendre 1 s
     digitalWrite(LED,1);    // LED allumée
     delay(1000);            // Attendre 1 s
   }

Dans la fonction ``setup()`` :

   * ``pinMode(LED,OUTPUT)`` paramètre la broche ``LED`` en sortie (``OUPUT``).

Dans la fonction ``loop()`` :

   * ``digitalWrite(LED,LOW)`` fixe un niveau logique 0 (``LOW``) sur la broche ``LED``.
   * ``digitalWrite(LED,HIGH)`` fixe un niveau logique 1 (``HIGH``) sur la broche ``LED``.

A retenir
---------

Une **sortie numérique présente deux états logiques** : état bas (0 V) ou état haut (5 V).

========================== =======================================
Instruction                Description
========================== =======================================
``pinMode(pin,OUTPUT)``    Configure le broche ``pin`` en sortie
``digitalWrite(pin,LOW)``  Met la broche ``pin`` à l'état bas (0 V)
``digitalWrite(pin,HIGH)`` Met la broche ``pin`` à l'état haut (5 V)
========================== =======================================

Applications
------------

   * Commande d'un actionneur (LED, relais, ...) en tout ou rien.
   * Communication numérique.

Avec Python et Nanpy
--------------------

.. code:: python

   from nanpy import ArduinoApi           # Librairie du gestion des carte Arduino
   from nanpy import SerialManager        # Librairie de gestion du port série
   from time import sleep                 # Importation fonction sleep()

   port = SerialManager()                 # Déclaration du port série
   uno = ArduinoApi(connection=port)      # Déclaration de la carte Arduino Uno

   pinLed = 11                            # N° de broche où la Led est branchée
   uno.pinMode(pinLed,uno.OUTPUT)         # Broche Led en sortie

   for i in range(100):                   # Boucle : répéter 100 fois
       uno.digitalWrite(pinLed,1)         # Led allumée
       sleep(1)                           # Attendre 1 s
       uno.digitalWrite(pinLed,0)         # Led eteinte
       sleep(1)                           # Attendre 1 s


