.. |kohm| replace:: :math:`{k\Omega}`

Capteur résistif - CTN (seconde générale)
=========================================


.. topic:: Programme de seconde générale 2019 - Enseignement commun

   Mesurer une grandeur physique à l’aide d’un capteur électrique résistif. **Produire et utiliser une courbe d’étalonnage** reliant la résistance d’un système avec une grandeur d’intérêt (température, pression, intensité lumineuse, etc.).
   Utiliser un dispositif avec microcontrôleur et capteur.



Principe
--------

Un capteur résistif est un composant électronique dont la résistance varie en fonction de la grandeur physique à mesurer. 

Par exemple, une CTN est un **capteur résistif  à coefficient de température négatif**.


.. figure:: Images/CTN_Caracteristique_R(T).png
   :width: 843
   :height: 581
   :scale: 50 %
   :alt: 
   :align: center
   
   Courbe d'étalonnage d'une CTN 10k 

.. note::

   Pour 25°C la résistance mesurée est égale à 10 |kohm| !

Pour obtenir une tension qui varie en fonction de la résistance, donc de la température, la solution la plus simple est de **placer la CTN dans un pont diviseur de tension**.

.. image:: Images/CTN_Div_tension.png
   :width: 460
   :height: 340
   :scale: 50 %
   :alt: 
   :align: center

L'expression de la tension :math:`u` est donnée par la relation suivante :

.. math::

   {u = \dfrac{R}{R_0+R} \times V_{cc}}

En choisissant la résistance :math:`R_0=10\,k\Omega` (valeur de la résistance caractéristique de la CTN), l'évolution de la tension obtenue en fonction de la température est **partiellement linéarisée**.

.. figure:: Images/CTN_Caracteristique_Diviseur_tension.png
   :width: 843
   :height: 581
   :scale: 50 %
   :alt: 
   :align: center

   Évolution de la tension en fonction de la température pour :math:`R_0=10\,k\Omega`

Entre 0 et 40°C, il est donc possible de calculer la température à partir de la tension mesurée par la relation suivante :

.. math::

   T = \dfrac{u-b}{a}




Montage
-------

.. image:: Images/CTN_Montage.png
   :width: 634
   :height: 450
   :scale: 50 %
   :alt: 
   :align: center

Programme
---------

.. code-block:: arduino

   /*
    * Mesure d une température avec une CTN 10k (25°C)
    * placée dans un pont diviseur de tension avec
    * une résistance de 10k.
    */

   float tension;      // Tension mesurée sur A0
   int temperature;    // Température en °C
   float a = -0.0441;  // Coeff. directeur du modèle
   float b = 3.66;     // Ordonnée à l origine du modèle

   void setup() {
     Serial.begin(9600);  // Paramétrage du port série
   }

   void loop() {
     tension = analogRead(A0)*5.0/1023; // Lecture tension en V
     temperature = (tension-b)/a;       // Calcul température en °C
     Serial.print("U = ");              // Affichage dans moniteur série
     Serial.println(tension);
     Serial.print("T= ");
     Serial.println(temperature);
     delay(1000);                       // Temporisation d'une seconde
   }
   
A retenir
---------

Placer un **capteur résistif** (température, pression, lumière, ...) dans un **pont diviseur de tension** reste une solution simple d'interfacage avec un microcontrôleur.

Allez plus loin
---------------

Mesurer la résistance de la CTN
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Dans le pont diviseur de tension, la résistance de la CTN s'exprime par la relation suivante :

.. math::

   R = R_0 \times\dfrac{u}{V_{cc}-u}

.. code-block:: arduino

   /*
    * Mesure de la résistance d une CTN
    */
    
   #define Vcc 5       // Tension d'alimentation
   #define Ro  10000   // Résistance du pont

   float u;            // Tension CTN
   float R;            // Résistance CTN
    
    void setup() {
      Serial.begin(9600);  // Paramétrage du port série
   }
    
   void loop() {
      u = analogRead(A0)*5.0/1023;  // Lecture tension
      R = Ro * u/(Vcc-u);           // Calcul de la résistance
      Serial.print("U = ");         // Début affichage
      Serial.println(u);
      Serial.print("R = ");
      Serial.println(R);            // Fin affichage
      delay(1000);                  // Temporisation de 1s
   }

Mesure de la température avec la relation de Steinhart-Hart
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sur une grande plage de variation , la relation entre la température (en K) et la résistance de la CTN est :

.. math::

   \dfrac{1}{T} = A + B \times \ln(R) + C \times (\ln(R))^3

A, B et C sont les coefficients de Steinhart-Hart. Ils sont donnés par le constructeur
ou peuvent se déterminer expérimentalement à partir de trois points de mesure.

.. note::

   Un programme Python pour déterminer ces trois coefficients A, B et C est disponible sur `Wikipédia <https://fr.wikipedia.org/wiki/Relation_de_Steinhart-Hart>`_.

.. code-block:: arduino

   /*
    * Mesure de la température avec la relation de Steinhart-Hart
    */

   #define Vcc 5       // Tension d'alimentation
   #define Ro  10000   // Résistance du pont
   #define A   1.0832e-3
   #define B   2.1723e-4
   #define C   3.2770e-7

   float u;            // Tension CTN
   float R;            // Résistance CTN
   float logR;         // ln(R)
   float T;            // Température en °C


   void setup() {
      Serial.begin(9600);  // Paramétrage du port série
   }

   void loop() {
      u = analogRead(A0)*5.0/1023;                  // Lecture tension en V
      R = Ro * u/(Vcc-u);                           // Calcul de la résistance
      logR = log(R);                                // Calcul de ln(R)
      T = (1.0 / (A + B*logR + C*logR*logR*logR));  // Calcul de la température
      T = T - 273.15;                               // Conversion en °C
      Serial.print("R = ");                         // Début affichage
      Serial.println(R);
      Serial.print("T = ");
      Serial.println(T);                            // Fin affichage
      delay(1000);                                  // Temporisation de 1s
   }

Simplification de relation de Steinhart-Hart
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sur une plage de variation plus réduite de la température, la relation de Steinhart-Hart permet d'écrire :

.. math::

   R \approx R_0 \times e^{\beta(\frac{1}{T}-\frac{1}{T_0})}

* :math:`{R_0}` est la valeur de la résistance pour la température :math:`{T_0}`.

* :math:`{\beta}` (en K).

.. figure:: Images/CTN_Caracteristique_R(T)_modele.png
   :width: 811
   :height: 521
   :scale: 50 %
   :alt: 
   :align: center

La détermination de la température (en K) s'effectue à l'aide de la relation suivante :

.. math::

   \dfrac{1}{T} = \dfrac{1}{\beta}\times\ln(\dfrac{R}{R_0})+\dfrac{1}{T_0}






