"""Provides a Python interface to NLPIR."""
from __future__ import unicode_literals
from ctypes import c_bool, c_char_p, c_int, cdll
import logging
import os
import sys

logger = logging.getLogger('pynlpir')

is_python3 = sys.version_info[0] > 2

is_linux = sys.platform.startswith('linux')
is_windows = sys.platform.startswith('win')
is_64bit = sys.maxsize > 2**32
logger.debug("Loading NLPIR module on a %s %s system." % ('64-bit' if is_64bit
             else '32-bit', sys.platform))
if not is_linux and not is_windows:
    logger.error("Platform '%s' is not supported by NLPIR." % sys.platform)

#: The absolute path to this package (used by NLPIR to find the ``Data``
#: directory).
PACKAGE_DIR = os.path.abspath(os.path.dirname(__file__))

#: The absolute path to this path's lib directory.
LIB_DIR = os.path.join(PACKAGE_DIR, 'lib')

# NLPIR encoding constants:
UTF8 = 1

# Part of speech mapping constants:
ICT_2 = 0
ICT_1 = 1
PKU_2 = 2
PKU_1 = 3
POS = {'ict2': ICT_2, 'ict1': ICT_1, 'pku2': PKU_2, 'pku1': PKU_1}


class NLPIR(object):
    """A Python interface to NLPIR.

    :param str lib_dir: The directory containing the NLPIR library files.
        Defaults to the library directory that is included with this Python
        package.
    :param str data_dir: The directory containing NLPIR's ``Data`` directory.
        Defaults to this package's root directory.
    :param str pos: The part of speech map to use. This should be one of:
        ``'ict1'``, ``'ict2'``, ``'pku1'``, or ``'pku2'``.

    """

    def __init__(self, lib_dir=LIB_DIR, data_dir=PACKAGE_DIR, pos='ict2'):
        """Loads the NLPIR library; initializes the API; sets the POS map."""
        self.logger = logging.getLogger('pynlpir.%s' % self.__class__.__name__)
        self.logger.debug("Initializing a NLPIR object: {'lib_dir': '%s', "
                          "'data_dir': '%s', 'pos': '%s'}." %
                          (lib_dir, data_dir, pos))
        self.pos = pos  # TODO: make this set to default NLPIR POS map.
        self._load_library(lib_dir)
        self._init(data_dir)
        self.set_pos_map(pos)

    def _load_library(self, lib_dir=LIB_DIR):
        """Loads the NLPIR library appropriate for the user's system.

        :param str lib_dir: The directory that contains the library files.

        """
        self.logger.info("Loading the NLPIR library file.")
        self.logger.debug("Loading library file from '%s'" % lib_dir)
        if is_windows and is_64bit:
            lib = os.path.join(lib_dir, 'NLPIR64')
            self.logger.debug("Using library file for 64-bit Windows.")
        elif is_windows:
            lib = os.path.join(lib_dir, 'NLPIR32')
            self.logger.debug("Using library file for 32-bit Windows.")
        elif is_linux and is_64bit:
            lib = os.path.join(lib_dir, 'libNLPIR64.so')
            self.logger.debug("Using library file for 64-bit GNU/Linux.")
        elif is_linux:
            lib = os.path.join(lib_dir, 'libNLPIR32.so')
            self.logger.debug("Using library file for 32-bit GNU/Linux.")
        else:
            raise RuntimeError("Platform '%s' is not supported by NLPIR." %
                               sys.platform)
        self.libNLPIR = cdll.LoadLibrary(lib)
        self.logger.debug("Library file '%s' loaded." % lib)
        self.logger.info("NLPIR library file loaded.")

    def _init(self, data_dir=PACKAGE_DIR):
        """Initializes the NLPIR API."""
        self.logger.info("Initializing the NLPIR API.")
        self.logger.debug("Initializing the NLPIR API: {'data_dir': '%s'}"
                          % data_dir)
        init = self.get_func('NLPIR_Init')
        if not init(data_dir, UTF8):
            raise RuntimeError("NLPIR function 'NLPIR_Init' failed. "
                               "Check NLPIR error log for more information.")
        else:
            self.logger.info("NLPIR API initialized.")

    def _exit(self):
        """Exits the NLPIR API and frees allocated memory."""
        self.logger.debug("Exiting the NLPIR API.")
        _exit = self.get_func('NLPIR_Exit', restype=c_bool)
        if not _exit():
            self.logger.warning("NLPIR function 'NLPIR_Exit' failed.")
        else:
            self.logger.debug("NLPIR API exited.")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Exits the NLPIR API when a context manager is used."""
        self.close()

    def close(self):
        """Exits the NLPIR API."""
        self._exit()

    def _is_unicode(self, s):
        """Checks if *s* is unicode (str in Python 3)."""
        if is_python3:
            return isinstance(s, str)
        return isinstance(s, unicode)

    def _decode(self, s):
        """Decodes *s* using UTF-8."""
        return s if self._is_unicode(s) else s.decode('utf-8')

    def _encode(self, s):
        """Encodes *s* using UTF-8."""
        return s.encode('utf-8') if self._is_unicode(s) else s

    def get_func(self, name, argtypes=None, restype=None):
        """Retrieves the corresponding NLPIR function.

        *name* is a string containing the name of the NLPIR function to get.
        *argtypes* is a list of :mod:`ctypes` data types that correspond to the
        function's argument types.
        *restype* is a :mod:`ctypes` data type that corresponds to the
        function's return type (only needed if the return type isn't
        :class:`ctypes.c_int`).

        """
        self.logger.debug("Getting NLPIR API function: {'name': '%s', "
                          "'argtypes': '%s', 'restype': '%s'}." %
                          (name, argtypes, restype))
        func = getattr(self.libNLPIR, name)
        if argtypes is not None:
            func.argtypes = argtypes
        if restype is not None:
            func.restype = restype
        self.logger.debug("NLPIR API function '%s' retrieved." % name)
        return func

    def set_pos_map(self, pos):
        """Changes the current part of speech map.

        :param str pos_map: Which part of speech map to use. Must be one of:
            ``'ict1'``, ``'ict2'``, ``'pku1'``, or ``'pku2'``.

        """
        self.logger.info("Setting POS map to '%s'." % pos)
        pos_map = pos.lower().replace('_', '').replace('-', '')
        try:
            pos_cons = POS[pos_map]
        except KeyError:
            raise ValueError("POS map '%s' not supported by NLPIR." % pos)
        _set_pos_map = self.get_func('NLPIR_SetPOSmap', argtypes=[c_int])
        if not _set_pos_map(pos_cons):
            self.logger.error("Unable to set POS map to '%s'." % pos)
        else:
            self.logger.info("POS map set to '%s'." % pos)
            self.pos = pos

    def segment(self, s, pos_tagging=True):
        """Segment Chinese text *s* using NLPIR.

        The segmented tokens are returned in a list. If *pos_tagging* is
        ``True``, then each token is returned as a tuple: ``(token, pos)``.
        If it's ``False``, then each token is returned as a string.

        """
        s = self._decode(s)
        self.logger.debug("Segmenting text with%s POS tagging: %s." %
                          ('' if pos_tagging else 'out', s))
        _process_paragraph = self.get_func('NLPIR_ParagraphProcess',
                                           [c_char_p, c_int], c_char_p)
        result = _process_paragraph(self._encode(s), pos_tagging)
        result = result.decode('utf-8')
        self.logger.debug("Finished segmenting text: %s." % result)
        self.logger.debug("Formatting segmented text.")
        tokens = result.split(' ')
        if pos_tagging:
            tokens = [tuple(t.split('/')) for t in tokens]
        self.logger.debug("Formatted segmented text: %s." % tokens)
        return tokens

    def get_key_words(self, p, max_words=50, weighted=False):
        """Determines key words in paragraph *p*.

        The key words are returned in a list. If *weighted* is ``True``,
        then each token is returned as a tuple: ``(token, weight)``, where
        *weight* is a float. If it's *False*, then each token is returned as a
        string.

        """
        def to_float(s):
            try:
                n = float(s)
                return n
            except ValueError:
                return False

        p = self._decode(p)
        self.logger.debug("Searching for up to %s%s key words in: %s." %
                          (max_words, ' weighted' if weighted else '', p))
        _get_key_words = self.get_func('NLPIR_GetKeyWords',
                                       [c_char_p, c_int, c_bool], c_char_p)
        result = _get_key_words(self._encode(p), max_words, weighted)
        result = result.decode('utf-8')
        self.logger.debug("Finished key word search: %s." % result)
        self.logger.debug("Formatting key word search results.")
        if not weighted:
            fresult = result.split(' ')
        else:
            weights, words = [], []
            for w in result.split(' '):
                n = to_float(w)
                if n is not False:
                    weights.append(n)
                else:
                    words.append(w)
            fresult = zip(words, weights)
        self.logger.debug("Key words formatted: %s." % fresult)
        return fresult
