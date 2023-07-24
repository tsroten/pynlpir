=======
PyNLPIR
=======

.. image:: https://badge.fury.io/py/pynlpir.svg
    :target: https://pypi.org/project/pynlpir

.. image:: https://github.com/tsroten/pynlpir/actions/workflows/ci.yml/badge.svg
    :target: https://github.com/tsroten/pynlpir/actions/workflows/ci.yml

PyNLPIR is a Python wrapper around the
`NLPIR/ICTCLAS Chinese segmentation software <http://www.nlpir.org/wordpress/>`_.

* Documentation: https://tsroten.github.io/pynlpir/
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
* Includes a copy of NLPIR
* Supports macOS (Intel), Linux, and Windows

Getting Started
---------------

* `Install PyNLPIR <https://tsroten.github.io/pynlpir/installation.html>`_

  * ``pip install pynlpir`` to install PyNLPIR
  * ``pynlpir update`` to download the latest license

* Read `PyNLPIR's tutorial <https://tsroten.github.io/pynlpir/tutorial.html>`_
* Learn from the `API documentation <https://tsroten.github.io/pynlpir/api.html>`_
* `Contribute <https://tsroten.github.io/pynlpir/contributing.html>`_ documentation, code, or feedback