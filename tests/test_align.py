# -*- coding: utf-8 -*-

import unittest
import json

import kraken
import dataclasses

from pathlib import Path

from kraken.lib import xml
from kraken.align import forced_align

thisfile = Path(__file__).resolve().parent
resources = thisfile / 'resources'

class TestKrakenAlign(unittest.TestCase):
    """
    Tests for the forced alignment module
    """
    def setUp(self):
        self.doc = resources / '170025120000003,0074.xml'
        self.bls = xml.XMLPage(self.doc).to_container()

    def test_forced_align_simple(self):
        """
        Simple alignment test.
        """
        pass
