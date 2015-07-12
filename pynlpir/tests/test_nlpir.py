# -*- coding: utf-8 -*-
"""Unit tests for pynlpir.nlpir."""
from __future__ import unicode_literals
import ctypes
import os
import unittest

import pynlpir
nlpir = pynlpir.nlpir
pynlpir.open()


class TestNLPIR(unittest.TestCase):
    """Unit tests for the pynlpir.nlpir module."""

    def test_load_library(self):
        """Tests that the load_library() function works as expected."""
        self.assertTrue(isinstance(nlpir.libNLPIR, ctypes.CDLL))

    def test_nwi(self):
        """Tests that the basic new word identification functions work."""
        data_dir = os.path.join(os.path.dirname(__file__), 'data')
        test_file = os.path.join(data_dir, 'nwi-test.txt')
        self.assertTrue(nlpir.NWI_Start())
        self.assertTrue(nlpir.NWI_AddFile(test_file))
        self.assertTrue(nlpir.NWI_Complete())
        self.assertEqual('撒门#西生#撒督#',
                         nlpir.NWI_GetResult(False).decode('utf-8'))
