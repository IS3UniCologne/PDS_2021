import os
import pandas as pd
import pickle


def read_file(path=os.getcwd()):
    if path == os.getcwd():
        print("Standard path")
    else:
        df = pd.read_csv(path)
        print("Read in dataframe.")
        # file cleaning ...
        return df


def read_model():
    with open("../output/model.pkl", "rb") as f:
        model = pickle.load(f)
    return model
