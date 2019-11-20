Mesurer une pression - Loi de Mariotte (première générale)
==========================================================

.. topic:: Programme de première générale 2019 - Enseignement de spécialité.

   Tester la loi de Mariotte, par exemple en utilisant un dispositif comportant un microcontrôleur.

Principe
--------

La manipulation consiste à vérifier la loi de Mariotte :math:`{P \times V = constante}` (à température et quantité de matière constantes).

La mesure de pression s'effectue avec un capteur de pression absolue du type MPX5700 (700 kPa - 5V). La tension de sortie est linéaire à la pression mesurée.

.. figure:: Images/pression_abs_MPX5700GP_700kPa_Farnell.fr.jpg
   :width: 290
   :height: 200
   :scale: 70 %
   :alt: 
   :align: center
   
   Capteur MPX5700GP (0 à 700 kPa) (image : farnell.fr)

.. figure:: Images/pression-grove-mpx5700ap-gotronic.jpg
   :width: 600
   :height: 600
   :scale: 50 %
   :alt: 
   :align: center
   
   Capteur MPX5700AP Grove (15 kPa à 700 kPa) (image : gotronic.fr)

Montage
-------

Le montage est composé d'une carte Educaduino Lab, d'un capteur de pression Educaduino (20 kPa à 400 kPa) et d'une seringue. L'expression de la pression (en kPa) en fonction de la tension délivrée par le cateur est :

.. math::

   P = 76 \times U + 20

.. image:: Images/pression_mariotte_montage_educaduino.JPG
   :width: 800
   :height: 400
   :scale: 70 %
   :alt: 
   :align: center

.. note::

   Dans cette manipulation, il est important de tenir compte du volume d'air :math:`{V_O}` présent dans le tube. La loi de Mariotte s'écrit alors 

   .. math::
      P \times (V+V_0) = constante

Programme
---------

.. code-block:: arduino
   :linenos:

   /*
    * Mesure d'une pression absolue
    * Capteur Educaduino 20 kPa à 400 kPa
    * branché sur la broche A9
    */

   #define brocheCapteur A9      // Numéro de broche connectée au capteur
   #include <LiquidCrystal.h>    // Librairie de gestion de l écran LCD

   LiquidCrystal lcd(12, 11, 5, 4, 3, 2);  // Déclaration de l écran LCD


   float tension ;               // Tension mesurée
   float pression ;              // Pression mesurée

   void setup() {
     lcd.begin(16, 2);           // Paramétrage de l ecran LCD

   }

   void loop() {
     tension = analogRead(brocheCapteur)*5.0/1023 ;   // Lecture de la tension
     pression = tension * 76 + 20 ;                   // Calcul de la pression en kPa
     lcd.clear();                                     // Début affichage
     lcd.setCursor(0,0);
     lcd.print("Pression en kPa");
     lcd.setCursor(0,1);
     lcd.print(pression);                             // Fin affichage
     delay(1000);
   }

Résultats
---------


======== ==== ==== ==== ==== ==== ==== ==== ==== ====
V (mL)   12   11   10   9    8    7    6    5    4
P (kPa)  96,5 105  114  124  136  152  171  194  227
======== ==== ==== ==== ==== ==== ==== ==== ==== ====

.. image:: Images/pression_mariotte_courbe.png
   :width: 640
   :height: 480
   :scale: 100 %
   :alt: 
   :align: center
