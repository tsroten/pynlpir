PyNLPIR API
===========

.. module:: pynlpir

``pynlpir``
-----------

Provides an easy-to-use Python interface to NLPIR/ICTCLAS.

The functions below are not as extensive as the full set of functions exported
by NLPIR (for that, see :mod:`pynlpir.nlpir`). A few design choices have been
made with these functions as well, e.g. they have been renamed and their output
is formatted differently.

The functions in this module all assume input is either unicode or encoded
using the encoding specified when :func:`open` is called.
These functions return unicode strings.

After importing this module, you must call :func:`open` in order to initialize
the NLPIR API. When you're done using the NLPIR API, call :func:`close` to exit
the API.

.. data:: ENCODING

    The encoding configured by :func:`open`.

.. data:: ENCODING_ERRORS

    The encoding error handling scheme configured by :func:`open`.

.. function:: open(data_dir=nlpir.PACKAGE_DIR, encoding=ENCODING, encoding_errors=ENCODING_ERRORS, license_code=None)

    Initializes the NLPIR API.

    This calls the function :func:`~pynlpir.nlpir.Init`.

    :param str data_dir: The absolute path to the directory that has NLPIR's
        `Data` directory (defaults to :data:`pynlpir.nlpir.PACKAGE_DIR`).
    :param str encoding: The encoding that the Chinese source text will be in
        (defaults to ``'utf_8'``). Possible values include ``'gbk'``,
        ``'utf_8'``, or ``'big5'``.
    :param str encoding_errors: The desired encoding error handling scheme.
        Possible values include ``'strict'``, ``'ignore'``, and ``'replace'``.
        The default error handler is 'strict' meaning that encoding errors
        raise :class:`ValueError` (or a more codec specific subclass, such
        as :class:`UnicodeEncodeError`).
    :param str license_code: The license code that should be used when
        initializing NLPIR. This is generally only used by commercial users.
    :raises RuntimeError: The NLPIR API failed to initialize. Sometimes, NLPIR
        leaves an error log in the current working directory or NLPIR's
        ``Data`` directory that provides more detailed messages (but this isn't
        always the case).

.. function:: close

    Exits the NLPIR API and frees allocated memory. This calls the function
    :func:`~pynlpir.nlpir.Exit`.

.. function:: segment(s, pos_tagging=True, pos_names='parent', pos_english=True)

    Segment Chinese text *s* using NLPIR.

    The segmented tokens are returned as a list. Each item of the list is a
    string if *pos_tagging* is `False`, e.g. ``['我们', '是', ...]``. If
    *pos_tagging* is `True`, then each item is a tuple (``(token, pos)``), e.g.
    ``[('我们', 'pronoun'), ('是', 'verb'), ...]``.

    If *pos_tagging* is `True` and a segmented word is not recognized by
    NLPIR's part of speech tagger, then the part of speech code/name will
    be returned as :data:`None` (e.g. a space returns as ``(' ', None)``).

    This uses the function :func:`~pynlpir.nlpir.ParagraphProcess` to segment
    *s*.

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
    :param bool pos_english: Whether to use English or Chinese for the part
        of speech names, e.g. ``'conjunction'`` or ``'连词'``. Defaults to
        ``True``. This is only used if *pos_names* is ``True``.

.. function:: get_key_words(s, max_words=50, weighted=False)

    Determines key words in Chinese text *s*.

    The key words are returned in a list. If *weighted* is ``True``,
    then each list item is a tuple: ``(word, weight)``, where
    *weight* is a float. If it's *False*, then each list item is a string.

    This uses the function :func:`~pynlpir.nlpir.GetKeyWords` to determine
    the key words in *s*.

    :param s: The Chinese text to analyze. *s* should be Unicode or a UTF-8
        encoded string.
    :param int max_words: The maximum number of key words to find (defaults to
        ``50``).
    :param bool weighted: Whether or not to return the key words' weights
        (defaults to ``True``).


.. module:: pynlpir.nlpir

``pynlpir.nlpir``
~~~~~~~~~~~~~~~~~

This module uses :mod:`ctypes` to provide a Python API to NLPIR. Other than
argument names used in this documentation, the functions are left the same as
they are in NLPIR.

When this module is imported, the NLPIR library is imported and the functions
listed below are exported by a :class:`ctypes.CDLL` instance.

There is a less extensive, easier-to-use NLPIR interface directly in the
:mod:`pynlpir` module.

:func:`Init` must be called before any other NLPIR functions can be called.
After using the API, you can call :func:`Exit` to exit the API and free up
allocated memory.

.. data:: PACKAGE_DIR

    The absolute path to this package (used by NLPIR to find its ``Data``
    directory). This is a string in Python 2 and a bytes object in Python 3
    (so it can be used with the :func:`Init` function below).

.. data:: LIB_DIR

    The absolute path to this path's lib directory.

.. data:: libNLPIR

    A :class:`ctypes.CDLL` instance for the NLPIR API library.

.. data:: GBK_CODE
    :annotation: 0

    NLPIR's GBK encoding constant.

.. data:: UTF8_CODE
    :annotation: 1

    NLPIR's UTF-8 encoding constant.

.. data:: BIG5_CODE
    :annotation: 2

    NLPIR's BIG5 encoding constant.

.. data:: GBK_FANTI_CODE
    :annotation: 3

    NLPIR's GBK (Traditional Chinese) encoding constant.

.. data:: ICT_POS_MAP_SECOND
    :annotation: 0

    ICTCLAS part of speech constant #2.

.. data:: ICT_POS_MAP_FIRST
    :annotation: 1

    ICTCLAS part of speech constant #1.

.. data:: PKU_POS_MAP_SECOND
    :annotation: 2

    PKU part of speech constant #2.

.. data:: PKU_POS_MAP_FIRST
    :annotation: 3

    PKU part of speech constant #1.

.. class:: ResultT

    The NLPIR ``result_t`` structure. Inherits from :class:`ctypes.Structure`.

    .. data:: start

        The start position of the word in the source Chinese text string.

    .. data:: length

        The detected word's length.

    .. data:: sPOS

        A string representing the word's part of speech.

    .. data:: word_type

        If the word is found in the user's dictionary.

    .. data:: weight

        The weight of the detected word.

.. function:: get_func(name, argtypes=None, restype=c_int, lib=libNLPIR)

    Retrieves the corresponding NLPIR function.

    :param str name: The name of the NLPIR function to get.
    :param list argtypes: A list of :mod:`ctypes` data types that correspond
        to the function's argument types.
    :param restype: A :mod:`ctypes` data type that corresponds to the
        function's return type (only needed if the return type isn't
        :class:`ctypes.c_int`).
    :param lib: A :class:`ctypes.CDLL` instance for the NLPIR API library where
        the function will be retrieved from (defaults to :data:`libNLPIR`).
    :returns: The exported function. It can be called like any other Python
        callable.

.. function:: Init(data_dir, encoding=GBK_CODE, license_code=None)

    Initializes the NLPIR API. This must be called before any other NLPIR
    functions will work.

    :param str data_dir: The path to the NLPIR data folder's parent folder.
        :data:`PACKAGE_DIR` can be used for this.
    :param int encoding: Which encoding NLPIR should expect.
        :data:`GBK_CODE`, :data:`UTF8_CODE`, :data:`BIG5_CODE`, and
        :data:`GBK_FANTI_CODE` should be used for this argument.
    :param str license_code: A license code for unlimited usage. Most users
        shouldn't need to use this.
    :returns: Whether or not the function executed successfully.
    :rtype: bool

.. function:: Exit()

    Exits the NLPIR API and frees allocated memory.

    :returns: Whether or not the function executed successfully.
    :rtype: bool

.. function:: ParagraphProcess(s, pos_tagging=True)

    Segments a string of Chinese text (encoded using the encoding specified
    when :func:`Init` was called).

    :param str s: The Chinese text to process.
    :param bool pos_tagging: Whether or not to return part of speech tags with
        the segmented words..
    :returns: The segmented words.
    :rtype: str

.. function:: ParagraphProcessA(s, size_pointer, user_dict=True)

    Segments a string of Chinese text (encoded using the encoding specified
    when :func:`Init` was called).

    Here is an example of how to use this function:

    .. code:: python
    
        size = ctypes.c_int()
        result = ParagraphProcessA(s, ctypes.byref(size), False)
        result_t_vector = ctypes.cast(result, ctypes.POINTER(ResultT))
        words = []
        for i in range(0, size.value):
            r = result_t_vector[i]
            word = s[r.start:r.start+r.length]
            words.append((word, r.sPOS))

    :param str s: The Chinese text to process.
    :param size_pointer: A pointer to a :class:`ctypes.c_int` that will be set to
        the result vector's size.
    :type pointer: :func:`ctypes.POINTER`
    :param bool user_dict: Whether or not to use the user dictionary.
    :returns: A pointer to the result vector. Each result in the result vector
        is an instance of :class:`ResultT`.

.. function:: FileProcess(source_filename, result_filename, pos_tagging=True)

    Processes a text file.

    :param str source_filename: The name of the file that contains the source
        text.
    :param str result_filename: The name of the file where the results should
        be written.
    :param bool pos_tagging: Whether or not to include part of speech tags in
        the output.
    :returns: If the function executed successfully, the processing speed is
        returned (:class:`float`). Otherwise, ``0`` is returned.

.. function:: ImportUserDict(filename)

    Imports a user-defined dictionary from a text file.

    :param str filename: The filename of the user's dictionary file.
    :returns: The number of lexical entries successfully imported.
    :rtype: int

.. function:: AddUserWord(word)

    Adds a word to the user's dictionary.

    :param str word: The word to add to the dictionary.
    :returns: ``1`` if the word was added successfully, otherwise ``0``.
    :rtype: int

.. function:: SaveTheUsrDic()

    Writes the user's dictionary to disk.

    :returns: ``1`` if the dictionary was saved successfully, otherwise ``0``.
    :rtype: int

.. function:: DelUsrWord(word)

    Deletes a word from the user's dictionary.

    :param str word: The word to delete.
    :returns: ``-1`` if the word doesn't exist in the dictionary. Otherwise,
        the pointer to the word deleted.
    :rtype: int

.. function:: GetKeyWords(s, max_words=50, weighted=False)

    Extracts key words from a string of Chinese text.

    :param str s: The Chinese text to process.
    :param int max_words: The maximum number of key words to return.
    :param bool weighted: Whether or not the key words' weights are returned.
    :returns: The key words.
    :rtype: str

.. function:: GetFileKeyWords(filename, max_words=50, weighted=False)

    Extracts key words from Chinese text in a file.

    :param str filename: The file to process.
    :param int max_words: The maximum number of key words to return.
    :param bool weighted: Whether or not the key words' weights are returned.
    :returns: The key words.
    :rtype: str

.. function:: GetNewWords(s, max_words=50, weighted=False)

    Extracts new words from a string of Chinese text.

    :param str s: The Chinese text to process.
    :param int max_words: The maximum number of new words to return.
    :param bool weighted: Whether or not the new words' weights are returned.
    :returns: The new words.
    :rtype: str

.. function:: GetFileNewWords(filename, max_words=50, weighted=False)

    Extracts new words from Chinese text in a file.

    :param str filename: The file to process.
    :param int max_words: The maximum number of new words to return.
    :param bool weighted: Whether or not the new words' weights are returned.
    :returns: The new words.
    :rtype: str

.. function:: FingerPrint(s)

    Extracts a fingerprint from a string of Chinese text.

    :param str s: The Chinese text to process.
    :returns: The fingerprint of the content. ``0`` if the function failed.

.. function:: SetPOSmap(pos_map)

    Selects which part of speech map to use.

    :param int pos_map: The part of speech map that should be used. This should
        be one of :data:`ICT_POS_MAP_FIRST`, :data:`ICT_POS_MAP_SECOND`,
        :data:`PKU_POS_MAP_FIRST`, or :data:`PKU_POS_MAP_SECOND`.
    :returns: ``0`` if the function failed, otherwise ``1``.
    :rtype: int

.. function:: NWI_Start()

    Initializes new word identification.

    :returns: ``True`` if the function succeeded; ``False`` if it failed.
    :rtype: bool

.. function:: NWI_AddFile(filename)

    Adds the words in a text file.

    :param string filename: The text file's filename.
    :returns: ``True`` if the function succeeded; ``False`` if it failed.
    :rtype: bool

.. function:: NWI_AddMem(filename)

    Increases the allotted memory for new word identification.

    :param string filename: NLPIR's documentation is unclear on what this
        argument is for.
    :returns: ``True`` if the function succeeded; ``False`` if it failed.
    :rtype: bool

.. function:: NWI_Complete()

    Terminates new word identifcation. Frees up memory and resources.

    :returns: ``True`` if the function succeeded; ``False`` if it failed.
    :rtype: bool

.. function:: NWI_GetResult(weight)

    Returns the new word identification results.

    :param bool weight: Whether or not to include word weights in the results.
    :returns: ``True`` if the function succeeded; ``False`` if it failed.
    :returns: The identified words.
    :rtype: str

.. function:: NWI_Results2UserDict()

    Adds the newly identified words to the user dictionary.

    This function should only be called after
    :func:`~pynlpir.nlpir.NWI_Complete` is called.

    If you want to save the user dictionary, consider running
    :func:`~pynlpir.nlpir.SaveTheUsrDic`.

    :returns: ``1`` if the function succeeded; ``0`` if it failed.
    :rtype: int


.. module:: pynlpir.pos_map

``pynlpir.pos_map``
~~~~~~~~~~~~~~~~~~~

Part of speech mapping constants and functions for NLPIR/ICTCLAS.

This module is used by :mod:`pynlpir` to format segmented words for output.

.. data:: POS_MAP

    A dictionary that maps part of speech codes returned by NLPIR to
    human-readable names (English and Chinese).

.. function:: get_pos_name(code, name='parent', english=True)

    Gets the part of speech name for *code*.

    :param str code: The part of speech code to lookup, e.g. ``'nsf'``.
    :param str name: Which part of speech name to include in the output. Must
        be one of ``'parent'``, ``'child'``, or ``'all'``. Defaults to
        ``'parent'``. ``'parent'`` indicates that only the most generic name
        should be used, e.g. ``'noun'`` for ``'nsf'``. ``'child'`` indicates
        that the most specific name should be used, e.g.
        ``'transcribed toponym'`` for ``'nsf'``. ``'all'`` indicates that all
        names should be used, e.g. ``('noun', 'toponym',
        'transcribed toponym')`` for ``'nsf'``.
    :param bool english: Whether to return an English or Chinese name.
    :returns: ``str`` (``unicode`` for Python 2) if *name* is ``'parent'`` or
        ``'child'``. ``tuple`` if *name* is ``'all'``. :data:`None` if the part
        of speech code is not recognized.
