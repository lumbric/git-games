Tic-tac-toe
===========


Rules
-----

    Tic-tac-toe (American English), noughts and crosses (British English) or Xs
    and Os, is a paper-and-pencil game for two players, X and O, who take turns
    marking the spaces in a 3×3 grid. The player who succeeds in placing three
    of their marks in a horizontal, vertical, or diagonal row wins the game.

Source: https://en.wikipedia.org/wiki/Tic-tac-toe


How to play
-----------

Preparation:

- fork this repository (or clone and push to your own GIT server)
- add other player(s) as collaborators to the fork (or allow pushing to your)
- clone the fork to your local machine

Playing:

- choose a player symbol `X` or `O`
- edit the text file `board` and replace a character `.` by your player symbol
- commit your move (the commit message is not important, but following conventions is appreciated)
- push your commit
- next player fetches changes by running `git pull`
- check for forced pushes and invalid moves
- re-do the previous 6 steps until one of the players wins

Finalizing:

- clean the board by running `git checkout master tic-tac-toe/board`
- add the winner to the wall of fame in the README.rst_
- create a pull request (adds wall of fame and all moves)

.. _README.rst: ../README.rst
