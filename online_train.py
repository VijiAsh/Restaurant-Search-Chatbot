from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import tarfile
import os

import logging

from rasa_core.agent import Agent
from rasa_core.channels.console import CmdlineInput
from rasa_core.interpreter import RegexInterpreter
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter

logger = logging.getLogger(__name__)


def run_restaurant_online(input_channel, interpreter,
                          domain_file="domain.yml",
                          training_data_file='data/stories.md'):
    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(), KerasPolicy()],
                  interpreter=interpreter,
                  generator=None)

    agent.train(training_data_file,
                input_channel=input_channel,
                max_history=2,
                batch_size=50,
                epochs=200,
                max_training_samples=300,
                validation_split=0.2)

    return agent


if __name__ == '__main__':
    logging.basicConfig(level="INFO")
    directory = './models'
    for filename in os.listdir(directory):
        if filename.endswith(".tar.gz"):
            #print('FILE NAME== ',filename)
            tar = tarfile.open(os.path.join(directory, filename))
            tar.extractall()
            tar.close()
            continue
        else:
            continue
    nlu_interpreter = RasaNLUInterpreter('./nlu')
    run_restaurant_online(CmdlineInput(), nlu_interpreter)