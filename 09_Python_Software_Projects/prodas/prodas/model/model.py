from .. import io
from sklearn.linear_model import LinearRegression


def hidden_function():
    pass


def create_model():
    lin = LinearRegression
    print("Linear model created")

    hidden_function()

    # ... train the model

    print("Linear model trained.")

    io.save_model(lin)

