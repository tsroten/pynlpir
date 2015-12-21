=======
PyNLPIR
=======

.. image:: https://badge.fury.io/py/pynlpir.png
    :target: http://badge.fury.io/py/pynlpir

.. image:: https://travis-ci.org/tsroten/pynlpir.png?branch=develop
        :target: https://travis-ci.org/tsroten/pynlpir

PyNLPIR is a Python wrapper around the
`NLPIR/ICTCLAS Chinese segmentation software <http://ictclas.nlpir.org>`_.

* Documentation: http://pynlpir.rtfd.org
* GitHub: https://github.com/tsroten/pynlpir
* Support: https://github.com/tsroten/pynlpir/issues
* Free software: `MIT license <http://opensource.org/licenses/MIT>`_

About
-----

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
* Supports OS X, Linux, and Windows

Getting Started
---------------

* `Install PyNLPIR <http://pynlpir.readthedocs.org/en/latest/installation.html>`_
* Read `PyNLPIR's tutorial <http://pynlpir.readthedocs.org/en/latest/tutorial.html>`_
* Learn from the `API documentation <http://pynlpir.readthedocs.org/en/latest/api.html>`_
* `Contribute <http://pynlpir.readthedocs.org/en/latest/contributing.html>`_ documentation, code, or feedback
