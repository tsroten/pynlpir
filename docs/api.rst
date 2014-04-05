PyNLPIR API
===========

.. module:: pynlpir.nlpir

``pynlpir.nlpir``
-----------------

Provides a Python API to NLPIR/ICTCLAS.

.. data:: PACKAGE_DIR

    The absolute path to this package (used by NLPIR to find its ``Data`` directory).

.. data:: LIB_DIR

    The absolute path to this path's lib directory.

.. data:: libNLPIR

    A CDLL instance for the NLPIR API library.

.. function:: get_func(name, argtypes=None, restype=None, lib=libNLPIR)

    Retrieves the corresponding NLPIR function.

    :param str name: The name of the NLPIR function to get.
    :param list argtypes: A list of :mod:`ctypes` data types that correspond
        to the function's argument types.
    :param restype: A :mod:`ctypes` data type that corresponds to the
        function's return type (only needed if the return type isn't
        :class:`ctypes.c_int`).
    :param lib: A :class:`ctypes.CDLL` instance for the NLPIR API library where
        the function will be retrieved from (defaults to :data:`libNLPIR`).

.. function:: close

    Exits the NLPIR API and frees allocated memory. This calls the NLPIR
    function ``NLPIR_Exit``.

.. function:: segment(s, pos_tagging=True, pos_names=True, parents=False, english=True)

    Segment Chinese text *s* using NLPIR.

    The segmented tokens are returned as a list. Each item of the list is a
    string if *pos_tagging* is `False`, e.g. ``['我们', '是', ...]``. If
    *pos_tagging* is `True`, then each item is a tuple (``(token, pos)``), e.g.
    ``[('我们', 'pronoun'), ('是', 'verb'), ...]``.

    This uses the NLPIR function ``NLPIR_ParagraphProcess`` to segment *s*.

    :param s: The Chinese text to segment. *s* should be Unicode or a UTF-8
        encoded string.
    :param bool pos_tagging: Whether or not to include part of speech tagging
        (defaults to ``True``).
    :param pos_names: What type of part of speech names to return. This
        argument is only used if *pos_tagging* is ``True``. :data:`None`
        means only the original NLPIR part of speech code will be returned.
        Other than :data:`None`, *pos_names* may be one of ``'parent'``,
        ``'child'``, or ``'all'``. Defaults to ``'parent'``. ``'parent'``
        indicates that only the most generic name should be used, e.g.
        ``'noun'`` for ``'nsf'``. ``'child'`` indicates that the most specific
        name should be used, e.g. ``'transcribed toponym'`` for ``'nsf'``.
        ``'all'`` indicates that all names should be used, e.g.
        ``'noun:toponym:transcribed toponym'`` for ``'nsf'``.
    :type pos_names: ``str`` or :data:`None`
    :param bool english: Whether to use English or Chinese for the part
        of speech names, e.g. ``'conjunction'`` or ``'连词'``. Defaults to
        ``True``. This is only used if *pos_names* is ``True``.

.. function:: get_key_words(s, max_words=50, weighted=False)

    Determines key words in Chinese text *s*.

    The key words are returned in a list. If *weighted* is ``True``,
    then each list item is a tuple: ``(word, weight)``, where
    *weight* is a float. If it's *False*, then each list item is a string.

    This uses the NLPIR function ``NLPIR_GetKeyWords`` to determine the key
    words in *s*.

    :param s: The Chinese text to analyze. *s* should be Unicode or a UTF-8
        encoded string.
    :param int max_words: The maximum number of key words (up to ``50``) to
        find (defaults to ``50``).
    :param bool weighted: Whether or not to return the key words' weights.


.. module:: pynlpir.pos_map

``pynlpir.pos_map``
-------------------

Part of speech mapping constants and functions for NLPIR/ICTCLAS.

.. autodata:: POS_MAP
    :annotation:

.. autofunction:: get_pos_name
