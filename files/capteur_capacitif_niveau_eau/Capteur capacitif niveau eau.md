# Capteur capacitif niveau eau

## Principe

- 4 plaques époxy.

## Étalonnage

| d (cm) | C (nF) |
| ------ | ------ |
| 2      | 0.97   |
| 4      | 1.49   |
| 6      | 2.00   |
| 8      | 2.61   |
| 10     | 3.14   |
| 12     | 3.73   |
| 14     | 4.15   |

## Réponse à un échelon

Résistance série :

$$
R = 100~{\rm k\Omega}
$$

Constante de temps :

$$
\tau_{min} = R\times C_{min} = 100\cdot10^3\times1,0\cdot10^{-9} = 100~\rm µs 
$$

$$
\tau_{max} = R\times C_{max} = 100\cdot10^3\times5,0\cdot10^{-9} = 500~\rm µs 
$$

## Mesure de la constante avec Arduino UNO

- Résolution de $4~\rm µs$ pour la fonction `micros()` sur un Arduino UNO R3 !

$$
N = \dfrac{500}{4} = 125~\rm points
$$

- Temps d'exécution de $100~\rm µs$ pour la fonction `analogRead()`  !


