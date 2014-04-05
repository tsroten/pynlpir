# -*- coding: utf-8 -*-
"""Unit tests for pynlpir.pos_map."""
from __future__ import unicode_literals
import unittest

from pynlpir import pos_map


class TestPOSMap(unittest.TestCase):
    """Unit tests for the pynlpir.pos_map module."""

    def test_get_pos_name_no_parents_english(self):
        n_name = pos_map.get_pos_name('n')
        self.assertEqual('noun', n_name)

        ng_name = pos_map.get_pos_name('ng')
        self.assertEqual('noun morpheme', ng_name)

        nrf_name = pos_map.get_pos_name('nrf')
        self.assertEqual('transcribed personal name', nrf_name)

    def test_get_pos_name_no_parents_chinese(self):
        n_name = pos_map.get_pos_name('n', english=False)
        self.assertEqual('名词', n_name)

        ng_name = pos_map.get_pos_name('ng', english=False)
        self.assertEqual('名词性语素', ng_name)

        nrf_name = pos_map.get_pos_name('nrf', english=False)
        self.assertEqual('音译人名', nrf_name)

    def test_get_pos_name_parents_english(self):
        n_name = pos_map.get_pos_name('n', parents=True)
        self.assertEqual(('noun', ), n_name)

        ng_name = pos_map.get_pos_name('ng', parents=True)
        self.assertEqual(('noun', 'noun morpheme'), ng_name)

        nrf_name = pos_map.get_pos_name('nrf', parents=True)
        expected_nrf_name = ('noun', 'personal name',
                             'transcribed personal name')
        self.assertEqual(expected_nrf_name, nrf_name)

    def test_get_pos_name_parents_chinese(self):
        n_name = pos_map.get_pos_name('n', parents=True, english=False)
        self.assertEqual(('名词', ), n_name)

        ng_name = pos_map.get_pos_name('ng', parents=True, english=False)
        self.assertEqual(('名词', '名词性语素'), ng_name)

        nrf_name = pos_map.get_pos_name('nrf', parents=True, english=False)
        expected_nrf_name = ('名词', '人名', '音译人名')
        self.assertEqual(expected_nrf_name, nrf_name)

    def test_get_pos_name_wrong_code(self):
        self.assertRaises(ValueError, pos_map.get_pos_name, 'pqr')
