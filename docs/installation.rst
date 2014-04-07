Installation
============

Installing PyNLPIR is simple. PyNLPIR is designed to run on Python 2.7 or 3. Because of the included NLPIR library files, it only runs on Windows or GNU/Linux.

Pip
---

Install PyNLPIR using `pip <http://www.pip-installer.org/>`_:

.. code-block:: bash

    $ pip install pynlpir

This will download PyNLPIR from
`the Python Package Index <http://pypi.python.org/>`_ and install it in your
Python's ``site-packages`` directory.

Install from Source
-------------------

If you'd rather install PyNLPIR manually:

1.  Download the most recent release from `PyNLPIR's PyPi page <http://pypi.python.org/pypi/pynlpir>`_.
2. Unpack the archive file.
3. From inside the directory ``PyNLPIR-XX``, run ``python setup.py install``

This will install PyNLPIR in your Python's ``site-packages`` directory.

Install the Development Version
-------------------------------

`PyNLPIR's code <https://github.com/tsroten/pynlpir>`_ is hosted at GitHub.
To install the development version first make sure `Git <http://git-scm.org/>`_
is installed. Then run:

.. code-block:: bash
   
    $ git clone git://github.com/tsroten/pynlpir.git
    $ pip install -e pynlpir

This will link the ``PyNLPIR`` directory into your ``site-packages``
directory.

Running the Tests
-----------------

Running the tests is easy. After downloading and unpacking PyNLPIR's source,
run the following code from inside PyNLPIR's source directory:

.. code-block:: bash

    $ python setup.py test

If you want to run the tests using different versions of Python, install and
run tox:

.. code-block:: bash

    $ pip install tox
    $ tox
