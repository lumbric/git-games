.. image:: https://img.shields.io/github/license/lumbric/git-games.svg
  :alt: MIT License  

git-games
=========

**git-games** is a collection of (mostly classical board or paper and pencil) games which can be played by using GIT for educational purposes. It might be more fun to play these games with paper an pencil, but less fun to learn GIT or test GIT commands without playing these games! :)


How to play
-----------

Playing involves roughly the following steps:

- fork this repository (or clone and push to your own GIT server)
- add other player(s) as collaborators to the fork :sup:`1` (or allow pushing to your remote)
- clone the fork to your local machine
- play the game by editing files, committing and pushing
- clean the board to original state
- add the winner to the wall of fame in table below
- create a pull request (adds wall of fame and all moves)

Cheating is highly appreciated! If you can trick your opponent, the victory is yous. See Security_ for more details.

**Detailed instructions can be found in the README.rst for each game.**

:sup:`1` In theory you could also accept pull requests for every move for your opponents, but this will make the game pretty chaotic.

Games
-----

- Tic-tac-toe_
- Chess_
- `Connect Four`_
- Mastermind_

.. _Tic-tac-toe: tic-tac-toe/README.rst
.. _Chess: chess/README.rst
.. _`Connect Four`: connect-four/README.rst
.. _`Mastermind`: mastermind/README.rst


Wall of fame
------------

+----------------------+------------+---------------+
| Game                 | Winner     | Other players |
+======================+============+===============+
| Tic-tac-toe_         |  Doris     |  Kathi        |
+----------------------+------------+---------------+


Security
--------

Your opponent might rewrite the history and trick you in this way. To avoid
this, you can run ``git fetch`` first and check the difference between
``origin/your_branch`` and ``your_branch`` before you merge
``origin/your_branch`` in ``your_branch``. Git warns in case of forced pushes,
but this warning is easy to overlook. If you want to make a fetch fail in case
of a forced push, you can remove the ``+`` in the Git config in
``remote.fetch``. If you own the remote you might be able to block forced
pushes on server side, for example with Gerrit or `Github Enterprise`.

In order to guarantee authenticated entries in the wall of fame, we would like
to ask to `sign the commit`_ which modifies the wall of fame. Ideally the
winner modifies the wall of fame, signs it and all opponents add a signed dummy
commit on top (e.g. only white-space changes) to confirm that the winner did
not cheat and modify the history before creating the pull request. You can
easily create signed commits (using Github's GPG key) by editing and committing
a file using `Github`_'s web interface.

.. _`Github Enterprise`: https://help.github.com/en/enterprise/2.15/admin/developer-workflow/blocking-force-pushes-to-a-repository
.. _`sign the commit`: https://git-scm.com/book/en/v2/Git-Tools-Signing-Your-Work
.. _`Github`: https://help.github.com/en/articles/signing-commits


Inspiration for more games in future
------------------------------------

- https://en.wikipedia.org/wiki/Ultimate_tic-tac-toe
- https://en.wikipedia.org/wiki/Order_and_Chaos
- https://en.wikipedia.org/wiki/Paper-and-pencil_game
