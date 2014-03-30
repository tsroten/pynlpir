# -*- coding: utf-8 -*-
"""Unit tests for pynlpir.nlpir."""
from __future__ import unicode_literals
import ctypes
import unittest

from pynlpir import nlpir


class TestNLPIR(unittest.TestCase):
    """Unit tests for the pynlpir.nlpir module."""

    def test_load_library(self):
        """Tests that the load_library() method works as expected."""
        self.assertTrue(isinstance(nlpir.libNLPIR, ctypes.CDLL))

    def test_segment(self):
        """Tests that the segment() method works as expected."""
        s = '我们都是美国人。'
        seg_s = nlpir.segment(s, False)
        pos_seg_s = nlpir.segment(s, True)
        expected_seg_s = ['我们', '都', '是', '美国', '人', '。']
        expected_pos_seg_s = [('我们', 'rr'), ('都', 'd'), ('是', 'vshi'),
                              ('美国', 'nsf'), ('人', 'n'), ('。', 'wj')]
        self.assertEqual(expected_seg_s, seg_s)
        self.assertEqual(expected_pos_seg_s, pos_seg_s)
