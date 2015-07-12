# -*- coding: utf-8 -*-
"""Unit tests for pynlpir.nlpir."""
from __future__ import unicode_literals
import ctypes
import unittest

import pynlpir
nlpir = pynlpir.nlpir


class TestNLPIR(unittest.TestCase):
    """Unit tests for the pynlpir.nlpir module."""

    def test_load_library(self):
        """Tests that the load_library() function works as expected."""
        self.assertTrue(isinstance(nlpir.libNLPIR, ctypes.CDLL))
