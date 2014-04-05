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

.. function:: load_library(platform, is_64bit, lib_dir=LIB_DIR)

    Loads the NLPIR library appropriate for the user's system.

    :param str platform: The platform identifier for the user's system.
    :param bool is_64bit: Whether or not the user's system is 64-bit.
    :param str lib_dir: The directory that contains the library files
        (defaults to :data:`LIB_DIR`).

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

.. function:: init(data_dir=PACKAGE_DIR)

    Initializes the NLPIR API.

    :param str data_dir: The absolute path to the directory that has NLPIR's
        `Data` directory (defaults to :data:`PACKAGE_DIR`).

.. function:: close

    Exits the NLPIR API and frees allocated memory.

.. function:: segment(s, pos_tagging=True, pos_names=True, parents=False, english=True)

    Segment Chinese text *s* using NLPIR.

    The segmented tokens are returned as a list. Each item of the list is a
    string if *pos_tagging* is `False`, e.g. ``['我们', '是', ...]``. If
    *pos_tagging* is `True`, then each item is a tuple (``(token, pos)``), e.g.
    ``[('我们', 'personal pronoun'), ('是', 'verb 是'), ...]``.

    :param s: The Chinese text to segment. *s* should be Unicode or a UTF-8
        encoded string.
    :param bool pos_tagging: Whether or not to include part of speech tagging
        (defaults to ``True``).
    :param bool pos_names: Whether or not to convert the part of speech codes
        to part of speech names, e.g. ``'wd'`` to ``'comma'``. Defaults to
        ``True``.
    :param bool parents: Whether or not to include the part of speech name's
        parents, e.g. ``'noun:personal name:Chinese surname'``. Defaults to
        ``False``. This is only used if *pos_names* is ``True``.
    :param bool english: Whether or not to use English or Chinese for the part
        of speech names, e.g. ``'conjunction'`` or ``'连词'``. Defaults to
        ``True``. This is only used if *pos_names* is ``True``.

.. function:: get_key_words(s, max_words=50, weighted=False)

    Determines key words in Chinese text *s*.

    The key words are returned in a list. If *weighted* is ``True``,
    then each list item is a tuple: ``(word, weight)``, where
    *weight* is a float. If it's *False*, then each list item is a string.

    :param s: The Chinese text analyze. *s* should be Unicode or a UTF-8
        encoded string.
    :param int max_words: The maximum number of key words (up to ``50``) to
        find (defaults to ``50``).
    :param bool weighted: Whether or not to return the key words' weights.
