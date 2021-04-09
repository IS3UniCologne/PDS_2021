import os
import pickle


def save_model(model):
    pickle.dump(model, open("../../output/model.pkl", "wb"))
    print("Model saved.")


def save_dummy():
    print("I'm a dummy function.")

