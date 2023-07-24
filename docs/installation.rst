Installation
============

Installing PyNLPIR is easy. You can use
`pip <https://pip.pypa.io>`_:

.. code:: bash

    $ pip install pynlpir

That will download PyNLPIR from
`the Python Package Index <https://pypi.python.org/>`_ and install it in your
Python's ``site-packages`` directory.

Tarball Release
---------------

If you'd rather install PyNLPIR manually:

1. Download the most recent release from `PyNLPIR's PyPi page <https://pypi.python.org/pypi/pynlpir/>`_.
2. Unpack the tarball.
3. From inside the directory ``pynlpir-XX``, run ``pip install .``

That will install PyNLPIR in your Python's ``site-packages`` directory.

Install the Development Version
-------------------------------

`PyNLPIR's code <https://github.com/tsroten/pynlpir>`_ is hosted at GitHub.
To install the development version first make sure `Git <https://git-scm.org/>`_
is installed. Then run:

.. code-block:: bash
   
    $ git clone git://github.com/tsroten/pynlpir.git
    $ pip install -e pynlpir

This will link the ``pynlpir`` directory into your ``site-packages``
directory.

Running the Tests
-----------------

Running the tests is easy. Make sure you have `hatch <https://hatch.pypa.io>`_
installed.

.. code-block:: bash

    $ hatch run test
