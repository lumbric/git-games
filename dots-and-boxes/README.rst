Dots and Boxes
==============

Rules
-----

`Dots and Boxes`_

.. _`Dots and Boxes`: https://en.wikipedia.org/wiki/Dots_and_Boxes


How to play
-----------

Preparation:

- fork this repository (or clone and push to your own GIT server)
- add other player(s) as collaborators to the fork (or allow pushing to your remote)
- clone the fork to your local machine

Playing:

- choose a color: ``R`` or ``Y``
- edit the text file ``board``, add stones of your color to the tiles - note that there is gravity!
- commit your move (the commit message is not important, but following conventions_ is appreciated - bonus points if you can make your opponent laugh or cry with an extraordinary creative message!)
- push your commit to your fork/your remote
- next player fetches changes by running ``git pull``
- check for forced pushes and invalid moves
- re-do the previous 6 steps until one of the players wins

.. _conventions: https://chris.beams.io/posts/git-commit/

Finalizing:

- clean the board by running ``git checkout master connect-four/board``
- add the winner to the wall of fame in the README.rst_
- create a pull request (adds wall of fame and all moves)

.. _README.rst: ../README.rst
