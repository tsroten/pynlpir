Tutorial
========

Now that you have :doc:`PyNLPIR installed <installation>`, let's look at how to use it.

There are two ways to use PyNLPIR: directly using the :mod:`ctypes` interface provided by PyNLPIR or using PyNLPIR's helper functions. The :mod:`ctypes` interface is more extensive, but more rigid. The helper functions are easy-to-use, but don't provide access to every NLPIR function. You can also use a mixture of the two methods. First, let's look at the helper functions.

PyNLPIR Helper Functions
------------------------

The helper functions are located in PyNLPIR's ``__init__.py`` file, so they are accessible by importing :mod:`pynlpir` directly.

Initializing NLPIR
~~~~~~~~~~~~~~~~~~

Importing PyNLPIR loads the NLPIR API library automatically:

.. code:: python

    import pynlpir

Once it's imported, call :func:`~pynlpir.open` to tell NLPIR to open the
data files and initialize the API. See :func:`~pynlpir.open`'s documentation
for information on specifying a different data directory.

.. code:: python

    pynlpir.open()

By default, input is assumed to be unicode or UTF-8 encoded. If you'd like to use
a different encoding (e.g. GBK or BIG5), use the *encoding* keyword argument
when calling :func:`~pynlpir.open`:

.. code:: python

    pynlpir.open(encoding='big5')

.. TIP::

    No matter what encoding you've specified, you can always pass unicode strings to
    :mod:`pynlpir` functions.

PyNLPIR's helper functions always return unicode strings.

Once you've initialized NLPIR, you can start segmenting and analyzing text.

Segmenting Text
~~~~~~~~~~~~~~~

Let's segment a lengthy sentence:

.. code:: python

    s = 'NLPIR分词系统前身为2000年发布的ICTCLAS词法分析系统，从2009年开始，为了和以前工作进行大的区隔，并推广NLPIR自然语言处理与信息检索共享平台，调整命名为NLPIR分词系统。'
    pynlpir.segment(s)

    # Sample output: [('NLPIR', 'noun'), ('分词', 'verb'), ('系统', 'noun'), ('前身', 'noun'), ('为', 'preposition'), ('2000年', 'time word'), ('发布', 'verb'), . . . ]

If you don't want part of speech tagging, call :func:`~pynlpir.segment` with
*pos_tagging* set to ``False``:

.. code:: python

    pynlpir.segment(s, pos_tagging=False)

    # Sample output: ['NLPIR', '分词', '系统', '前身', '为', '2000年', '发布', . . . ]

You can also customize how the part of speech tags are shown. By default,
only the most generic part of speech name is used, i.e. the parent (for example,
``'noun'`` instead of ``'transcribed toponym'``). If you'd like the
most specific part of speech name instead, i.e. the child, set *pos_names*
to ``'child'``:

.. code:: python

    pynlpir.segment(s, pos_names='child')

If you want even more information about the part of speech tags, you can set
*pos_names* to ``'all'`` and a part of speech hierarchy is returned (for example,
``'noun:toponym:transcribed toponym'``):

.. code:: python

    pynlpir.segment(s, pos_names='all')

By default, part of speech tags are returned in English. If you'd like to see Chinese
instead (e.g. ``'名词'`` instead of ``'noun'``), set *pos_english* to ``False``:

.. code:: python

    pynlpir.segment(s, pos_english=False)

Getting Key Words
~~~~~~~~~~~~~~~~~

Another useful function is :func:`~pynlpir.get_key_words`:

.. code:: python

    pynlpir.get_key_words(s, weighted=True)
    [('NLPIR', 2.08), ('系统', 1.74)]

:func:`~pynlpir.get_key_words` analyzes the given Chinese text string and returns
words that NLPIR considers key words. If *weighted* is ``True``, then the key word's
weight is also returned as a ``float``.

Closing the API
~~~~~~~~~~~~~~~

Now that we've looked at a brief introduction to PyNLPIR's helper functions, let's look
at how to close the API.

When you're done using PyNLPIR, you can free up allocated memory by calling
:func:`~pynlpir.close`:

.. code:: python

    pynlpir.close()

:mod:`ctypes` NLPIR Interface
-----------------------------

:mod:`pynlpir.nlpir` provides access to NLPIR's C functions via :mod:`ctypes`.
You can call them directly without bothering with the helper functions above.
These functions work almost exactly the same as their C counterparts.

:mod:`pynlpir.nlpir` includes the module-level constants exported by NLPIR that
are needed for calling many of its functions (e.g. encoding and part of speech
constants). See the API page on :mod:`pynlpir.nlpir` for more information.

The sections below do not provide a comprehensive explanation of how to use NLPIR.
NLPIR has its own documentation. The section below provides basic information about
how to get started with PyNLPIR assuming you are familiar with NLPIR. If you're not,
be sure to check out the documentation linked to below.

Initializing and Exiting the API
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before you can call any other NLPIR functions, you need to initialize the NLPIR API.
This is done by calling :func:`~pynlpir.nlpir.Init`. You have to specify where
NLPIR's ``Data`` directory is. PyNLPIR ships with a copy and it's found in the 
top-level of the package directory. So, you can use the module-level constant
:data:`~pynlpir.nlpir.PACKAGE_DIR` when calling :func:`~pynlpir.nlpir.Init`:

.. code:: python

    from pynlpir import nlpir

    nlpir.Init(nlpir.PACKAGE_DIR)

NLPIR defaults to using GBK encoding. If you don't plan on passing around GBK-encoded
strings, you'll want to change the encoding when calling :func:`~pynlpir.nlpir.Init`:

.. code:: python

    nlpir.Init(nlpir.PACKAGE_DIR, nlpir.UTF8_CODE)

Once NLPIR is initialized, you can begin using the rest of the NLPIR functions. When
you're finished, it's good to call :func:`~pynlpir.nlpir.Exit` in order to exit the
NLPIR API and free the allocated memory:

.. code:: python

    nlpir.Exit()

The Rest of the NLPIR Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For a complete list of NLPIR functions that :mod:`pynlpir.nlpir` includes,
check out the :doc:`api`. NLPIR's documentation is included in a PDF file in
the `NLPIR/ICTCLAS 2016 download <http://ictclas.nlpir.org/downloads>`_.
Consult it for detailed information on how to use NLPIR.

What's Next
-----------

Now that you've finished the tutorial, you should be able to perform basic tasks
using PyNLPIR. If you need more information regarding a module, constant, or function,
be sure to check out the :doc:`api`. If you need help, spot a bug, or have a feature
request, then please visit
`PyNLPIR's GitHub Issues page <https://github.com/tsroten/pynlpir/issues>`_.
