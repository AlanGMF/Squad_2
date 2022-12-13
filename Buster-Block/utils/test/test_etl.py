import sys
import os
import unittest
import datetime
import pandas as pd
sys.path.append('./Buster-Block')
import utils.etl.extraction as extraction
import utils.etl.transform as transform
import utils.etl.save as save

class TestExtraction(unittest.TestCase):
    """Extraction module test"""

    def test_root_file_(self):
        self.assertEqual(type(extraction.root_file()), dict)

    
class TestTransform(unittest.TestCase):
    """Transformation module test"""

    def test_standardization(self):
        dic_test = {'test' : 'test.csv'}
        msj = 'Error in the standardization process, info: '
        self.assertEqual(transform.standardization(dic_test), msj)
    
    def test_df_prod(self):
        bad_file = 'test'
        good_file = 'Buster-Block/utils/etl/raw_data/prod_cat_info.csv'
        msj = 'Error transforming file test_transactions.csv, info: '
        self.assertEqual(transform.df_prod(bad_file), msj)
        self.assertEqual(type(transform.df_prod(good_file)), pd.DataFrame)

    def test_df_transactions(self):
        bad_file = 'test'
        good_file = 'Buster-Block/utils/etl/raw_data/transactions.csv'
        msj = 'Error transforming file transactions.csv, info: '
        self.assertEqual(transform.df_transactions(bad_file), msj)
        self.assertEqual(type(transform.df_transactions(good_file)), pd.DataFrame)
    
    def test_df_customers(self):
        bad_file = 'test'
        good_file = 'Buster-Block/utils/etl/raw_data/customer.csv'
        msj = 'Error transforming file customer.csv, info: '
        self.assertEqual(transform.df_customers(bad_file), msj)
        self.assertEqual(type(transform.df_customers(good_file)), pd.DataFrame)
    
    def test_no_change(self):
        file = 'Buster-Block/utils/etl/raw_data/stores.csv'
        self.assertEqual(type(transform.no_change(file)), pd.DataFrame)

class TestSave(unittest.TestCase):
    """Test the save module"""

    def test_save_csv(self):
        file = 'test'
        df = 'test'
        msj = 'File saving error '
        self.assertEqual(save.save_csv(file, df), msj)


if __name__ == '__main__':
    unittest.main()