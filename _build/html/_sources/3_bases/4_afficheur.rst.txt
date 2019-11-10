Afficheur LCD
=============

Ce sont généralement des afficheurs génériques de 32 caractères disposés sur 2 lignes. Ils ont la particularité d'être simple à mettre en œuvre.

Afficheur LCD 16x2 (port parallèle)
-----------------------------------

Principe
~~~~~~~~

Le pilotage d'un afficheur LCD 16x2 nécessite de 6 broches numériques.

Pour éviter un câblage trop complexe, le plus simple est de fixer sur la carte de développement un "shield" afficheur.

.. figure:: images/04_eduicaduino_lcd.png
   :width: 700
   :height: 400
   :scale: 40 %
   :alt:
   :align: center
   
   Afficheur Educaduino-Lab (image: Eurosmart)


Le logiciel Arduino dipose de la librairie ``LiquidCrystal`` (installée par défaut) pour piloter ce type d'afficheur.

Montage
~~~~~~~

Programme
~~~~~~~~~

.. code:: arduino

   /*
   Exemple d utilisation d'un écran LCD 16x2 parallèle
   */

   #include <LiquidCrystal.h>      // Importation de la librairie LiquidCrystal

   LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

   void setup() {
     lcd.begin(16, 2);             // fixe le nombre de colonnes et de lignes de l afficheur
   }

   void loop() {
     lcd.setCursor(5,0);           // place le curseur à la colonne 5 et à la ligne 0
     lcd.print("Bonjour");         // Affiche un texte
     lcd.setCursor(0,1);           // place le curseur à la colonne 0 et à la ligne 1
     lcd.print("tout le monde !"); 
   }

A retenir
~~~~~~~~~


========================================== =======================================
Instruction                                Description
========================================== =======================================
``#include <LiquidCrystal.h>``             Importe la librairie de gestion de l'afficheur LCD
``LiquidCrystal lcd(12, 11, 5, 4, 3, 2)``  Déclare l'afficheur en précisant les numéros de broches
``lcd.begin(16, 2)``                       Fixe le nombre de colonnes et de lignes de l'afficheur
``lcd.setCursor(col,line)``                Positionne le cuseur
``lcd.print(variable)``                    Affiche le contenu d'une variable à la position du curseur
========================================== =======================================


Afficheur LCD 16x2 (I2C)
------------------------

Principe
~~~~~~~~

Ce sont les mêmes afficheurs que précédement mais avec un port série de données (I2C) nécessitant moins de cables (4 en tout) !

.. figure:: images/04_grove_rgb_lcd.jpg
   :width: 700
   :height: 525
   :scale: 50 %
   :alt:
   :align: center
   
   Module Grove - LCD RGB Backlight (image : http://wiki.seeedstudio.com)

Chaque afficheur utilise sa propre librairie (ex. ``rgb_lcd.h`` pour le Grove LCD RGB Backlight) en plus de la librairie ``wire.h`` qui est obligatoire pour la gestion du port I2C.

Montage
~~~~~~~



.. figure:: images/04_grove_rgb_lcd_exemple.jpg
   :width: 700
   :height: 300
   :scale: 50 %
   :alt:
   :align: center
   
   Modules Grove (image : http://wiki.seeedstudio.com)

Programme
~~~~~~~~~

.. code:: arduino

   #include <Wire.h>
   #include "rgb_lcd.h"
   
   rgb_lcd lcd;
   
   const int colorR = 255;
   const int colorG = 0;
   const int colorB = 0;
   
   void setup() 
   {
       // set up the LCD's number of columns and rows:
       lcd.begin(16, 2);

       lcd.setRGB(colorR, colorG, colorB);

       // Print a message to the LCD.
       lcd.print("hello, world!");

       delay(1000);
   }

   void loop() 
   {
       // set the cursor to column 0, line 1
       // (note: line 1 is the second row, since counting begins with 0):
       lcd.setCursor(0, 1);
       // print the number of seconds since reset:
       lcd.print(millis()/1000);

       delay(100);
   }



