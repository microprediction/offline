from microprediction import MicroReader
from statsmodels.tsa.api import SimpleExpSmoothing
import os
import random
MODEL_FIT_PATH = os.path.dirname(os.path.realpath(__file__)) + os.path.sep + 'modelfits' + os.path.sep + 'expsmooth'

mr = MicroReader()
STREAMS = mr.get_stream_names()


def fit_one():
    """ Pick a random stream and update parameters """
    name = random.choice(STREAMS)
    lagged_values = list(reversed(mr.get_lagged_values(name=name, count=5000)))
    if len(lagged_values)>300:
        model_fit = SimpleExpSmoothing(lagged_values, initialization_method="estimated").fit()
        model_fit.save(MODEL_FIT_PATH + os.path.sep + name.replace('.json', '.pkl'))


if __name__=='__main__':
    fit_one()