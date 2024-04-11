from unittest import TestCase
from solution import selectFirstRows
import pandas as pd

class TestSelectionOfFirst3Rows(TestCase):

    def test_case_larger_data_frame(self):
        df = pd.DataFrame({'column1': [1, 2, 3, 4], 'column2': ['a', 'b', 'c', 'd']})
        assert pd.DataFrame.equals(df.iloc[:3], selectFirstRows(df))

    def test_case_exactly_three(self):
        df = pd.DataFrame({'column1': [1, 2, 3], 'column2': ['a', 'b', 'c']})
        assert pd.DataFrame.equals(df.iloc[:3], selectFirstRows(df))

    def test_case_smaller_data_frame(self):
        df = pd.DataFrame({'column1': [1, 2], 'column2': ['a', 'b']})
        assert pd.DataFrame.equals(df.iloc[:2], selectFirstRows(df))

    def test_case_empty_data_frame(self):
        df = pd.DataFrame({})
        assert pd.DataFrame.equals(df.iloc[:], selectFirstRows(df))

