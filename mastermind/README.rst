Mastermind
==========

Rules
-----

One player chooses a secret combination of four colors picked (available
colors: ``r``, ``b``, ``g``, ``v``, ``o``, ``y``). The other player has to
guess the secret color combination with maximum 12 tries. After each try the
number of correctly guessed colors and correctly guess colors and positions are
revealed.


How to play
-----------

Preparation:

- fork this repository (or clone and push to your own GIT server)
- add other player(s) as collaborators to the fork (or allow pushing to your remote)
- clone the fork to your local machine
- one player picks a secret color combination and adds it on the board
- commit the board in a secret branch ``secret`` and **do not push it**
- add the sha1 of the commit to the ``board`` in a public branch and push it

Playing:

- edit the text file ``board`` in the public branch and try guessing colors starting in row 1
- commit your guess (the commit message is not important, but following conventions_ is appreciated - bonus points if you can make your opponent laugh or cry with an extraordinary creative message!)
- push your commit to your fork/your remote
- the other player fetches the last guess by running ``git pull``
- check for forced pushes to avoid cheating
- add the number of correctly guessed colors/positions using ``o`` or only colors using ``.``
- commit (not in the ``secret`` branch!) and push board
- re-do the these steps until the secret color combination is correctly guessed

.. _conventions: https://chris.beams.io/posts/git-commit/

Finalizing:

- merge the ``secret`` branch into the public branch and push, note that you'll need to fix a merge conflict
- the other play may now verify the commit hash from the beginning of the game
- clean the board by running ``git checkout master mastermind/board``
- add the winner to the wall of fame in the README.rst_
- create a pull request (adds wall of fame and all moves)

.. _README.rst: ../README.rst
