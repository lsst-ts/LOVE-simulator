========
Overview
========

The LOVE-simulator is part of the LSST Operation and Visualization Environment (L.O.V.E.) project and it is written in Python.
The LOVE-simulator defines a set of CSC simulation tools to be used for development/demonstration purposes. Therefore, it is only used in development deployment stacks and not in real operations.

In short, the LOVE-simulator is used to simulate some of the CSCs of the LSST, enabling the LOVE-producer to get simulated data through SAL:

.. image:: ../assets/Simulator_Overview.svg

As shown in the figure above, there are different software instances interacting with SAL:

  - :code:`Simulator`: defines a set of remotes that send commands through SAL to simulated (or real) instances of different CSCs
  - :code:`CSC sim`: defines a set of controllers that simulate different CSCs. These controllers receive commands from the remotes defined in :code:`simulator`. They are used to simulate some of the LSST CSCs in order to display statuses in the CSC SUmmary display.
  - :code:`ScriptQueue sim`: defines a set of controllers that simulate instances of ScriptQueues (can be more than 1 instance with different salindexes.
  - :code:`ATDome sim`: defines a set of controllers that simulate instances of ATDomes

In a typical deployment, there is an instance of the LOVE-simulator (built from, the :code:`simulator` module) and 1 instance of each (simulated) CSC defined in the :code:`csc-sim` module.
Some of the CSC simulators have been developed in separate repositories by LSST staff and repackaged/tweaked in this repository. This is done in order to fit LOVE's development and deployment strategies for easier usage.
