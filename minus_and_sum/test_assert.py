#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest


class Example(unittest.TestCase):
    def test_minus(self):
        self.assertEqual(2,3-1)
        print "minus"

    def test_sum(self):
        a,b,c = 1,1,3
        # self.assertEqual(5,a+b+c)
        print"sum"
