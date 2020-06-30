Qu'est-ce que MicroPython ?
===========================

Site Web : https://micropython.org/

Présentation
------------

MicroPython est une réécriture complète de Python (version 3) optimisée pour des microcontrôleurs créée par le physicien Damien George.

Comme le plupart des distributions Python, MicroPython permet :

   * d'interpréter des scripts (fichiers ``.py``) directement sur le microcontrôleur ;
   * ou d'exécuter des instructions en mode interactif depuis un ordinateur distant (mode RELP).
   
Ce type de fonctionnement impose l'installation d'un **firmware** englobant MicroPython sur le microcontrôleur. La plupart du temps, ce firmware est présent d'origine.

MicroPython sous `licence MIT <https://docs.micropython.org/en/latest/license.html>`_  est libre. Ce qui explique l’existence d'autres distrubutions dérivées comme `Micro:bit MicroPython <https://microbit-micropython.readthedocs.io/en/latest/>`_ ou `CircuitPython <https://circuitpython.org/>`_.

Quels microcontrôleurs ?
------------------------

Le fonctionnement de MicroPython nécessite un microcontrôleur avec un microprocesseur performant (32 bits) et avec suffisamment de mémoire. Porté à l'origine sur les architectures ARM Cortex M, la distribution se retrouve aujourd'hui sur d'autres architectures comme ESP8266 ou ESP32. Par contre, l'Arduino UNO n'est pas compatible !

Voici une liste non-exhaustive de cartes de développement fonctionnant sous MicroPython :

* `Pyboard <https://store.micropython.org/>`_ (STM32R405 - carte performante - un peu chère) ;
* `BBC Micro:bit <https://microbit.org/fr/>`_ (nRF51822 - éducation - un peu simpliste) ;
* `M5Stack <https://m5stack.com/>`_ (ESP32 - plutôt orienté informatique - Wifi).

.. note::

   Une version de `CircuitPython <https://circuitpython.org/board/arduino_zero/>`_ existe pour la carte `Arduino Zero <https://store.arduino.cc/genuino-zero>`_ (SAMD21).

Le langage
----------

Le langage MicroPython est identique à Python sauf que la distrubution est un peu plus légère et prend moins de place en mémoire. Du coup, seules les principales librairies comme ``math`` ou ``utime`` (équivalente à ``time``) sont implémentées.

.. note::

   Le préfixe ``u`` est utilisé pour spécifier une version du module propre à MicroPython.
   
Il existe aussi d'autres librairies spécifiques à la carte de développement utilisée comme par exemple :

   * ``pyb`` pour la Pyboard ;
   * ``microbit`` pour la Micro:bit ;
   * ou encore ``esp32`` pour la M5Stack.
   
Par contre, d'autres librairies spéciales comme ``machine`` sont utilisables avec toutes les cartes.


Environnement de développement
------------------------------

Plusieurs outils ont été conçus pour le développement de microcontrôleurs sous MicroPython.

* `Mu <https://codewith.mu/>`_ est un éditeur simpliste pour Micro:bit et les cartes Adafruit sous CircuitPython.

* `uPyCraft IDE <http://docs.dfrobot.com/upycraft/>`_ de DFRobot gère les microcontrôleurs ESP32 et ESP8266.

* `Thonny <https://thonny.org/>`_, un autre éditeur pour débutant, intègre des plugins pour la plupart des microcontrôleurs (micro:bit, Pyboard, ESP32, ...). C'est le plus polyvalent.
 




   









