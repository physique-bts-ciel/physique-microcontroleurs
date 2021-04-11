=====================
Affichage de messages
=====================


Principe
========

De base, les cartes Arduino ne possède pas d'écran pour afficher des messages. L'interface série (UART) reste le moyen le plus simple pour afficher des informations sur un ordinateur en provenance d'une carte Arduino.



Programmation en langage Arduino (C/C++)
========================================

Le logiciel Arduino IDE met à disposition un **moniteur série** (dans le menu ``Outils > Moniteur série``) pour **lire des données** au format texte (ASCII) envoyées par le microcontrôleur.


.. image:: images/03_arduino_ide_moniteur_serie.png
   :width: 911
   :height: 603
   :scale: 50 %
   :alt:
   :align: center
   
Le moniteur série permet également de transmettre des données vers le microcontrôleur !

.. note::

   Il est possible d'utiliser d'autres logiciels de communication série comme `Putty <https://www.putty.org/>`_ ou encore `Termite <https://www.compuphase.com/software_termite.htm>`_.


.. code:: arduino

   int n = 0;

   void setup() {
     Serial.begin(9600);     // Paramétrage du port série

   }

   void loop() {
     Serial.print("N = ");   // Affichage
     Serial.println(n);      // Affichage du contenu de la variable n
     n = n + 1;              // Incrémentation de la variable n
     delay(1000);            // Temporisation de 1s
   }


.. image:: images/03_arduino_ide_moniteur_serie_2.png
   :width: 911
   :height: 603
   :scale: 50 %
   :alt:
   :align: center


* L'instruction ``Serial.begin(9600)`` paramètre le port série à 9600 baud (bits par seconde).

* ``Serial.print("N = ")`` affiche la chaine de caractères ``N =`` dans le moniteur série.

* ``Serial.println(n)`` affiche le contenu de la variable ``n`` suivie d'un saut de ligne.



Programmation en langage Python (pilotage Nanpy)
================================================

Avec Nanpy, le code Python est exécuté sur l'ordinateur et non sur le microcontrôleur. La fonction native ``print()`` de Python s'utilise tout naturellement ! 

.. code-block:: Python

   from nanpy import ArduinoApi, SerialManager
   from time import sleep

   port = SerialManager(device='COM6')  # Sélection du port série à modifier
   uno = ArduinoApi(connection=port)    # Déclaration de la carte Arduino Uno

   N = 0                                # Initialisation du compteur

   while True:
      print("N =", N)                   # Affichage
      N = N + 1                         # Incrémentation du compteur
      sleep(1)                          # Temporisation



Applications
============

* Affichage d'une ou plusieurs mesures sur l'écran d'un ordinateur.
* Affichage des données d'une acquisition au format CSV pour exploitation par un tableur ou des logiciels spécialisés (Regressi, Latis, ...). 


