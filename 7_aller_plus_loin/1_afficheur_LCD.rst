=============
Afficheur LCD
=============

Ce sont des afficheurs génériques de 32 caractères disposés sur 2 lignes. Ils ont la particularité d'être simple à mettre en œuvre. Il en existe deux types.



Afficheur LCD 16x2 sur port I2C
===============================

Principe
--------

Ce sont les mêmes afficheurs que précédement mais avec un port série de données (I2C) nécessitant moins de cables (4 en tout).

.. figure:: images/04_grove_rgb_lcd.jpg
   :width: 700
   :height: 525
   :scale: 50 %
   :alt:
   :align: center
   
   Module Grove - LCD RGB Backlight (image : http://wiki.seeedstudio.com)

Chaque afficheur utilise sa propre librairie (ex. ``rgb_lcd.h`` pour le Grove LCD RGB Backlight) en plus de la librairie ``wire.h`` qui est obligatoire pour la gestion du port I2C.

Montage
-------



.. figure:: images/04_grove_rgb_lcd_exemple.jpg
   :width: 700
   :height: 300
   :scale: 50 %
   :alt:
   :align: center
   
   Modules Grove (image : http://wiki.seeedstudio.com)

Programme en langage Arduino
----------------------------

Télécharger `ici <https://github.com/Seeed-Studio/Grove_LCD_RGB_Backlight>`_ le fichier ``Grove_LCD_RGB_Backlight-master.zip`` pour l'installation de la librairie ``rgb_lcd`` avant la compilation du programme.


.. code-block:: arduino

   /*
    * Exemple affichage sur LCD 2x16 RGB I2C Grove
    */


   #include <Wire.h>       // Importation librairie gestion port I2C
   #include "rgb_lcd.h"    // Importation librairie gestion afficheur LCD I2C Grove

   rgb_lcd lcd;            // Déclaration de l'afficheur

   const int colorR = 255; // Couleur fond écran
   const int colorG = 0;
   const int colorB = 0;

   void setup()
   {
       lcd.begin(16, 2);                      // Fixe 2 colonnes et 16 caractères/ligne
       lcd.setRGB(colorR, colorG, colorB);    // Fixe couleur de fond
       lcd.print("hello, world!");            // Affiche texte
       delay(1000);                           // Temporisation 1s
   }

   void loop()
   {
       lcd.setCursor(0, 1);                  // Déplace le curseur
       lcd.print(millis()/1000);             // Affiche le temps écoulé en s (timer interne)
       delay(100);                           // Temporisation 1s
   }


Pour les versions plus simple sans rétro-éclairage RGB :

.. figure:: images/04_grove_lcd_16x2.jpg
   :width: 701
   :height: 384
   :scale: 60 %
   :alt:
   :align: center
   
   Grove LCD 16x12 (image: http://wiki.seeedstudio.com)

.. code-block:: arduino

   /*
    * Exemple affichage sur LCD 2x16 I2C Grove sans RGB
    */

   #include <Wire.h>
   #include "rgb_lcd.h"

   rgb_lcd lcd;         // Déclation de l'afficheur LCD branché sur un port I2C

   void setup() 
   {
      lcd.begin(16, 2);  // Initialisation de l'afficheur LCD sur 2 lignes à 16 caractères
   }

   void loop() 
   {
      lcd.setCursor(0, 0);        // Placement du curseur
      lcd.print("Bonjour !");     // Affichage de la valeur de la tension
      delay(1000);                // Pause de 1000 ms
   }


Afficheur LCD 16x2 sur port parallèle
=====================================

Principe
--------

Le pilotage d'un afficheur LCD 16x2 nécessite de 6 broches numériques.
Pour éviter un câblage trop complexe, le plus simple est de fixer sur la carte de développement un "shield" afficheur.



.. figure:: images/04_eduicaduino_lcd_montage.png
   :width: 900
   :height: 600
   :scale: 50 %
   :alt:
   :align: center

   Afficheur Educaduino-Lab


.. Le logiciel Arduino met à disposition la librairie ``LiquidCrystal`` (installée par défaut) pour le pilotage ce type d'afficheur.



Programme en langage Arduino (C/C++)
------------------------------------

.. code-block:: arduino

   /*
    * Exemple d'utilisation d'un écran LCD 16x2 parallèle
    */

   #include <LiquidCrystal.h>        // Importation de la librairie LiquidCrystal

   LiquidCrystal lcd(12, 11, 5, 4, 3, 2);  // Brochage de l'afficheur

   void setup() {
     lcd.begin(16, 2);               // fixe le nombre de colonnes et de lignes de l afficheur
   }

   void loop() {
     lcd.setCursor(5,0);             // place le curseur à la colonne 5 et à la ligne 0
     lcd.print("Bonjour");           // Affiche un texte
     lcd.setCursor(0,1);             // place le curseur à la colonne 0 et à la ligne 1
     lcd.print("tout le monde !");   // Affiche un autre texte
   }

.. note::

   Il sera peut-être necessaire d'installer la librairie ``LiquidCrystal`` dans le logiciel Arduino.

En résumé
---------


========================================== =======================================
Instruction                                Description
========================================== =======================================
``#include <LiquidCrystal.h>``             Importe la librairie de gestion de l'afficheur LCD
``LiquidCrystal lcd(12, 11, 5, 4, 3, 2)``  Déclare l'afficheur en précisant les numéros de broches
``lcd.begin(16, 2)``                       Fixe le nombre de colonnes et de lignes de l'afficheur
``lcd.setCursor(col,line)``                Positionne le cuseur
``lcd.print(variable)``                    Affiche le contenu d'une variable à la position du curseur
========================================== =======================================
