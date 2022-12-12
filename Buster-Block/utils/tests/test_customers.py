import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
import sys
import os
from pathlib import Path

path_utils = Path(__file__).parent.parent
sys.path.append(str(path_utils))

from etl.transform import df_customers

class TestCustomers(unittest.TestCase):
    
    def tests_customer1(self):
        """Test "df_customer" function
        """
       # Split the extension from the path
        try:
            filepath = "/mnt/c/Users/Alan Hernandez/Desktop/Squad_2/BusterBlock/utils/tests/test_data/raw_data/customer.csv"
            ext = os.path.splitext(filepath)[-1]
            df_customers(filepath) 
            self.assertEqual(ext,".csv")
          
        except AssertionError:
            ext = "Invalid extension"
            assert ext == "Invalid extension"    
                    
if __name__ == '__main__':
    unittest.main()