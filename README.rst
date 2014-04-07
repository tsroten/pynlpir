PyNLPIR
=======

PyNLPIR is a Python wrapper for the
`NLPIR/ICTCLAS Chinese segmentation software <http://nlpir.org>`_.

Easily segment text using NLPIR, one of the most widely-regarded Chinese text
analyzers:

.. code:: python

    import pynlpir
    pynlpir.open()

    s = '欢迎科研人员、技术工程师、企事业单位与个人参与NLPIR平台的建设工作。'
    pynlpir.segment(s)

    [('欢迎', 'verb'), ('科研', 'noun'), ('人员', 'noun'), ('、', 'punctuation mark'), ('技术', 'noun'), ('工程师', 'noun'), ('、', 'punctuation mark'), ('企事业', 'noun'), ('单位', 'noun'), ('与', 'conjunction'), ('个人', 'noun'), ('参与', 'verb'), ('NLPIR', 'noun'), ('平台', 'noun'), ('的', 'particle'), ('建设', 'verb'), ('工作', 'verb'), ('。', 'punctuation mark')]

Features
--------

* Helper functions for common use cases
* English/Chinese part of speech mapping
* Support for UTF-8, GBK, and BIG5 encoded strings (and unicode of course!)
* Access to NLPIR's C functions via ``ctypes``
* No third-party dependencies (PyNLPIR includes a copy of NLPIR)
* Runs on Python 2.7 and 3

Install
-------

NLPIR supports Windows and GNU/Linux. PyNLPIR will install, but not run, on other
platforms (e.g. OS X).

Just use `pip <http://www.pip-installer.org/>`_:

.. code:: bash

    $ pip install pynlpir

That's it! Everything is shipped with PyNLPIR -- there are no external dependencies.

Documentation
-------------

PyNLPIR has `documentation <http://pynlpir.readthedocs.org>`_. It features an
installation guide, tutorial, and API reference.

Support
-------

If you encounter a bug, have a feature request, or need help using PyNLPIR, then use
`PyNLPIR's GitHub Issues page <https://github.com/tsroten/pynlpir/issues>`_ to
get in touch.

License
-------

PyNLPIR is released under the OSI-approved
`MIT License <http://opensource.org/licenses/MIT>`_. See the file ``LICENSE.txt``
for more information. This license doesn't apply to the included copies of NLPIR's
data directory and shared libraries.
