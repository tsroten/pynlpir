.. PyNLPIR documentation master file, created by
   sphinx-quickstart on Thu Mar 27 17:10:46 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to PyNLPIR's documentation!
===================================

PyNLPIR is a Python wrapper around the
`NLPIR/ICTCLAS Chinese segmentation software <http://nlpir.org>`_.

PyNLPIR allows you to easily segment Chinese text using NLPIR,
one of the most widely-regarded Chinese text analyzers:

.. code:: python

    import pynlpir
    pynlpir.open()

    s = '欢迎科研人员、技术工程师、企事业单位与个人参与NLPIR平台的建设工作。'
    pynlpir.segment(s)

    [('欢迎', 'verb'), ('科研', 'noun'), ('人员', 'noun'), ('、', 'punctuation mark'), ('技术', 'noun'), ('工程师', 'noun'), ('、', 'punctuation mark'), ('企事业', 'noun'), ('单位', 'noun'), ('与', 'conjunction'), ('个人', 'noun'), ('参与', 'verb'), ('NLPIR', 'noun'), ('平台', 'noun'), ('的', 'particle'), ('建设', 'verb'), ('工作', 'verb'), ('。', 'punctuation mark')]

If this is your first time using PyNLPIR, check out :doc:`installation`. Then read
the :doc:`tutorial`.

If you want a more in-depth view of PyNLPIR, check out the :doc:`api`.

If you're looking to help out, check out :doc:`contributing`.


Support
-------

If you encounter a bug, have a feature request, or need help using PyNLPIR, then use
`PyNLPIR's GitHub Issues page <https://github.com/tsroten/pynlpir/issues>`_ to send
feedback.


Documentation Contents
----------------------

.. toctree::
   :maxdepth: 2

   installation
   tutorial
   api
   contributing
   history
   authors
