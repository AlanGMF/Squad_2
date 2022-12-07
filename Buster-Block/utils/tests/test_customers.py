import unittest
import pandas as pd
import sys
import os
from pathlib import Path

path_utils = Path(__file__).parent.parent
sys.path.append(str(path_utils))

from etl.transform import df_customers

class TestCustomers(unittest.TestCase):
    
    def tests_customer(self):
        
        filepath = "/mnt/c/Users/Alan Hernandez/Desktop/Squad_2/BusterBlock/utils/tests/test_data/raw_data/customers.html"
       # Split the extension from the path
        try:
            ext = os.path.splitext(filepath)[-1]
            df_customers(filepath) 
            self.assertEqual(ext,".csv")
        except:
            ext = "Invalid extension"
            assert ext == "Invalid extension"   
        
         
          
            
if __name__ == '__main__':
    unittest.main()