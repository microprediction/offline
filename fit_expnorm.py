from microprediction import MicroReader
from microprediction.univariate.expnormdist import ExpNormDist
import os
import random
import json
from pprint import pprint
from copy import deepcopy
MODEL_FIT_PATH = os.path.dirname(os.path.realpath(__file__)) + os.path.sep + 'modelfits' + os.path.sep + 'expnorm'
import matplotlib.pyplot as plt
import time

mr = MicroReader()
STREAMS = mr.get_stream_names()



DEFAULT_EXPNORM_PARAMS = {'g1': 0.5, 'g2': 5.0, 'logK': -2., 'loc': 0.0, 'logScale': 0.0}
DEFAULT_EXPNORM_LOWER = {'g1': 0.001, 'g2': 0.001, 'logK': -5, 'loc': -0.15, 'logScale': -4}
DEFAULT_EXPNORM_UPPER = {'g1': 1.0, 'g2': 15.0, 'logK': 1, 'loc': 0.15, 'logScale': 4.0}
OFFLINE_EXPNORM_HYPER = {'lower_bounds': deepcopy(DEFAULT_EXPNORM_LOWER),
                         'upper_bounds': deepcopy(DEFAULT_EXPNORM_UPPER),
                         'space': None, 'algo': None, 'max_evals': 250}


class ExpNormAccumulator(ExpNormDist):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def anchors(self, lagged_values, lagged_times):
        def post_getter(state, value, machine):
            return state['anchor']
        return self.replay(lagged_values=lagged_values, lagged_times=lagged_times, post_getter=post_getter)



def plot_machine(machine, lagged_values, lagged_times, c='g', num=100):
    anchors = machine.anchors(lagged_values=lagged_values, lagged_times=lagged_times)
    chronological_times = list(reversed(lagged_times))
    chronological_values = list(reversed(lagged_values))
    plt.plot(chronological_times[-num:], anchors[-num:], c=c)
    plt.plot(chronological_times[-num:], chronological_values[-num:], 'b+')


def fit_one():
    """ Pick a random stream and update parameters """
    name = random.choice(STREAMS)
    lagged_values, lagged_times = mr.get_lagged_values_and_times(name=name, count=5000)
    start_time = time.time()
    if len(lagged_values)>300:
        machine = ExpNormAccumulator(hyper_params=OFFLINE_EXPNORM_HYPER)
        plot_machine(machine=machine, lagged_values=lagged_values, lagged_times=lagged_times)
        params_before = deepcopy(machine.params)
        plt.title('Before')
        plt.pause(0.001)
        machine.fit(lagged_values=lagged_values, lagged_times=lagged_times)
        params_after = deepcopy(machine.params)
        print('Params before ')
        pprint(params_before)
        print('Params after fitting ')
        pprint(params_after)

        param_file = MODEL_FIT_PATH+os.path.sep + name
        with open(param_file, 'w') as fp:
            json.dump(machine.params, fp)
        # Example run forward
        plot_machine(machine=machine, lagged_values=lagged_values, lagged_times=lagged_times, c='r')
        plt.title('After')
        plot_file = param_file.replace('.json','.png')
        plt.savefig(plot_file)
        end_time = time.time()
        print('Elapsed minutes = '+str((end_time-start_time)/60.))
        pass


if __name__=='__main__':
    fit_one()