Pilotage d'une carte Arduino en Python avec Nanpy
=================================================

Qu'est-ce que Nanpy ?
---------------------

Nanpy est une librairie pour Python utilisée pour le **pilotage** d'une carte Arduino par le câble USB (port série).

https://nanpy.github.io/

Principe de fonctionnement
--------------------------

La carte Arduino a été préalablement programmer avec le firmware **Nanpy** téléversé à partir du logiciel Arduino. Ce firmware est un **programme particulier** (écrit en langage Arduino C/C++) qui **gère le  protocole de communication** entre le programme Python exécuté sur l'ordinateur et la carte Arduino.

.. warning::

   Il est important de retenir que **Nanpy ne permet pas un fonctionnement autonome** de la carte Arduino puisque le carte doit-être **constamment connectée à l'ordinateur** sur lequel le programme Python est exécuté !

Installation de firmware Nanpy sur une carte Arduino
----------------------------------------------------

Téléchargement du firmware
~~~~~~~~~~~~~~~~~~~~~~~~~~

Le fichier ``nanpy-firmware-master.zip`` est une librairie Arduino contenant le firmware Nanpy à installer sur la carte Arduino.

Ce fichier est à télécharger sur le site https://github.com/nanpy/nanpy-firmware.

.. image:: images/nanpy_telechargement_firmware_ksnip.png
   :width: 998
   :height: 530
   :scale: 50 %
   :alt: 
   :align: center

Installation du firmware dans le logiciel Arduino
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Le fichier ``nanpy-firmware-master.zip`` est à installer dans les librairies d'Arduino à partir du menu `Croquis > Inclure une bibliothèque > Ajouter la bibliothèque au format .Zip ...`

.. image:: images/nanpy_ajouter_librairie_ksnip.png
   :width: 750
   :height: 400
   :scale: 50 %
   :alt: 
   :align: center

Téléversement du firmware dans la carte Arduino
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ouvrir le fichier d'exemple ``Nampy`` à partir du menu :

*Fichier > Exemples > nanpy-firmware-master > Nanpy*



.. image:: images/nanpy_ouvrir_exemple_ksnip.png
   :width: 680
   :height: 840
   :scale: 50 %
   :alt: 
   :align: center

Puis **téléverser** le programme dans la carte Arduino.

.. image:: images/nanpy_televersement_ksnip.png
   :width: 500
   :height: 563
   :scale: 70 %
   :alt: 
   :align: center

.. warning::

   Ne pas oublier de sélectionner le type de carte (ex. Arduino Uno) et le port de communication série (ex. COM3) dans le menu *Outils* avant le téléversement du firmware !

La carte est mainteanant prête pour un fonctionnement avec Nanpy !

Installer la libairie Nanpy sur l'ordinateur
--------------------------------------------

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

Exemple : Blink
---------------

Voici un exemple du programme **Blink** en Python.

.. code:: python

   from nanpy import ArduinoApi           # Librairie du gestion des carte Arduino
   from nanpy import SerialManager        # Librairie de gestion du port série
   from time import sleep                 # Importation fonction sleep()

   port = SerialManager()                 # Déclaration du port série
   uno = ArduinoApi(connection=port)      # Déclaration de la carte Arduino Uno

   pinLed = 13                            # Led intégrée branchée sur boche 13
   uno.pinMode(pinLed,uno.OUTPUT)         # Broche Led en sortie

   while True:                            # Boucle infinie
       uno.digitalWrite(pinLed,1)         # Led allumée
       sleep(1)                           # Attendre 1 s
       uno.digitalWrite(pinLed,0)         # Led éteinte
       sleep(1)                           # Attendre 1 s

