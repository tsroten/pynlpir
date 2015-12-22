# -*- coding: utf-8 -*-
"""Unit tests for pynlpir's __init__.py file."""
from __future__ import unicode_literals
import unittest

import pynlpir
from pynlpir.tests.utilities import timeout

pynlpir.open()


class TestNLPIR(unittest.TestCase):
    """Unit tests for pynlpir."""

    def test_segment(self):
        """Tests that the segment() function works as expected."""
        s = '我们都是美国人。'
        seg_s = pynlpir.segment(s, pos_tagging=False)
        pos_seg_s = pynlpir.segment(s, pos_tagging=True, pos_names='child')
        npos_seg_s = pynlpir.segment(s, pos_tagging=True, pos_names=None)
        ppos_seg_s = pynlpir.segment(s, pos_tagging=True, pos_names='all')
        expected_seg_s = ['我们', '都', '是', '美国', '人', '。']
        expected_pos_seg_s = [('我们', 'personal pronoun'), ('都', 'adverb'),
                              ('是', 'verb 是'), ('美国', 'transcribed toponym'),
                              ('人', 'noun'), ('。', 'period')]
        expected_npos_seg_s = [('我们', 'rr'), ('都', 'd'), ('是', 'vshi'),
                               ('美国', 'nsf'), ('人', 'n'), ('。', 'wj')]
        expected_ppos_seg_s = [('我们', 'pronoun:personal pronoun'),
                               ('都', 'adverb'), ('是', 'verb:verb 是'),
                               ('美国', 'noun:toponym:transcribed toponym'),
                               ('人', 'noun'), ('。', 'punctuation mark:period')]
        self.assertEqual(expected_seg_s, seg_s)
        self.assertEqual(expected_pos_seg_s, pos_seg_s)
        self.assertEqual(expected_npos_seg_s, npos_seg_s)
        self.assertEqual(expected_ppos_seg_s, ppos_seg_s)

    def test_segment_space(self):
        """Tests that the fix for issue #2 works."""
        s = '这个句子有 空格。'
        seg_s = pynlpir.segment(s, pos_tagging=False)
        pos_seg_s = pynlpir.segment(s)
        expected_seg_s = ['这个', '句子', '有', ' ', '空格', '。']
        expected_pos_seg_s = [('这个', 'pronoun'), ('句子', 'noun'),
                              ('有', 'verb'), (' ', None), ('空格', 'noun'),
                              ('。', 'punctuation mark')]
        self.assertEqual(expected_seg_s, seg_s)
        self.assertEqual(expected_pos_seg_s, pos_seg_s)

    def test_get_key_words(self):
        """Tests that the get_key_words() function works as expected."""
        s = '我们都是美国人。'
        key_words = pynlpir.get_key_words(s)
        weighted_key_words = pynlpir.get_key_words(s, weighted=True)
        expected_key_words = ['美国']
        expected_weighted_key_words = [('美国', 2.2)]
        self.assertEqual(expected_key_words, key_words)
        self.assertEqual(expected_weighted_key_words, weighted_key_words)

    def test_double_slash(self):
        """Tests for issue #7 -- double slashes raises exception."""
        s = '转发微博 //@张明明:霸气全露'
        seg_s = pynlpir.segment(s)
        expected_seg_s = [('转发', 'verb'), ('微', 'adjective'),
                          ('博', 'adjective'), (' ', None),
                          ('//', 'string'), ('@张明明', 'noun'),
                          (':', 'punctuation mark'), ('霸气', 'noun'),
                          ('全', 'adverb'), ('露', 'verb')]
        self.assertEqual(expected_seg_s, seg_s)

    def test_issue_23(self):
        """Tests for issue #20 -- get key words with no count returned."""
        s = '我们很好,你呢'
        weighted_key_words = pynlpir.get_key_words(s, weighted=True)
        expected_weighted_key_words = [('我们', -1.00)]
        self.assertEqual(expected_weighted_key_words, weighted_key_words)

    def test_issue_33(self):
        """Tests for issue #33 -- segment hangs with English and newline."""
        s = 'E\n'
        expected_seg_s = ['E']
        timeout_segment = timeout(timeout=1)(pynlpir.segment)
        try:
            seg_s = timeout_segment(s, False)
        except RuntimeError:
            self.fail('Segment function timed out.')
        self.assertEqual(expected_seg_s, seg_s)
