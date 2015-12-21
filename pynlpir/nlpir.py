# -*- coding: utf-8 -*-
"""This module uses :mod:`ctypes` to provide a Python API to NLPIR.

Other than argument names used in this documentation, the functions are left
the same as they are in NLPIR.

When this module is imported, the NLPIR library is imported and the functions
listed below are exported by a :class:`ctypes.CDLL` instance.

There is a less extensive, easier-to-use NLPIR interface directly in the
:mod:`pynlpir` module.

:func:`Init` must be called before any other NLPIR functions can be called.
After using the API, you can call :func:`Exit` to exit the API and free up
allocated memory.

"""
from __future__ import unicode_literals
from ctypes import (c_bool, c_char, c_char_p, c_double, c_int, c_uint,
                    c_ulong, c_void_p, cdll, POINTER, Structure)
import logging
import os
import sys

logger = logging.getLogger('pynlpir.nlpir')

#: The absolute path to this package (used by NLPIR to find its ``Data``
#: directory). This is a string in Python 2 and a bytes object in Python 3
#: (so it can be used with the :func:`Init` function below).
PACKAGE_DIR = os.path.abspath(os.path.dirname(__file__))

#: The absolute path to this path's lib directory.
LIB_DIR = os.path.join(PACKAGE_DIR, 'lib')

is_python3 = sys.version_info[0] > 2
if is_python3:
    # Python 3 expects bytes for data type ctypes.c_char_p.
    PACKAGE_DIR = PACKAGE_DIR.encode('utf_8')

#: NLPIR's GBK encoding constant.
GBK_CODE = 0
#: NLPIR's UTF-8 encoding constant.
UTF8_CODE = 1
#: NLPIR's BIG5 encoding constant.
BIG5_CODE = 2
#: NLPIR's GBK (Traditional Chinese) encoding constant.
GBK_FANTI_CODE = 3

#: ICTCLAS part of speech constant #2.
ICT_POS_MAP_SECOND = 0
#: ICTCLAS part of speech constant #1.
ICT_POS_MAP_FIRST = 1
#: PKU part of speech constant #2.
PKU_POS_MAP_SECOND = 2
#: PKU part of speech constant #1.
PKU_POS_MAP_FIRST = 3


class ResultT(Structure):
    """The NLPIR ``result_t`` structure."""

    _fields_ = [
        # The start position of the word in the source Chinese text string.
        ('start', c_int),

        # The detected word's length.
        ('length', c_int),

        # A string representing the word's part of speech.
        ('sPOS', c_char * 40),

        ('iPOS', c_int),

        ('word_ID', c_int),

        # If the word is found in the user's dictionary.
        ('word_type', c_int),

        # The weight of the detected word.
        ('weight', c_int)
    ]


def load_library(platform, is_64bit, lib_dir=LIB_DIR):
    """Loads the NLPIR library appropriate for the user's system.

    This function is called automatically when this module is loaded.

    :param str platform: The platform identifier for the user's system.
    :param bool is_64bit: Whether or not the user's system is 64-bit.
    :param str lib_dir: The directory that contains the library files
        (defaults to :data:`LIB_DIR`).
    :raises RuntimeError: The user's platform is not supported by NLPIR.

    """
    logger.debug("Loading NLPIR library file from '%s'" % lib_dir)
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
    elif platform == 'darwin':
        lib = os.path.join(lib_dir, 'libNLPIRios.so')
        logger.debug("Using library file for OSX/iOS.")
    else:
        raise RuntimeError("Platform '%s' is not supported by NLPIR." %
                           platform)
    libNLPIR = cdll.LoadLibrary(lib)
    logger.debug("NLPIR library file '%s' loaded." % lib)
    return libNLPIR


is_64bit = sys.maxsize > 2**32

#: A :class:`ctypes.CDLL` instance for the NLPIR API library.
libNLPIR = load_library(sys.platform, is_64bit)


def get_func(name, argtypes=None, restype=c_int, lib=libNLPIR):
    """Retrieves the corresponding NLPIR function.

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

    """
    logger.debug("Getting NLPIR API function: {'name': '%s', 'argtypes': '%s',"
                 " 'restype': '%s'}." % (name, argtypes, restype))
    func = getattr(lib, name)
    if argtypes is not None:
        func.argtypes = argtypes
    if restype is not c_int:
        func.restype = restype
    logger.debug("NLPIR API function '%s' retrieved." % name)
    return func


# Get the exported NLPIR API functions.
Init = get_func('NLPIR_Init', [c_char_p, c_int, c_char_p], c_bool)
Exit = get_func('NLPIR_Exit', restype=c_bool)
ParagraphProcess = get_func('NLPIR_ParagraphProcess', [c_char_p, c_int],
                            c_char_p)
ParagraphProcessA = get_func('NLPIR_ParagraphProcessA',
                             [c_char_p, c_void_p, c_bool],
                             POINTER(ResultT))
FileProcess = get_func('NLPIR_FileProcess', [c_char_p, c_char_p, c_int],
                       c_double)
ImportUserDict = get_func('NLPIR_ImportUserDict', [c_char_p], c_uint)
AddUserWord = get_func('NLPIR_AddUserWord', [c_char_p])
SaveTheUsrDic = get_func('NLPIR_SaveTheUsrDic')
DelUsrWord = get_func('NLPIR_DelUsrWord', [c_char_p])
GetKeyWords = get_func('NLPIR_GetKeyWords', [c_char_p, c_int, c_bool],
                       c_char_p)
GetFileKeyWords = get_func('NLPIR_GetFileKeyWords',
                           [c_char_p, c_int, c_bool], c_char_p)
GetNewWords = get_func('NLPIR_GetNewWords', [c_char_p, c_int, c_bool],
                       c_char_p)
GetFileNewWords = get_func('NLPIR_GetFileNewWords',
                           [c_char_p, c_int, c_bool], c_char_p)
FingerPrint = get_func('NLPIR_FingerPrint', [c_char_p], c_ulong)
SetPOSmap = get_func('NLPIR_SetPOSmap', [c_int])
NWI_Start = get_func('NLPIR_NWI_Start', None, c_bool)
NWI_AddFile = get_func('NLPIR_NWI_AddFile', [c_char_p], c_bool)
NWI_AddMem = get_func('NLPIR_NWI_AddMem', [c_char_p], c_bool)
NWI_Complete = get_func('NLPIR_NWI_Complete', None, c_bool)
NWI_GetResult = get_func('NLPIR_NWI_GetResult', [c_bool], c_char_p)
NWI_Result2UserDict = get_func('NLPIR_NWI_Result2UserDict', None, c_bool)
