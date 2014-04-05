# -*- coding: utf-8 -*-
"""Unit tests for pynlpir.pos_map."""
from __future__ import unicode_literals
import unittest

from pynlpir import pos_map


class TestPOSMap(unittest.TestCase):
    """Unit tests for the pynlpir.pos_map module."""

    def test_get_pos_name_child_english(self):
        n_name = pos_map.get_pos_name('n', names='child')
        self.assertEqual('noun', n_name)

        ng_name = pos_map.get_pos_name('ng', names='child')
        self.assertEqual('noun morpheme', ng_name)

        nrf_name = pos_map.get_pos_name('nrf', names='child')
        self.assertEqual('transcribed personal name', nrf_name)

    def test_get_pos_name_child_chinese(self):
        n_name = pos_map.get_pos_name('n', names='child', english=False)
        self.assertEqual('名词', n_name)

        ng_name = pos_map.get_pos_name('ng', names='child', english=False)
        self.assertEqual('名词性语素', ng_name)

        nrf_name = pos_map.get_pos_name('nrf', names='child', english=False)
        self.assertEqual('音译人名', nrf_name)

    def test_get_pos_name_all_english(self):
        n_name = pos_map.get_pos_name('n', names='all')
        self.assertEqual(('noun', ), n_name)

        ng_name = pos_map.get_pos_name('ng', names='all')
        self.assertEqual(('noun', 'noun morpheme'), ng_name)

        nrf_name = pos_map.get_pos_name('nrf', names='all')
        expected_nrf_name = ('noun', 'personal name',
                             'transcribed personal name')
        self.assertEqual(expected_nrf_name, nrf_name)

    def test_get_pos_name_all_chinese(self):
        n_name = pos_map.get_pos_name('n', names='all', english=False)
        self.assertEqual(('名词', ), n_name)

        ng_name = pos_map.get_pos_name('ng', names='all', english=False)
        self.assertEqual(('名词', '名词性语素'), ng_name)

        nrf_name = pos_map.get_pos_name('nrf', names='all', english=False)
        expected_nrf_name = ('名词', '人名', '音译人名')
        self.assertEqual(expected_nrf_name, nrf_name)

    def test_get_pos_name_parent_english(self):
        n_name = pos_map.get_pos_name('n', names='parent')
        self.assertEqual('noun', n_name)

        ng_name = pos_map.get_pos_name('ng', names='parent')
        self.assertEqual('noun', ng_name)

        nrf_name = pos_map.get_pos_name('nrf', names='parent')
        self.assertEqual('noun', nrf_name)

    def test_get_pos_name_parent_chinese(self):
        n_name = pos_map.get_pos_name('n', names='parent', english=False)
        self.assertEqual('名词', n_name)

        ng_name = pos_map.get_pos_name('ng', names='parent', english=False)
        self.assertEqual('名词', ng_name)

        nrf_name = pos_map.get_pos_name('nrf', names='parent', english=False)
        self.assertEqual('名词', nrf_name)

    def test_get_pos_name_wrong_code(self):
        self.assertRaises(ValueError, pos_map.get_pos_name, 'i')
