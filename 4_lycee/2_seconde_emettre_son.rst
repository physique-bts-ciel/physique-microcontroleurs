====================================
Émission d'un son (seconde générale)
====================================

.. topic:: Programme de seconde générale 2019 - Enseignement commun

   Utiliser un dispositif comportant un microcontrôleur pour produire un signal sonore.

Principe
========

Certains microcontrôleurs (Arduino et Micro:bit) ne possédant pas de sortie analogique (CNA) pour générer des tensions sinusoïdales,
une méthode simple pour produire un son est de générer une tension carrée (entre 0 et Vcc) de fréquence f à l'entrée d'un haut-parleur.

Le son obtenu par cette technique n'est pas pur car il comporte des harmoniques aux fréquences 3f, 5f, 7f, ...

.. warning::

   Pour les faibles fréquences, le son devient "métallique" avec la présence importante d'harmoniques !


Méthode 1 : construire le signal carré
======================================

Arduino (C/C++)
---------------

.. image:: Images/Son_Piezo.png
   :width: 514
   :height: 418
   :scale: 60 %
   :alt: 
   :align: center

.. code-block:: arduino

   #define brocheHP 8
                            
   float frequence=440;                             
   float periode=1/frequence;

   void setup(){           
       pinMode(brocheHP, OUTPUT); 
   }

   void loop(){          
     digitalWrite(brocheHP,HIGH);               
     delayMicroseconds(1000000*periode/2.0);  
     digitalWrite(brocheHP,LOW);               
     delayMicroseconds(1000000*periode/2.0);  
   }

Arduino (Python/Nanpy)
----------------------

PyBoard (MicroPython)
---------------------

Micro:bit (MicroPython)
-----------------------


Méthode 2 : avec la fonction ``tone()``
=======================================

Arduino (C/C++)
---------------

.. code-block:: arduino

   /*
    * Génération d un son
    */

   #define Do3 262
   #define Re3 294
   #define Mi3 330
   #define Fa3 349
   #define Sol3 392
   #define La3 440
   #define Si3 494

   #define brocheHP 8

   void setup() {
     pinMode(brocheHP,OUTPUT);
     tone(brocheHP,La3,4000);
   }

   void loop() {
   }

Arduino (Python/Nanpy)
----------------------

PyBoard (MicroPython)
---------------------

Micro:bit (MicroPython)
-----------------------

Applications
============

* Hauteur d'un son (relation entre fréquences et notes).

* Générer une mélodie à partir de plusieurs notes.

