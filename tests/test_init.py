# -*- coding: utf-8 -*-
"""Unit tests for pynlpir's __init__.py file."""
from __future__ import unicode_literals
import os
import shutil
import tempfile
import unittest
try:
    from urllib.error import URLError
except ImportError:
    from urllib2 import URLError

import pynlpir
from tests.utilities import timeout

DATA_DIR = os.path.join(pynlpir.nlpir.PACKAGE_DIR, 'Data')
TEST_DIR = os.path.abspath(os.path.dirname(__file__))
LICENSE_NAME = 'NLPIR.user'
LICENSE_FILE = os.path.join(TEST_DIR, 'data', LICENSE_NAME)


class TestNLPIR(unittest.TestCase):
    """Unit tests for pynlpir."""

    def setUp(self):
        try:
            pynlpir.cli.update_license_file(DATA_DIR)
        except URLError:
            pass

        pynlpir.open()

    def tearDown(self):
        pynlpir.close()

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

    def test_issue_52(self):
        """
        Tests for issue #52 -- segment(pos_names='all') fails for certain texts
        input.
        """
        # it seems '甲' returns 'Mg', which is not listed in the POS_MAP.
        # thus in this case 'None' needs to be returned for '甲'.
        s = u'其中，新增了甲卡西酮、曲马多、安钠咖等12种新类型毒品的定罪量刑数量标准，' \
            u'并下调了在我国危害较为严重的毒品氯胺酮的定罪量刑数量标准。'

        segments = pynlpir.segment(s=s, pos_tagging=True, pos_names='all')

        expected_segments = [
            (u'其中', 'pronoun:demonstrative pronoun'),
            (u'，', 'punctuation mark:comma'), (u'新增', 'verb'),
            (u'了', 'particle:particle 了/喽'), (u'甲', 'numeral'),
            (u'卡', 'noun'), (u'西', 'distinguishing word'), (u'酮', 'noun'),
            (u'、', 'punctuation mark:enumeration comma'),
            (u'曲马多', 'noun:personal name:transcribed personal name'),
            (u'、', 'punctuation mark:enumeration comma'),
            (u'安', 'noun:personal name:Chinese surname'), (u'钠', 'noun'),
            (u'咖', 'noun'), (u'等', 'particle:particle 等/等等/云云'),
            (u'12', 'numeral'), (u'种', 'classifier'), (u'新', 'adjective'),
            (u'类型', 'noun'), (u'毒品', 'noun'),
            (u'的', 'particle:particle 的/底'), (u'定罪', 'verb:noun-verb'),
            (u'量刑', 'verb:noun-verb'), (u'数量', 'noun'), (u'标准', 'noun'),
            (u'，', 'punctuation mark:comma'),
            (u'并', 'conjunction:coordinating conjunction'), (u'下调', 'verb'),
            (u'了', 'particle:particle 了/喽'), (u'在', 'preposition'),
            (u'我国', 'noun'), (u'危害', 'verb:noun-verb'), (u'较为', 'adverb'),
            (u'严重', 'adjective'), (u'的', 'particle:particle 的/底'),
            (u'毒品', 'noun'), (u'氯', 'noun'), (u'胺', 'noun'), (u'酮', 'noun'),
            (u'的', 'particle:particle 的/底'), (u'定罪', 'verb:noun-verb'),
            (u'量刑', 'verb:noun-verb'), (u'数量', 'noun'), (u'标准', 'noun'),
            (u'。', 'punctuation mark:period'),
        ]

        self.assertEqual(segments, expected_segments)


class TestNLPIRInit(unittest.TestCase):
    """Unit tests for pynlpir initialization."""

    def test_license_expire(self):
        """Tests that a LicenseError is raised if the license is invalid."""
        temp_dir = tempfile.mkdtemp()
        temp_data_dir = os.path.join(temp_dir, 'Data')
        shutil.copytree(DATA_DIR, temp_data_dir)
        shutil.copy(LICENSE_FILE, temp_data_dir)

        self.assertRaises(pynlpir.LicenseError, pynlpir.open, temp_dir)

        temp_license_file = os.path.join(temp_data_dir, LICENSE_NAME)
        os.remove(temp_license_file)

        self.assertRaises(pynlpir.LicenseError, pynlpir.open, temp_dir)

        shutil.rmtree(temp_dir)
