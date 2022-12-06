import sys
import unittest
import os
import pandas as pd
import numpy as np
from pathlib import Path

path_utils = Path(__file__).parent.parent
sys.path.append(str(path_utils))

from etl.save import save_csv
from etl.transform import no_change


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

path_test_csv = Path(__file__).parent.joinpath(
                                            "test_data"
                                            ).joinpath(
                                            "raw_data"
                                            ).joinpath(
                                            "prod_cat_info.csv"
                                            )

path_test_csv = str(path_test_csv)

class Mytest(unittest.TestCase):

    def test_save_csv(self):

        save_csv("test_df", TEST_DF)
        path = os.path.exists(str(TEST_PATH))
        self.assertTrue(path)
        os.remove(TEST_PATH)

    def test_no_change(self):

        df = no_change(path_test_csv)
        self.assertTrue(type(df) == pd.DataFrame)
        print("x")


if __name__ == '__main__':

    unittest.main()
    
