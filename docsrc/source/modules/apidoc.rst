..
    This file is part of LOVE-simulator.
..
    Copyright (c) 2023 Inria Chile.
..
    Developed by Inria Chile.
..
    This program is free software: you can redistribute it and/or modify it under 
    the terms of the GNU General Public License as published by the Free Software 
    Foundation, either version 3 of the License, or at your option any later version.
..
    This program is distributed in the hope that it will be useful,but WITHOUT ANY
    WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR 
    A PARTICULAR PURPOSE. See the GNU General Public License for more details.
..
    You should have received a copy of the GNU General Public License along with 
    this program. If not, see <http://www.gnu.org/licenses/>.


=======
ApiDoc
=======

These are the ApiDocs of the project.

As explained in the :ref:`Overview and configuration` section. The project is subdivided in 2 main modules:

  - :code:`simulator`: defines a set of remotes that send commands through SAL to simulated (or real) instances of different CSCs
  - :code:`csc_sim`: defines a set of controllers that simulate different CSCs. These controllers receive commands from the remotes defined in :code:`simulator`

.. toctree::
   :maxdepth: 4

   ../apidoc/simulator/modules.rst
   ../apidoc/csc_sim/modules.rst
