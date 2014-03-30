"""Unit tests for pynlpir.nlpir."""
from __future__ import unicode_literals
import ctypes
import logging
import unittest

from pynlpir import nlpir

is_supported = nlpir.is_linux or nlpir.is_windows


class TestNLPIR(unittest.TestCase):
    """Unit tests for the NLPIR class."""

    def setUp(self):
        """Creates a new instance of NLPIR."""
        if is_supported:
            self.nlpir = nlpir.NLPIR()

    def tearDown(self):
        """Exits the NLPIR API."""
        if is_supported:
            self.nlpir.close()
            del self.nlpir

    def test_init(self):
        """Tests that the __init__() method works as expected."""
        if not is_supported:
            self.assertRaises(RuntimeError, nlpir.NLPIR)
            return
        self.assertTrue(isinstance(self.nlpir.libNLPIR, ctypes.CDLL))

    def test_segment(self):
        """Tests that the segment() method works as expected."""
        if not is_supported:
            return
        s = '我们都是美国人。'
        seg_s = self.nlpir.segment(s, False)
        pos_seg_s = self.nlpir.segment(s, True)
        expected_seg_s = ['我们', '都', '是', '美国', '人', '。']
        expected_pos_seg_s = [('我们', 'rr'), ('都', 'd'), ('是', 'vshi'),
                              ('美国', 'nsf'), ('人', 'n'), ('。', 'wj')]
        self.assertEqual(expected_seg_s, seg_s)
        self.assertEqual(expected_pos_seg_s, pos_seg_s)
