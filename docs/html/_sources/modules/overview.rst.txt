==========================
Overview and configuration
==========================

The LOVE-simulator is part of the LSST Operation and Visualization Environment (L.O.V.E.) project and it is written in Python.
The LOVE-simulator defines a set of CSC simulation tools to be used for development/demonstration purposes. Therefore, it is only used in development deployment stacks and not in real operations.

In short, the LOVE-simulator is used to simulate some of the CSCs of the LSST, enabling the LOVE-producer to get simulated data through SAL:

.. image:: ../assets/Overview.svg

As shown in the figure above, there are different software instances interacting with SAL:

  - :code:`Simulator`: defines a set of remotes that send commands through SAL to simulated (or real) instances of different CSCs
  - :code:`ScriptQueue sim`: defines a set of controllers that simulate instances of ScriptQueues (can be more than 1 instance with different salindexes
  - :code:`ATDome sim`: defines a set of controllers that simulate instances of the ATDome
  - :code:`ATMCS sim`: defines a set of controllers that simulate instances of the ATMCS
  - :code:`TestCSC sim`: defines a set of controllers that simulate instances of the TestCSC
  - :code:`Watcher sim`: defines a set of controllers that simulate instances of the Watcher

In a typical deployment, there is an instance of the LOVE-simulator (built from, the :code:`simulator` module) and 1 instance of each (simulated) CSC defined in the :code:`csc-sim` module.
Some of the CSC simulators have been developed in separate repositories by LSST staff and repackaged/tweaked in this repository. This is done in order to fit LOVE's development and deployment strategies for easier usage.

The :code:`config.json` gives information of which CSCs and in which SAL topics (and their indices) to simulate. Environment variables are also read to configure other parameters.


Defining simulated CSCs with :code:`config.json`
================================================
The LOVE-simulator and simulated CSC instances read a :code:`config.json` file (located in the :code:`simulator/config/` folder) to create the instances of the simulation tools.
This file specifies for each CSC the SAL index and a "source" for the data. The "source" can be either:

- :code:`command_sim`: specifies that the data will be sent by a simulated CSC
- :code:`emitter` specifies that the data will be simulated with random values by the :code:`simulator` itself.

For example:

.. code-block:: json

    {
        "Test": [
            { "index": 1, "source": "command_sim" },
            { "index": 2, "source": "emitter" },
        ],
        "ScriptQueue": [
            { "index": 1, "source": "command_sim" },
            { "index": 2, "source": "command_sim" }
        ],
        "ATDome": [
          { "index": 1, "source": "command_sim" }
        ],
    }

configures the following instances:

- 1 instance of a "Test" CSC with salindex 1 that will be simulated using a CSC simulator
- 1 instance of a "Test" CSC with salindex 2 that will be simulated with random values by the :code:`simulator` itself.
- 2 instance of "ScriptQueue"s, with salindexes 1 and 2, that will be simulated using a ScriptQueue simulator
- 1 instance of an "ATDome" CSC with salindex 1 that will be simulated using an ATDome simulator


Environment variables
=====================
Two environment variables must be set to configure the simulators:

- :code:`LSST_DDS_DOMAIN`: Used by :code:`salobj` to filter SAL messages in the network.
- :code:`OSPL_URI`: Location of the :code:`ospl.xml` file that defines the network configuration.
