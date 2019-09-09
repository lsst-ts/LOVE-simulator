ApiDoc
=======

These are the ApiDocs of the project.

As explained in the :ref:`Overview` section. The project is subdivided in 2 main modules:

  - :code:`simulator`: defines a set of remotes that send commands through SAL to simulated (or real) instances of different CSCs
  - :code:`csc-sim`: defines a set of controllers that simulate different CSCs. These controllers receive commands from the remotes defined in :code:`simulator`
