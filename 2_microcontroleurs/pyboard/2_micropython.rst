===================
Langage Micropython
===================

Pour de programmer la PyBoard en langage Python natif, un micrologiciel (firmware) contenant l'interpréteur MicroPython est installé dans la mémoire flash de la carte. Ce firmware peut-être mis à jour à partir d'une version plus récente disponible sur le site de `MicroPython <https://micropython.org/download>`_.

Les logiciels `Thonny <https://thonny.org/>`_ et `uPyCraft <https://github.com/DFRobot/uPyCraft>`_ exploitent pleinement la programmation des microcontrôleurs en MicorPython. Ils permettent deux types de programmation :

* directement dans l'interpréteur MicroPython (REPL) pour tester des instructions par exemple ;

* ou dans un script (fichier avec l'extension ``.py``) qui peut-être sauvegarder sur la mémoire de la carte pour être exécuté de façon autonome sur la carte.

.. warning::

   À chaque démarrage de la carte ou lors d'un reset, les fichiers ``setup.py`` puis ``main.py`` sont exécutés dans l'ordre. C'est dans le fichier ``main.py`` que doit être écrit le programme !