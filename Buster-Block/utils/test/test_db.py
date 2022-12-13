import sys
import os
import unittest
import datetime
import pandas as pd
sys.path.append('Buster-Block')
import utils.db.connect as connect
import utils.db.queries as queries
from utils.db import upload


class TestConnect(unittest.TestCase):

    def test_connect(self):
        msj = 'Database connection error, info: '
        self.assertEqual(connect.msj, msj)


class TestQueries(unittest.TestCase):

    def test_fetchTable(self):
        msj = 'Unsuccesful query execution, more info: '
        self.assertEqual(queries.fetchTable('test', 'test', 'test', 'test'), msj)

    def test_addWhitespace(self):
        query = 'test'
        self.assertEqual(queries.addWhitespace(query), 'test ')


class TestUpload(unittest.TestCase):

    def test_root_file(self):
        self.assertEqual(type(upload.root_file()), dict)

    def test_create_db(self):
        msj = 'Failed to create tables successfully created, info: '
        self.assertEqual(upload.create_db(), msj)
    
    def test_upload_csv(self):
        msj = 'Error in the process of uploading data to the table '
        self.assertEqual(upload.upload_csv('test', 'test'), msj)
    
    def test_upload_city(self):
        dict_test = {'test': 'test'}
        msj = 'Error uploading the cities table'
        self.assertEqual(upload.upload_city(dict_test), msj)

    def test_upload_customers(self):
        dict_test = {'test': 'test'}
        msj = 'Error uploading the customers table'
        self.assertEqual(upload.upload_customers(dict_test), msj)

    def test_upload_product_categories(self):
        dict_test = {'test': 'test'}
        msj = 'Error uploading the product_categories table'
        self.assertEqual(upload.upload_product_categories(dict_test), msj)

    def test_upload_store_types(self):
        dict_test = {'test': 'test'}
        msj = 'Error uploading the store_types table'
        self.assertEqual(upload.upload_store_types(dict_test), msj)

    def test_upload_stores(self):
        dict_test = {'test': 'test'}
        msj = 'Error uploading the stores table'
        self.assertEqual(upload.upload_stores(dict_test), msj)
    
    def test_upload_transactions(self):
        dict_test = {'test': 'test'}
        msj = 'Error uploading the transactions table'
        self.assertEqual(upload.upload_transactions(dict_test), msj)

    def test_drop_all_tables(self):
        msj = 'Error in the drop of existing tables for data aggregation, info: '
        self.assertEqual(upload.drop_all_tables(), msj)

    def test_read_upload_csv(self):
        dict_test = {'test': 'test'}
        self.assertEqual(upload.read_upload_csv(dict_test), None)


if __name__ == '__main__':
    unittest.main()