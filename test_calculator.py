"""
Unit tests for the calculator app
"""

import calc


class TestCalculator:
    def test1(self):
        assert 5 == calc.add(1, 4)

    def test2(self):
        assert 2 == calc.subtract(4, 2)
        