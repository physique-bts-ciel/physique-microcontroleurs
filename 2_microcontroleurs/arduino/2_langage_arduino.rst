=======================
Langage Arduino (C/C++)
=======================

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
3. **Téléversement** du programme sur la carte Arduino ;
4. **Exécution** du programme sur le carte Arduino (de façon autonome sans ordinateur).







Premier programme : Blink
=========================

Le programme **Blink** propose de faire clignoter la LED intégrée à la carte de développement. Cette LED est connectée en interne à la broche 13.

Edition
-------

Le programme **Blink** est disponible dans les exemples du logiciel **Arduino IDE**.

Dans le menu ``Fichier > Exemples > Basics > Blink``.

.. figure:: images/Blink_01_exemples_blink.png
   :width: 780
   :height: 605
   :scale: 50 %
   :alt: Ouvrir Blink
   :align: center
   
   Ouvrir le programme Blink

.. figure:: images/Blink_02_edition_blink.png
   :width: 625
   :height: 500
   :scale: 60 %
   :alt: Edition Blink
   :align: center
   
   Edition du programme Blink

.. note::

   * Un programme Arduino écrit en **langage C/C++** est composé **d'une suite d'intructions**.

   * Ces instructions sont exécutées dans **l'ordre des lignes de code**.

   * Les **commentaires** en gris sont délimités par les caractères ``/*`` et ``*/`` sur plusieurs lignes ou commencent pas les caractères ``//`` sur une même ligne.

.. figure:: images/Blink_02_edition_blink_modifie.png
   :width: 557
   :height: 523
   :scale: 70 %
   :alt: Edition Blink
   :align: center
   
   Une version modifiée du programme Blink

.. warning::

   Un progamme Arduino respecte toujours une **structure spécifique** composée en trois parties :

      * Les déclarations : **définitions** des constantes et des variables ;
      * La fonction ``setup()`` : **configuration** de la carte (entrées, sorties, port série, ...) ;
      * La fonction ``loop()`` : **instructions du programme exécutées** dans une **boucle infinie** (sans fin).




Compilation
-----------

.. warning::

   Avant de lancer la compilation, il est important de **choisir le modéle de carte Arduino utilisé**. Le programme généré est dépendant du type de microcontrôleur présent sur la carte.
   

.. figure:: images/Blink_03_compilation_choix_carte.png
   :width: 815
   :height: 600
   :scale: 50 %
   :alt: Edition Blink
   :align: center
   
   Choix du type de carte

.. figure:: images/Blink_03_compilation_ksnip.png
   :width: 500
   :height: 600
   :scale: 70 %
   :alt: Edition Blink
   :align: center

   Puis la compilation peut s'effectuée !

Téléversement
-------------

.. warning::

   Pour téléverser le programme obtenu, il est nécessaire de **sélectionner le port de communication série** sur lequel est connectée la carte Arduino.
   
.. figure:: images/Blink_04_televersement_choix_port.png
   :width: 855
   :height: 340
   :scale: 50 %
   :alt: Edition Blink
   :align: center
   
   Choix du port de communication

.. figure:: images/Blink_04_televersement_ksnip.png
   :width: 500
   :height: 600
   :scale: 70 %
   :alt: Edition Blink
   :align: center
   
   Téléversement du programme

Exécution
---------

Le programme s'exécute sur la carte Arduino de façon autonome (sans ordinateur).

.. figure:: images/Blink_05_execution_ksnip.png
   :width: 400
   :height: 283
   :scale: 70 %
   :alt: Edition Blink
   :align: center








Particularité du langage Arduino
================================

Le langage de programmation C/C++ est utilisé par le logiciel Arduino pour programmer les microcontrôleurs Arduino.

.. image:: images/Blink_02_edition_blink_modifie.png
    :width: 557
    :height: 523
    :scale: 100 %
    :alt: Edition Blink
    :align: center

Syntaxe
-------

* Toutes les instructions se terminent par un point virgule ``;`` sauf pour les directives ``#include`` et ``#define``.
* Les blocs d'instructions sont délimités par des accolades ``{...}``.
* Les **commentaires** en gris sont délimités par les caractères ``/*`` et ``*/`` sur plusieurs lignes ou commencent pas les caractères ``//`` sur une même ligne.

Typage des variables
--------------------

Le type d'une variable doit être renseigné à sa déclaration.

Quelques types disponibles :

========== ===================== =================
Type       Description           Valeurs
========== ===================== =================
``int``    entier sur 16 bits    -32768 à 32767
``long``   entier sur 32 bits    -2147483648 à 2147483647
``float``  flottant sur 32 bits  -3.4028235E+38 à -3.4028235E+38 ;
``char``   caractère sur 8 bits  Table ASCII 
========== ===================== =================


Exemples :

.. code:: arduino

    int a = 5;
    float pi = 3.14;
    char c = 'A';

Constantes prédéfinies
----------------------

Afin d'améliorer la lecture du code, des constantes sont définies.

================ ==================================
Constante        Valeur
================ ==================================
``LOW``          0 (niveau logique)
``HIGH``         1 (niveau logique)
``OUTPUT``       broche en sortie
``INPUT``        broche en entrée
``LED_BUILTIN``  ``13`` (numéro de broche de la LED intégrée)
================ ==================================

Structure du programme
----------------------

Un progamme Arduino respecte toujours une **structure spécifique** composée en trois parties :

    * Les déclarations : **définitions** des constantes et des variables ;
    * La fonction ``setup()`` : **configuration** de la carte (entrées, sorties, port série, ...) ;
    * La fonction ``loop()`` : **instructions du programme exécutées** dans une **boucle infinie** (sans fin).
   