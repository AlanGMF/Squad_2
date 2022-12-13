import os
import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
from BusterBlock.utils.etl.transform import df_prod, df_transactions

# dir path
DIR = os.path.dirname(os.path.normpath(__file__))


class TestTransform(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()
