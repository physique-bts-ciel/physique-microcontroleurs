Le logiciel Arduino
===================

Le logiciel **Arduino** est un environnement intégré de développement (IDE) multiplaforme. Il est téléchargeable sur le site officiel http://www.arduino.cc/en/

.. image:: images/Arduino_IDE.png
   :width: 500
   :height: 407
   :scale: 70 %
   :alt: Quelques cartes Arduino.
   :align: center

.. Note::
   Arduino.cc propose une **version Web** (https://create.arduino.cc/) de son environnement de développement. Elle nécessite l'installation d'un plugin afin de programmer la carte par le port USB.

Choix du port de communication avec la carte Arduino
----------------------------------------------------

.. image:: images/Arduino_IDE_Select_Port.png
   :width: 818
   :height: 347
   :scale: 70 %
   :alt: Quelques cartes Arduino.
   :align: center



.. warning::

   Pour programmer une carte Arduino, il est nécessaire de connectée cette dernière à l'ordinateur par l'intermédiaire d'un câble USB. Une fois le logiciel Arduino lancé, il est **impératif de  sélectionner le port série** donnant accès à la carte Arduino (ex. COM3). Sinon il ne sera pas possible de téléverser le futur programme.

Mise en œuvre d'un projet Arduino :
-----------------------------------

.. image:: images/Arduino_IDE_Barre_Outils.png
   :width: 500
   :height: 33
   :scale: 100 %
   :alt: Quelques cartes Arduino.
   :align: center

La mise en œuvre d'un projet Arduino s'effectue dans l'ordre suivant :

1. **Édition** du programme dans l'éditeur de l'interface ;
2. **Vérification** du programme (compilation) ;
3. **Téléversement** du programme ;
4. **Exécution** sur le carte Arduino (de façon autonome sans ordinateur).

