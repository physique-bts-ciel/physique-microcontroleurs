Pilotage d'une carte Arduino en Python avec Nanpy
=================================================

Qu'est-ce que Nanpy ?
---------------------

`Nanpy <https://nanpy.github.io/>`_ est une librairie pour Python utilisée pour le **pilotage** d'une carte Arduino **par le port USB d'un ordinateur programmé en Python**.

.. warning::

   Il est important de retenir que **Nanpy ne permet pas un fonctionnement autonome** de la carte Arduino puisque le carte doit-être **constamment connectée à l'ordinateur** sur lequel le programme Python est exécuté !


Principe de fonctionnement
--------------------------

La carte Arduino a été préalablement programmer avec le micro-logiciel **Nanpy-firmware** téléversé à partir du logiciel Arduino. Ce firmware est un **programme particulier** (écrit en langage Arduino C/C++) qui **gère le  protocole de communication** entre le programme Python exécuté sur l'ordinateur et la carte Arduino.

Téléversement du firmware Nanpy sur la carte Arduino
----------------------------------------------------

Installation du firmware dans les croquis du logiciel Arduino
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Le fichier ``nanpy-firmware-master.zip`` est à télécharger sur le site https://github.com/nanpy/nanpy-firmware.

.. image:: images/nanpy_telechargement_firmware_ksnip.png
   :width: 998
   :height: 530
   :scale: 50 %
   :alt: 
   :align: center

Puis il faut procéder dans l'orde suivant :

* extraire le répertoire ``nanpy-firmware-master`` de l'archive ``nanpy-firmware-master.zip`` à un emplacement quelconque ; 
* copier le fichier ``sample_cfg.h`` dans le répertoire ``Nanpy`` ;
* renommer ce nouveau fichier ``sample_cfg.h`` en ``cfg.f`` ;
* déplacer le répertoire ``Nanpy`` dans le carnet de croquis du logiciel Arduino (répertoire ``sketchbook``).

Téléversement du croquis du firmware sur la carte Arduino
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ouvrir le carnet de croquis ``Nampy`` à partir du menu :

*Fichier > Carnet de croquis > Nanpy*

.. image:: images/nanpy_ouvrir_croquis.png
   :width: 500
   :height: 601
   :scale: 70 %
   :alt: 
   :align: center

Puis **téléverser** le programme dans la carte Arduino.

.. image:: images/nanpy_televersement.png
   :width: 501
   :height: 600
   :scale: 70 %
   :alt: 
   :align: center

La carte est maintenant prête pour un fonctionnement avec Nanpy !

.. warning::

   Ne pas oublier de sélectionner le type de carte (ex. Arduino Uno) et le port de communication série (ex. COM3) dans le menu *Outils* avant le téléversement du firmware !



Installation la libairie Nanpy sur l'ordinateur
-----------------------------------------------

L'installation dépend de la distribution Python utilisée sur l'ordinateur.


Pour EduPython
~~~~~~~~~~~~~~

https://edupython.tuxfamily.org/

Il n'y a rien à faire car la librairie Nanpy est installée par défaut.

Pour les autres distributions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Il faut installer manuellement à partir du dépôt internet ``Pypi`` (https://pypi.org/project/nanpy/) à l'aide de la commande ``pip`` :

.. code:: bash

   pip install nanpy

Exemple : le programme Blink
----------------------------

Voici un exemple du programme **Blink** en Python.

.. code:: python

   from nanpy import ArduinoApi, SerialManager   # Fonctions de Nanpy
   from time import sleep                        # Importation fonction sleep()

   port = SerialManager(device='COM3')   # Sélection du port série (exemple : device = 'COM6')
   uno = ArduinoApi(connection=port)     # Déclaration de la carte Arduino Uno

   pinLed = 13                           # Led intégrée sur broche 13
   uno.pinMode(pinLed,uno.OUTPUT)        # Broche Led en sortie

   for i in range(100):                  # Boucle : répéter 100 fois
      uno.digitalWrite(pinLed,1)         # Led allumée
      sleep(1)                           # Attendre 1 s
      uno.digitalWrite(pinLed,0)         # Led eteinte
      sleep(1)                           # Attendre 1 s

