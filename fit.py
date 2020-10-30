from microprediction import MicroReader
from statsmodels.tsa.api import SimpleExpSmoothing
import os
MODEL_FIT = os.path.dirname(os.path.realpath(__file__))+os.path.sep+'modelfits'

STREAMS = ['electricity-load-nyiso-overall.json']


def fit_all():
    mr = MicroReader()
    for name in STREAMS:
        lagged_values = list(reversed(mr.get_lagged_values(name=name, count=5000)))
        if len(lagged_values)>300:
            model_fit = SimpleExpSmoothing(lagged_values, initialization_method="estimated").fit()
            model_fit.save(MODEL_FIT+os.path.sep+name.replace('.json','.pkl'))


if __name__=='__main__':
    fit_all()