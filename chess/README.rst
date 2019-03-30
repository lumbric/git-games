Chess
=====

Rules
-----

Well, it's chess... :)


How to play
-----------

Preparation:

- fork this repository (or clone and push to your own GIT server)
- add other player(s) as collaborators to the fork (or allow pushing to your remote)
- clone the fork to your local machine

Playing:

- choose a black or white
- edit the text file ``board``, move pieces by copy & paste
- commit your move (the commit message is not important, but following conventions_ is appreciated - bonus points if you can make your opponent laugh or cry with an extraordinary creative message!)
- push your commit to your fork/your remote
- next player fetches changes by running ``git pull``
- check for forced pushes and invalid moves
- re-do the previous 6 steps until one of the players wins

.. _conventions: https://chris.beams.io/posts/git-commit/

Finalizing:

- clean the board by running ``git checkout master chess/board``
- add the winner to the wall of fame in the README.rst_
- create a pull request (adds wall of fame and all moves)

.. _README.rst: ../README.rst
