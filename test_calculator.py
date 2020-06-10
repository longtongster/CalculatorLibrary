# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 13:00:50 2020

@author: sacha
"""

"""
Unit tests for the calculator library
"""

import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)