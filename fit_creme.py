from microprediction import MicroReader
from statsmodels.tsa.api import SimpleExpSmoothing
import os
import random
MODEL_FIT_PATH = os.path.dirname(os.path.realpath(__file__)) + os.path.sep + 'modelfits'

mr = MicroReader()
STREAMS = mr.get_stream_names()

from creme import preprocessing, compose, metrics, linear_model, stats, optim, datasets
from creme.time_series.snarimax import SNARIMAX

def fit_one():
    """ Pick a random stream and update parameters """
    name = random.choice(STREAMS)
    lagged_values = list(reversed(mr.get_lagged_values(name=name, count=5000)))
    LV = [ dict(time=v) for v in lagged_values ]
    model = SNARIMAX( p=0, d=0, q=0, m=12, sp=3, sq=6,
                      regressor=preprocessing.StandardScaler() |
                       linear_model.LinearRegression(
                        optimizer=optim.SGD(0.01),
                        intercept_lr=0.3))
    metric = metrics.Rolling(metrics.MAE(), 12)



if __name__=='__main__':
    fit_one()