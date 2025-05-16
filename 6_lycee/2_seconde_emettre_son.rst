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

.. figure:: Images/Son_Piezo.png
   :width: 514
   :height: 418
   :scale: 60 %
   :alt: 
   :align: center

   Branchement d'un haut-parleur sur la broche 8

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

Cette méthode n'est pas applicable ici car le pilotage de l'Arduino par Nanpy est **trop lent** !

.. PyBoard (MicroPython)
.. ---------------------

.. Micro:bit (MicroPython)
.. -----------------------


Méthode 2 : utiliser une fonction spéciale
==========================================

Arduino (C/C++)
---------------

.. code-block:: arduino

   /*
   Exemple Arduino
   */
   #include "pitches.h"

   // notes in the melody:
   int melody[] = {NOTE_C4, NOTE_G3,NOTE_G3, NOTE_A3, NOTE_G3,0, NOTE_B3, NOTE_C4};

   // note durations: 4 = quarter note, 8 = eighth note, etc.:
   int noteDurations[] = {4, 8, 8, 4, 4, 4, 4, 4 };

   void setup() {
   for (int thisNote = 0; thisNote < 8; thisNote++) {
      int noteDuration = 1000/noteDurations[thisNote];
      tone(8, melody[thisNote],noteDuration);
      int pauseBetweenNotes = noteDuration * 1.30;
      delay(pauseBetweenNotes);
      noTone(8);
   }
   }

   void loop() {
   // Pas de boucle ici !
   }

Arduino (Python/Nanpy)
----------------------

La classe ``Note`` de Nanpy dispose des méthodes :

* ``play(fréquence, durée)`` pour jouer une note pendant un durée en ms ;
* ``stop()`` pour arrêter la lecture de la note.

.. code-block:: Python

   # Nanpy v0.96
   from nanpy import ArduinoApi, SerialManager, Tone
   from time import sleep                      

   port = SerialManager(device='/dev/ttyACM0')  # Sélection du port série (exemple : device = 'COM6')
   uno = ArduinoApi(connection=port)            # Déclaration de la carte Arduino Uno

   note =  [Tone.NOTE_C4, Tone.NOTE_G3, Tone.NOTE_G3, Tone.NOTE_A3,
            Tone.NOTE_G3, 0 , Tone.NOTE_B3, Tone.NOTE_C4]
   noteDuration = [4, 8, 8, 4,
                   4, 4, 4, 4]

   hp = Tone(8)                                 # Haut parleur sur broche 8

   for i in range(8):
      duree = 1000/noteDuration[i]              # durée en ms
      hp.play(note[i] , duree)                  # jouer la note
      sleep(1.3*duree*1E-3)                     # pause en les notes

   hp.stop()                                    # Arrêt de la lecture


.. note::

   Une méthode ``tone()`` équivalent à celle du langage Arduino a été ajoutée dans la version modifiée de Nanpy d'Eurosmart. 

.. code-block:: Python

   # Version modifiée de Nanpy par Eurosmart
   from nanpy import ArduinoApi, SerialManager, Tone
   from time import sleep                       
   
   port = SerialManager(device='/dev/ttyACM0')  # Sélection du port série (exemple : device = 'COM6')
   uno = ArduinoApi(connection=port)            # Déclaration de la carte Arduino Uno
   
   melody =  [Tone.NOTE_C4, Tone.NOTE_G3, Tone.NOTE_G3, Tone.NOTE_A3, Tone.NOTE_G3, 0 , Tone.NOTE_B3, Tone.NOTE_C4]
   noteDuration = [4, 8, 8, 4, 4, 4, 4, 4]
   
   pinHP = 8                          # Haut-parleur sur broche 8
   
   for i in range(8):
       duree = 1/noteDuration[i]      # durée en ms
       uno.tone(pinHP, melody[i])     # Lecture de la note      
       sleep(duree)                   # Attendre la lecture
       uno.noTone(pinHP)              # Arrêt de la note
       sleep(duree*1.3)               # Pause entre les notes


.. PyBoard (MicroPython)
.. ---------------------

.. Micro:bit (MicroPython)
.. -----------------------

Applications
============

* Hauteur d'un son (relation entre fréquences et notes).

* Générer une mélodie à partir de plusieurs notes.

