import os
import pandas as pd


def read_file(path=os.getcwd()):
    if path == os.getcwd():
        print("Standard path")
    else:
        df = pd.read_csv(path)
        print("Read in dataframe.")

