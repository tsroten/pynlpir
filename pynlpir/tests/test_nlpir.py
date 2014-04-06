# -*- coding: utf-8 -*-
"""Unit tests for pynlpir.nlpir."""
from __future__ import unicode_literals
import ctypes
import unittest

from pynlpir import nlpir


class TestNLPIR(unittest.TestCase):
    """Unit tests for the pynlpir.nlpir module."""

    def test_load_library(self):
        """Tests that the load_library() function works as expected."""
        self.assertTrue(isinstance(nlpir.libNLPIR, ctypes.CDLL))
