import os
import unittest
import pandas as pd
import numpy as np
from pandas.testing import assert_frame_equal
from pathlib import Path
import sys

path_utils = Path(__file__).parent.parent
sys.path.append(str(path_utils))

from etl.transform import df_prod, df_transactions, no_change
from etl.save import save_csv

# Constant variables
DIR = os.path.dirname(os.path.normpath(__file__))

TEST_DF = pd.DataFrame(
                    np.arange(12).reshape(3, 4),
                    columns=['A', 'B', 'C', 'D']
                    )
TEST_PATH = (Path(__file__).parent.parent.joinpath(
                                                "etl"
                                                ).joinpath(
                                                "processed_data"
                                                ).joinpath(
                                                "test_df"
                                                ))

PATH_TEST_CSV = str(Path(__file__).parent.joinpath(
                                            "test_data"
                                            ).joinpath(
                                            "raw_data"
                                            ).joinpath(
                                            "prod_cat_info.csv"
                                            ))


class TestTransform(unittest.TestCase):

    # Test transform.py
    def test_df_prod(self):
        """Test "df_prod" function
        """
        # input for "df_prod"
        test_input = f"{DIR}/test_data/raw_data/prod_cat_info.csv"
        # process dataframe, final output
        expected = pd.read_csv(f"{DIR}/test_data/process_data/prod_cat_info_prod.csv")
        expected.pop("Unnamed: 0.1")
        # process the input dataframe with "df_prod"
        actual = df_prod(test_input)
        # test if data frames are equal
        assert_frame_equal(actual, expected)

    def test_df_transactions(seld):
        """Test "df_transactions" function
        """
        test_input = f"{DIR}/test_data/raw_data/transactions.csv"
        expected = pd.read_csv(f"{DIR}/test_data/process_data/transactions_test.csv",
                               parse_dates=["transaction_date"])
        expected.pop("Unnamed: 0.1")
        actual = df_transactions(test_input)
        assert_frame_equal(actual, expected)

    def test_no_change(self):
        """
        Check that the function returns a pd.dataframe
        """
        df = no_change(PATH_TEST_CSV)
        self.assertEqual(type(df), pd.DataFrame)

    # Test save.py
    def test_save_csv(self):
        """
        Verify that the function saves a test file
        to the path and then deletes the saved test file
        """
        save_csv("test_df", TEST_DF)
        path = os.path.exists(str(TEST_PATH))
        self.assertTrue(path)
        os.remove(TEST_PATH)


if __name__ == '__main__':
    unittest.main()
