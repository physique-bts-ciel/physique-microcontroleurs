Communication avec un ordinateur (port série)
=============================================

Principe
--------

De base, les cartes Arduino ne possède pas d'écran pour afficher des messages. L'interface série (UART) reste le moyen le plus simple pour communiquer avec une carte Arduino.

Le logiciel Arduino IDE dispose d'un **moniteur série** (``Outils > Moniteur série``) pour **lire des données** au format texte (ASCII) envoyées par le microcontrôleur.



.. image:: images/03_arduino_ide_moniteur_serie.png
   :width: 911
   :height: 603
   :scale: 50 %
   :alt:
   :align: center
   
Le moniteur série permet également de transmettre des données vers le microcontrôleur !

.. note::

   Il est possible d'utiliser d'autres logiciels de communication série comme `Putty <https://www.putty.org/>`_ ou encore `Termite <https://www.compuphase.com/software_termite.htm>`_.

Montage
-------

Une carte Arduino est connectée par le port USB à un ordinateur.

Programme
---------

.. code:: arduino

   /*
   * Affichage le contenu d'une variable dans un moniteur série.
   */

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


* L'instruction ``Serial.begin(9600)`` paramètre le port série à 9600 baud.

* ``Serial.print("N = ")`` affiche la chaine de caractère ``N =`` dans le moniteur série.

* ``Serial.println(n)`` affiche le contenu de la variable ``n`` suivie d'un saut de ligne.

A retenir
---------

========================== =======================================
Instruction                Description
========================== =======================================
``Serial.begin(speed)``    Fixe le vitesse de transmission en bits par seconde (baud)
``Serial.print()``         Ecrit des données (format texte) sur le port série
``Serial.println()``       Ecrit des données (format texte) sur le port série
                           suivi d'un saut de ligne
========================== =======================================


Applications
------------

* Affichage d'une ou plusieurs mesures sur l'écran d'un ordinateur.
* Affichage des données d'une acquisition au format CSV pour exploitation par un tableur ou des logiciels spécialisés tels que Regressi, Latis, ...


