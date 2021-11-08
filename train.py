import numpy as np
import pandas as pd
import sklearn

from sklearn.linear_model import LogisticRegression as LR
from sklearn.ensemble import RandomForestClassifier as RFC
from sklearn.utils import shuffle

def load_training_data():
    """
    Load data to train model
    """
    return

def train(data):
    """
    Train model on data
    """
    x = data.drop(columns=["target"])
    y = data["target"]
    x.replace([np.inf, -np.inf], np.nan, inplace=True)  # change infs to NaNs
    # Should be dropna?
    # x.fillna(0, inplace=True)  # drop any NaNs for training
    scaler = sklearn.preprocessing.MinMaxScaler()  # setup Normalization
    x = scaler.fit_transform(x)  # normalize data
    #lr = LR()
    model = RFC()  # setup model
    model.fit(x, y)  # train model

def predict(model, data):
    """
    Use trained model to predict category of any pixel
    """
    return

def test(model, data):
    """
    After model is trained, predict on test data and report score
    """
    return

