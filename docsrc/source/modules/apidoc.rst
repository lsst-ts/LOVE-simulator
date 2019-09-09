ApiDoc
=======

These are the ApiDocs of the project.

The project is subdivided in 2 main modules:

  - :code:`simulator`: defines a set of remotes that send commands through SAL to simulated (or real) instances of different CSCs
  - :code:`csc-sim`: defines a set of controllers that simulate different CSCs. These controllers receive commands from the remotes defined in :code:`simulator`

In a typical deployment, there is an instance of the LOVE-simulator (built from, the :code:`simulator` modules) and 1 instance of each (simulated) CSC defined in the :code:`csc-sim` module.

.. toctree::
   :maxdepth: 4

   ../apidoc/simulator/modules.rst
   ../apidoc/csc-sim/modules.rst
