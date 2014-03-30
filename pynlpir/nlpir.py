# -*- coding: utf-8 -*-
"""Provides a Python interface to NLPIR."""
from __future__ import unicode_literals
from ctypes import c_bool, c_char_p, c_int, cdll
import logging
import os
import sys

logger = logging.getLogger('pynlpir.nlpir')

is_python3 = sys.version_info[0] > 2
if is_python3:
    unicode = str

#: The absolute path to this package (used by NLPIR to find its ``Data``
#: directory).
PACKAGE_DIR = os.path.abspath(os.path.dirname(__file__))

#: The absolute path to this path's lib directory.
LIB_DIR = os.path.join(PACKAGE_DIR, 'lib')

#: NLPIR UTF-8 encoding constant.
UTF8 = 1


def load_library(platform, is_64bit, lib_dir=LIB_DIR):
    """Loads the NLPIR library appropriate for the user's system.

    :param str platform: The platform identifier for the user's system.
    :param bool is_64bit: Whether or not the user's system is 64-bit.
    :param str lib_dir: The directory that contains the library files
        (defaults to :data:`LIB_DIR`).

    """
    logger.info("Loading the NLPIR library file.")
    logger.debug("Loading library file from '%s'" % lib_dir)
    if platform.startswith('win') and is_64bit:
        lib = os.path.join(lib_dir, 'NLPIR64')
        logger.debug("Using library file for 64-bit Windows.")
    elif platform.startswith('win'):
        lib = os.path.join(lib_dir, 'NLPIR32')
        logger.debug("Using library file for 32-bit Windows.")
    elif platform.startswith('linux') and is_64bit:
        lib = os.path.join(lib_dir, 'libNLPIR64.so')
        logger.debug("Using library file for 64-bit GNU/Linux.")
    elif platform.startswith('linux'):
        lib = os.path.join(lib_dir, 'libNLPIR32.so')
        logger.debug("Using library file for 32-bit GNU/Linux.")
    else:
        raise RuntimeError("Platform '%s' is not supported by NLPIR." %
                           platform)
    libNLPIR = cdll.LoadLibrary(lib)
    logger.debug("Library file '%s' loaded." % lib)
    logger.info("NLPIR library file loaded.")
    return libNLPIR


is_64bit = sys.maxsize > 2**32
#: A CDLL instance for the NLPIR API library.
libNLPIR = load_library(sys.platform, is_64bit)


def get_func(name, argtypes=None, restype=None, lib=libNLPIR):
    """Retrieves the corresponding NLPIR function.

    :param str name: The name of the NLPIR function to get.
    :param list argtypes: A list of :mod:`ctypes` data types that correspond
        to the function's argument types.
    :param restype: A :mod:`ctypes` data type that corresponds to the
        function's return type (only needed if the return type isn't
        :class:`ctypes.c_int`).
    :param lib: A :class:`ctypes.CDLL` instance for the NLPIR API library where
        the function will be retrieved from (defaults to :data:`libNLPIR`).

    """
    logger.debug("Getting NLPIR API function: {'name': '%s', 'argtypes': '%s',"
                 " 'restype': '%s'}." % (name, argtypes, restype))
    func = getattr(lib, name)
    if argtypes is not None:
        func.argtypes = argtypes
    if restype is not None:
        func.restype = restype
    logger.debug("NLPIR API function '%s' retrieved." % name)
    return func


def init(data_dir=PACKAGE_DIR):
    """Initializes the NLPIR API.

    :param str data_dir: The absolute path to the directory that has NLPIR's
        `Data` directory (defaults to :data:`PACKAGE_DIR`).

    """
    logger.info("Initializing the NLPIR API.")
    logger.debug("Initializing the NLPIR API: {'data_dir': '%s'}" % data_dir)
    init = get_func('NLPIR_Init')
    if not init(data_dir, UTF8):
        raise RuntimeError("NLPIR function 'NLPIR_Init' failed.")
    else:
        logger.info("NLPIR API initialized.")


def close():
    """Exits the NLPIR API and frees allocated memory."""
    logger.debug("Exiting the NLPIR API.")
    exit = get_func('NLPIR_Exit', restype=c_bool)
    if not exit():
        logger.warning("NLPIR function 'NLPIR_Exit' failed.")
    else:
        logger.debug("NLPIR API exited.")


def _decode(s):
    """Decodes *s* using UTF-8."""
    return s if isinstance(s, unicode) else s.decode('utf-8')


def _encode(s):
    """Encodes *s* using UTF-8."""
    return s.encode('utf-8') if isinstance(s, unicode) else s


def _to_float(s):
    """Converts *s* to a float if possible; if not, returns `False`."""
    try:
        f = float(s)
        return f
    except ValueError:
        return False


def segment(s, pos_tagging=True):
    """Segment Chinese text *s* using NLPIR.

    The segmented tokens are returned as a list. Each item of the list is a
    string if *pos_tagging* is `False`, e.g. ``['我们', '是', ...]``. If
    *pos_tagging* is `True`, then each item is a tuple (``(token, pos)``), e.g.
    ``[('我们', 'rr'), ('是', 'vshi'), ...]``.

    :param s: The Chinese text to segment. *s* should be Unicode or a UTF-8
        encoded string.
    :param bool pos_tagging: Whether or not to include part of speech tagging
        (defaults to ``True``).

    """
    s = _decode(s)
    logger.debug("Segmenting text with%s POS tagging: %s." %
                 ('' if pos_tagging else 'out', s))
    _process_paragraph = get_func('NLPIR_ParagraphProcess', [c_char_p, c_int],
                                  c_char_p)
    result = _process_paragraph(_encode(s), pos_tagging)
    result = result.decode('utf-8')
    logger.debug("Finished segmenting text: %s." % result)
    logger.debug("Formatting segmented text.")
    tokens = result.strip().split(' ')
    if pos_tagging:
        tokens = [tuple(t.split('/')) for t in tokens]
    logger.debug("Formatted segmented text: %s." % tokens)
    return tokens


def get_key_words(s, max_words=50, weighted=False):
    """Determines key words in Chinese text *s*.

    The key words are returned in a list. If *weighted* is ``True``,
    then each list item is a tuple: ``(word, weight)``, where
    *weight* is a float. If it's *False*, then each list item is a string.

    :param s: The Chinese text analyze. *s* should be Unicode or a UTF-8
        encoded string.
    :param int max_words: The maximum number of key words (up to ``50``) to
        find (defaults to ``50``).
    :param bool weighted: Whether or not to return the key words' weights.

    """
    s = _decode(s)
    logger.debug("Searching for up to %s%s key words in: %s." %
                 (max_words, ' weighted' if weighted else '', s))
    _get_key_words = get_func('NLPIR_GetKeyWords', [c_char_p, c_int, c_bool],
                              c_char_p)
    result = _get_key_words(_encode(s), max_words, weighted)
    result = result.decode('utf-8')
    logger.debug("Finished key word search: %s." % result)
    logger.debug("Formatting key word search results.")
    fresult = result.strip('#').split('#')
    if weighted:
        weights, words = [], []
        for w in fresult:
            word, pos, weight = w.split('/')
            weight = _to_float(weight)
            weights.append(weight or 0.0)
            words.append(word)
        fresult = zip(words, weights)
    logger.debug("Key words formatted: %s." % fresult)
    return fresult


# Initialize the NLPIR API.
init()
