============
Introduction
============

La carte officielle Pyboard
===========================

.. image:: images/pyboard.jpg
   :width: 500
   :height: 500
   :scale: 70 %
   :alt: Quelques cartes Arduino.
   :align: center

Créée par le physicien australien Damien George, la Pyboard est la carte officielle de la distribution MicroPython. Construit autour d'un microcontrôleur STM32 de STMicroelectronics, il s'agit d'une des plus puissantes cartes de développement du marché.

**Principales caractéristiques de la Pyboard v1.1 :**

* Microcontrôleur STM32F405 (ARM Cortex M4 - 32 bit - 168 Mhz) ;
* 1024 ko de mémoire flash (ROM) ;* 192 ko de mémoire vive (RAM) ;
* niveau de tension à 3,3V ;
* 1 port micro USB (programmation REPL + accès mémoire flash) ;
* lecteur micro SD ;
* 2 boutons, 4 LED, 1 accéléromètre 3 axes ;
* 35 ports E/S ;
* 3 CAN disponibles sur 16 broches ;
* 2 CNA disponibles sur 2 broches (X5 et X6) ;
* 17 timers.

**Brochage :**

Les broches d'entrée/sortie sont réparties en deux blocs : X1 à X12 et Y1 à Y12.

.. image:: images/pybv11-pinout.jpg
   :width: 1200
   :height: 900
   :scale: 50 %
   :alt: Quelques cartes Arduino.
   :align: center

   

La carte **Plug'Uino PY** de Sciencethic
========================================

Le fournisseur `Sciencethic <https://www.sciencethic.com/accueil.html>`_ propose une carte Pyboard (STM32F405) spécialement conçue pour les sciences physiques **Plug'Uino PY**.

.. figure:: images/sciencethic_pluguino_py.png
   :width: 554
   :height: 591
   :scale: 70 %
   :alt: Quelques cartes Arduino.
   :align: center

   Image : Sciencethic


Par rapport à la carte officielle, cette carte a l'avantage de disposer :

* de **protections des entrées/sorties** contre les mauvaises manipulations ;
* d'une **adaptation du niveau des tensions à 5V** en logique et en analogique ;
* d'un brochage Arduino en plus des connecteurs SATA pour les capteurs.

Elle dispose en autres :

* d'un écran OLED 64x32 pixels ;
* d'un accéléromètre 3D ;
* d'un lecteur de carte SD.

La carte **Feather STM32F405 Express** d'Adafruit
=================================================

.. image:: images/adafruit_feather_stm32f405.jpg
   :width: 500
   :height: 394
   :scale: 70 %
   :alt: Quelques cartes Arduino.
   :align: center

Dans la famille Feather d'Adafruit, la carte de développement `Feather STM32F405 Express <https://www.adafruit.com/product/4382>`_  est équivalent à la Pyboard. Associée au  `Grove Shield Featherwing <https://www.adafruit.com/product/4309>`_ , cela peut-être une alternative intéressante pour les sciences physiques.

Précautions
-----------

.. attention::

    Les cartes Pyboard sont alimentées sous 3,3 V. Même si les microcontrôleur STM32F405 ont une **tolérance de 5 V sur les entrées logiques**, ce n'est pas le cas pour **les tenions appliquées sur les entrées analogiques qui ne doivent pas dépassées les 3,3 V** sous peine de détruire la carte.

Il faudra donc bien faire attention à la compatibilité des niveaux de tension lors du choix des capteurs (ex. capteur de pression). Les capteurs actifs alimentés sous 5 V ne fonctionneront pas !

Ces précautions ne s'appliquent pas pour la carte **Plug'uino Py** car ce dernière est compatible 5 V.